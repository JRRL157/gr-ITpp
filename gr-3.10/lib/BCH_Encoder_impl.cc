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

#pragma message("set the following appropriately and remove this warning")
using input_type = float;
#pragma message("set the following appropriately and remove this warning")
using output_type = float;
BCH_Encoder::sptr BCH_Encoder::make(int n, int t) {
  return gnuradio::make_block_sptr<BCH_Encoder_impl>(n, t);
}

/*
 * The private constructor
 */
BCH_Encoder_impl::BCH_Encoder_impl(int n, int t)
    : gr::sync_block(
          "BCH_Encoder",
          gr::io_signature::make(1 /* min inputs */, 1 /* max inputs */,
                                 sizeof(input_type)),
          gr::io_signature::make(1 /* min outputs */, 1 /*max outputs */,
                                 sizeof(output_type))) {}

/*
 * Our virtual destructor.
 */
BCH_Encoder_impl::~BCH_Encoder_impl() {}

int BCH_Encoder_impl::work(int noutput_items,
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
