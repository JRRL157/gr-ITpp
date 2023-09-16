/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */
#include <gnuradio/io_signature.h>

#include <itpp/itbase.h>
#include <itpp/comm/channel.h>

#include "BSC_Byte_impl.h"

namespace gr {
namespace ITpp {

using input_type = unsigned char;
using output_type = unsigned char;
BSC_Byte::sptr BSC_Byte::make(int bits, float probability) {
  return gnuradio::make_block_sptr<BSC_Byte_impl>(bits, probability);
}

/*
 * The private constructor
 */
BSC_Byte_impl::BSC_Byte_impl(int bits, float probability)
    : gr::sync_block(
          "BSC_Byte",
          gr::io_signature::make(1 /* min inputs */, 1 /* max inputs */,
                                 sizeof(input_type)),
          gr::io_signature::make(1 /* min outputs */, 1 /*max outputs */,
                                 sizeof(output_type)))
{
  d_probability = probability;
  d_bits = bits;

  itpp::RNG_randomize();
}

/*
 * Our virtual destructor.
 */
BSC_Byte_impl::~BSC_Byte_impl() {}

int BSC_Byte_impl::work(int noutput_items,
                        gr_vector_const_void_star &input_items,
                        gr_vector_void_star &output_items) {
  auto in = static_cast<const input_type *>(input_items[0]);
  auto out = static_cast<output_type *>(output_items[0]);

  itpp::bvec entrada_bits;
  entrada_bits.set_length(d_bits);
  entrada_bits.zeros();

  for(int j = 0; j < noutput_items; j++){
    out[j] = 0;

    //RNG_randomize();
    itpp::BSC bsc(d_probability);

    for(int i = 0; i < d_bits; i++){
      entrada_bits(i) = (in[j] >> i) & 0x01;
    }

    entrada_bits = bsc(entrada_bits);

    for(int i = 0; i < d_bits; i++){
      out[j] |= ((int)entrada_bits.get(i) << i);
    }

  }

  return noutput_items;
}

} /* namespace ITpp */
} /* namespace gr */
