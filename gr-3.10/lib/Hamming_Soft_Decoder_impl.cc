/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "Hamming_Soft_Decoder_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace ITpp {

using input_type = unsigned char;
using output_type = unsigned char;
Hamming_Soft_Decoder::sptr Hamming_Soft_Decoder::make(int m) {
  return gnuradio::make_block_sptr<Hamming_Soft_Decoder_impl>(m);
}

/*
 * The private constructor
 */
Hamming_Soft_Decoder_impl::Hamming_Soft_Decoder_impl(int m)
    : gr::block(
          "Hamming_Soft_Decoder",
          gr::io_signature::make(1, 1, sizeof(input_type)),
          gr::io_signature::make(1, 1, sizeof(output_type)))
{
  d_m = m;

  itpp::Hamming_Code block(d_m);
  d_K = block.get_k();
  d_N = block.get_n();
  itpp::bmat Gt = block.get_G().transpose();
  
  itpp::bmat C;
  
  int numMessages = (1 << d_K); // Calcula 2^K

  for (int i = 0; i < numMessages; ++i) {
      itpp::bvec u;
      u.set_length(d_K);
      u.zeros();
      for (int j = 0; j < d_K; ++j) {
          int bit = (i >> j) & 1; // Obtém o bit na posição j
          u.set(j,bit);
      }
      
      itpp::bvec v = vecMultMat(u,Gt);
      vecPrint(v);
      C.append_row(v);
  }

  itpp::Mat<float> A(numMessages,d_N);
  
  for(int i = 0;i<C.rows();i++){
    for(int j = 0;j<C.cols();j++){
      A.set(i,j,C.get(i,j));
    }
  }

  A = A.transpose();
  A *= 2;
  A -= 1;

  this->A = A;

  for(int i = 0;i<A.rows();i++){
    itpp::Vec<float> row = A.get_row(i);
    vecPrint(row);
  }
  
  std::printf("HEYA!");

  set_output_multiple(d_K);
}

/*
 * Our virtual destructor.
 */
Hamming_Soft_Decoder_impl::~Hamming_Soft_Decoder_impl() {}

void Hamming_Soft_Decoder_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
{
  ninput_items_required[0] = (int)(noutput_items * ((float)d_N)/((float)d_K));
}

int Hamming_Soft_Decoder_impl::general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items)
{
  auto in = static_cast<const input_type *>(input_items[0]);
  auto out = static_cast<output_type *>(output_items[0]);

  itpp::bvec decoded,decoded2, encoded;
  encoded.set_length(d_N);
  encoded.zeros();
  itpp::Hamming_Code block(d_m);

  for(int i = 0; i < noutput_items/d_K; i++){
    for(int j = 0; j < d_K; j++){
      out[d_K*i+j] = 0;
    }

    for(int j = 0; j < d_N; j++){
      encoded(j) = in[d_N*i+j];
    }

    decoded = block.decode(encoded);
    soft_decode(encoded);

    for(int j = 0; j < d_K; j++){
      out[d_K*i+j] = (int)decoded.get(j);
    }
  }

  consume(0, (int)(noutput_items * ((float)d_N)/((float)d_K)));

  return noutput_items;
}

template <typename T>
void Hamming_Soft_Decoder_impl::vecPrint(itpp::Vec<T> &x)
{
  int L = x.size();

  for(int i = 0;i < L;i++)
    std::printf("%d ",(int)x.get(i));
  std::printf("\n");
}

template<typename T>
itpp::Vec<T> Hamming_Soft_Decoder_impl::vecMultMat(itpp::Vec<T> &v, itpp::Mat<T> &mat) {
    if (v.length() != mat.cols()) {
        throw std::runtime_error("O número de colunas da matriz deve ser igual ao tamanho do vetor.");
    }

    itpp::Vec<T> result(mat.rows());

    for (int row = 0; row < mat.rows(); ++row) {
        T rowResult = 0;
        for (int col = 0; col < mat.cols(); ++col) {
            // Realize a multiplicação bit a bit e adicione ao resultado da linha.
            rowResult += (T)v.get(col) * (T)mat(row, col);
        }
        // Defina o bit no resultado como 1 se rowResult for ímpar, caso contrário, 0.
        result.set(row, rowResult);
    }

    return result;
}
itpp::bvec Hamming_Soft_Decoder_impl::bvecMultbMat(itpp::bvec &v, itpp::bmat &mat) {
    if (v.length() != mat.cols()) {
        throw std::runtime_error("O número de colunas da matriz deve ser igual ao tamanho do vetor.");
    }

    itpp::bvec result(mat.rows());

    for (int row = 0; row < mat.rows(); ++row) {
        int rowResult = 0;
        for (int col = 0; col < mat.cols(); ++col) {
            // Realize a multiplicação bit a bit e adicione ao resultado da linha.
            rowResult += (int)v.get(col) * (int)mat(row, col);
        }
        // Defina o bit no resultado como 1 se rowResult for ímpar, caso contrário, 0.
        result.set(row, rowResult % 2);
    }

    return result;
}

itpp::bmat Hamming_Soft_Decoder_impl::identityMatrix(int N)
{
    itpp::bmat identity(N, N);
    
    for (int i = 0; i < N; i++) {
        identity.set(i, i, 1.0);
    }
    
    return identity;
}

itpp::bvec Hamming_Soft_Decoder_impl::soft_decode(itpp::bvec& encoded)
{
  itpp::bvec bvec;
  if(!flag){
    itpp::Vec<float> v;
    v.set_length(encoded.length());
    v.zeros();
    
    for(int i = 0;i<encoded.length();i++)
      v.set(i,encoded.get(i));

    std::printf("A = (%d,%d)\n",A.rows(),A.cols());
    itpp::Mat<float> At = A.transpose();
    itpp::Vec<float> B = vecMultMat(v,At);
    vecPrint(B);
    
    this->flag = true;
  }
  return bvec;
}

} /* namespace ITpp */
} /* namespace gr */
