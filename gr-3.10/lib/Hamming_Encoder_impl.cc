/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "Hamming_Encoder_impl.h"
#include <gnuradio/io_signature.h>

#include <itpp/itbase.h>
#include <itpp/comm/hammcode.h>

namespace gr {
namespace ITpp {

using input_type = unsigned char;
using output_type = unsigned char;
Hamming_Encoder::sptr Hamming_Encoder::make(int m) {
  return gnuradio::make_block_sptr<Hamming_Encoder_impl>(m);
}

/*
 * The private constructor
 */
Hamming_Encoder_impl::Hamming_Encoder_impl(int m)
    : gr::block(
          "Hamming_Encoder",
          gr::io_signature::make(1, 1, sizeof(input_type)),
          gr::io_signature::make(1, 1, sizeof(output_type)))
{
  d_m = m;

  itpp::Hamming_Code block(d_m);
  d_K = block.get_k();
  d_N = block.get_n();

  std::printf("constructor(): d_K = %d, d_N = %d\n", d_K, d_N);

  set_output_multiple(d_N);
}

/*
 * Our virtual destructor.
 */
Hamming_Encoder_impl::~Hamming_Encoder_impl() {}

void Hamming_Encoder_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
{
  ninput_items_required[0] = (int)(noutput_items * ((float)d_K)/((float)d_N));
}

int Hamming_Encoder_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
{
  auto in = static_cast<const input_type *>(input_items[0]);
  auto out = static_cast<output_type *>(output_items[0]);

  itpp::bvec uncoded, encoded;
  uncoded.set_length(d_K);
  uncoded.zeros();
  itpp::Hamming_Code block(d_m);

  for(int i = 0; i < noutput_items/d_N; i++){
    
    for(int j = 0; j < d_N; j++){
      out[d_N*i+j] = 0;
    }

    for(int j = 0; j < d_K; j++){
      uncoded(j) = in[d_K*i+j];
    }
    
    encoded = block.encode(uncoded);

    for(int j = 0; j < d_N; j++){
      out[d_N*i+j] = (int)encoded.get(j);
    }

  }

  consume(0, (int)(noutput_items * ((float)d_K)/((float)d_N)));
  return noutput_items;
}

} /* namespace ITpp */
} /* namespace gr */
