/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "RS_Decoder_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace ITpp {

using input_type = unsigned char;
using output_type = unsigned char;
RS_Decoder::sptr RS_Decoder::make(int m, int t) {
  return gnuradio::make_block_sptr<RS_Decoder_impl>(m, t);
}

/*
 * The private constructor
 */
RS_Decoder_impl::RS_Decoder_impl(int m, int t)
    : gr::block(
          "RS_Decoder",
          gr::io_signature::make(1, 1, sizeof(input_type)),
          gr::io_signature::make(1, 1,sizeof(output_type))),
      bloco(m, t)
{
  d_N = m * (itpp::round_i(pow(2.0, m) - 1));
  d_K = m * (itpp::round_i(pow(2.0, m)) - 1 - 2 * t);
  encoded.set_length(d_N);
  decoded.set_length(d_K);
  set_output_multiple(d_K);
}

/*
 * Our virtual destructor.
 */
RS_Decoder_impl::~RS_Decoder_impl() {}

void RS_Decoder_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
{
  ninput_items_required[0] = (int)(noutput_items * ((float)d_N)/((float)d_K));
}

int RS_Decoder_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
{
  auto in = static_cast<const input_type *>(input_items[0]);
  auto out = static_cast<output_type *>(output_items[0]);

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
