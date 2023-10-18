/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_HAMMING_SOFT_DECODER_IMPL_H
#define INCLUDED_ITPP_HAMMING_SOFT_DECODER_IMPL_H

#include <gnuradio/ITpp/Hamming_Soft_Decoder.h>
#include <itpp/itbase.h>
#include <itpp/comm/hammcode.h>

namespace gr {
namespace ITpp {

class Hamming_Soft_Decoder_impl : public Hamming_Soft_Decoder {
private:
  int d_m;
  int d_K, d_N;
  itpp::bmat U;
  itpp::Mat<float> A;
  int flag = 0;
public:
  Hamming_Soft_Decoder_impl(int m);
  ~Hamming_Soft_Decoder_impl();

  // Where all the action really happens
  void forecast (int noutput_items, gr_vector_int &ninput_items_required);

  int general_work(int noutput_items,
        gr_vector_int &ninput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items);
        
  template <typename T>
  void vecPrint(itpp::Vec<T> &x);
  template <typename T>
  itpp::Vec<T> vecMultMat(itpp::Vec<T> &v, itpp::Mat<T> &mat);
  
  itpp::bvec bvecMultbMat(itpp::bvec& v, itpp::bmat &mat);
  itpp::bmat identityMatrix(int N);
  itpp::bvec soft_decode(itpp::Vec<float>& encoded);
  int getMaxElementIndex(itpp::Vec<float>& vec);
};

} // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_HAMMING_DECODER_IMPL_H */
