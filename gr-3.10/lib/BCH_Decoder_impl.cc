/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "BCH_Decoder_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace ITpp {

using input_type = unsigned char;
using output_type = unsigned char;
BCH_Decoder::sptr BCH_Decoder::make(int n, int t) {
  return gnuradio::make_block_sptr<BCH_Decoder_impl>(n, t);
}

/*
 * The private constructor
 */
BCH_Decoder_impl::BCH_Decoder_impl(int n, int t)
    : gr::block(
          "BCH_Decoder",
          gr::io_signature::make(1, 1, sizeof(input_type)),
          gr::io_signature::make(1, 1, sizeof(output_type))),
          bloco(n, t)
{
    d_N = n;
    d_T = t;
    d_K = bloco.get_k();
    encoded.set_length(d_N);
    set_output_multiple(d_K);
}

/*
 * Our virtual destructor.
 */
BCH_Decoder_impl::~BCH_Decoder_impl() {}

void BCH_Decoder_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
{
  ninput_items_required[0] = (int)(noutput_items * ((float)d_N)/((float)d_K));
}

int BCH_Decoder_impl::general_work(int noutput_items,
                           gr_vector_int &ninput_items,
                           gr_vector_const_void_star &input_items,
                           gr_vector_void_star &output_items)
{
  auto in = static_cast<const input_type *>(input_items[0]);
  auto out = static_cast<output_type *>(output_items[0]);

  encoded.zeros();

  for(int i = 0; i < noutput_items/d_K; i++){
    for(int j = 0; j < d_K; j++){
      out[d_K*i+j] = 0;
    }

    for(int j = 0; j < d_N; j++){
      encoded(j) = in[d_N*i+j];
    }

    decoded = bloco.decode(encoded);

    for(int j = 0; j < d_K; j++){
      out[d_K*i+j] = (int)decoded.get(j);
    }
  }

  consume(0, (int)(noutput_items * ((float)d_N)/((float)d_K)));

  return noutput_items;
}

} /* namespace ITpp */
} /* namespace gr */
