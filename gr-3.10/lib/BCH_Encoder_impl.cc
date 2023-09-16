/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "BCH_Encoder_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace ITpp {

using input_type = unsigned char;
using output_type = unsigned char;
BCH_Encoder::sptr BCH_Encoder::make(int n, int t) {
  return gnuradio::make_block_sptr<BCH_Encoder_impl>(n, t);
}

/*
 * The private constructor
 */
BCH_Encoder_impl::BCH_Encoder_impl(int n, int t)
    : gr::block(
          "BCH_Encoder",
          gr::io_signature::make(1, 1, sizeof(input_type)),
          gr::io_signature::make(1, 1, sizeof(output_type))),
      bloco(n, t)
{
  d_N = n;
  d_T = t;
  d_K = bloco.get_k();
  uncoded.set_length(d_K);
  set_output_multiple(d_N);
}

/*
 * Our virtual destructor.
 */
BCH_Encoder_impl::~BCH_Encoder_impl() {}

void BCH_Encoder_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
{
  ninput_items_required[0] = (int)(noutput_items * ((float)d_K)/((float)d_N));
}

int BCH_Encoder_impl::general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items)
{
  auto in = static_cast<const input_type *>(input_items[0]);
  auto out = static_cast<output_type *>(output_items[0]);

  uncoded.zeros();

  for(int i = 0; i < noutput_items/d_N; i++){
    
    for(int j = 0; j < d_N; j++){
      out[d_N*i+j] = 0;
    }

    for(int j = 0; j < d_K; j++){
      uncoded(j) = in[d_K*i+j];
    }
    
    encoded = bloco.encode(uncoded);

    for(int j = 0; j < d_N; j++){
      out[d_N*i+j] = (int)encoded.get(j);
    }

  }

  consume(0, (int)(noutput_items * ((float)d_K)/((float)d_N)));
  return noutput_items;
}

} /* namespace ITpp */
} /* namespace gr */
