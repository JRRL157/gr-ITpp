/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "Hamming_Decoder_impl.h"
#include <gnuradio/io_signature.h>

#include <itpp/itbase.h>
#include <itpp/comm/hammcode.h>

namespace gr {
namespace ITpp {

using input_type = unsigned char;
using output_type = unsigned char;
Hamming_Decoder::sptr Hamming_Decoder::make(int m) {
  return gnuradio::make_block_sptr<Hamming_Decoder_impl>(m);
}

/*
 * The private constructor
 */
Hamming_Decoder_impl::Hamming_Decoder_impl(int m)
    : gr::block(
          "Hamming_Decoder",
          gr::io_signature::make(1, 1, sizeof(input_type)),
          gr::io_signature::make(1, 1, sizeof(output_type)))
{
  d_m = m;

  itpp::Hamming_Code block(d_m);
  d_K = block.get_k();
  d_N = block.get_n();

  set_output_multiple(d_K);
}

/*
 * Our virtual destructor.
 */
Hamming_Decoder_impl::~Hamming_Decoder_impl() {}

void Hamming_Decoder_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
{
  ninput_items_required[0] = (int)(noutput_items * ((float)d_N)/((float)d_K));
}

int Hamming_Decoder_impl::general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items)
{
  auto in = static_cast<const input_type *>(input_items[0]);
  auto out = static_cast<output_type *>(output_items[0]);

  itpp::bvec decoded, encoded;
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

    for(int j = 0; j < d_K; j++){
      out[d_K*i+j] = (int)decoded.get(j);
    }
  }

  consume(0, (int)(noutput_items * ((float)d_N)/((float)d_K)));

  return noutput_items;
}

} /* namespace ITpp */
} /* namespace gr */
