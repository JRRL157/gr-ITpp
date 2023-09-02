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

#pragma message("set the following appropriately and remove this warning")
using input_type = float;
#pragma message("set the following appropriately and remove this warning")
using output_type = float;
RS_Decoder::sptr RS_Decoder::make(m, t) {
  return gnuradio::make_block_sptr<RS_Decoder_impl>(m, t);
}

/*
 * The private constructor
 */
RS_Decoder_impl::RS_Decoder_impl(m, t)
    : gr::sync_block(
          "RS_Decoder",
          gr::io_signature::make(1 /* min inputs */, 1 /* max inputs */,
                                 sizeof(input_type)),
          gr::io_signature::make(1 /* min outputs */, 1 /*max outputs */,
                                 sizeof(output_type))) {}

/*
 * Our virtual destructor.
 */
RS_Decoder_impl::~RS_Decoder_impl() {}

int RS_Decoder_impl::work(int noutput_items,
                          gr_vector_const_void_star &input_items,
                          gr_vector_void_star &output_items) {
  auto in = static_cast<const input_type *>(input_items[0]);
  auto out = static_cast<output_type *>(output_items[0]);

#pragma message(                                                               \
        "Implement the signal processing in your block and remove this warning")
  // Do <+signal processing+>

  // Tell runtime system how many output items we produced.
  return noutput_items;
}

} /* namespace ITpp */
} /* namespace gr */
