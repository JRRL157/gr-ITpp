/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_HAMMING_DECODER_IMPL_H
#define INCLUDED_ITPP_HAMMING_DECODER_IMPL_H

#include <gnuradio/ITpp/Hamming_Decoder.h>

namespace gr {
namespace ITpp {

class Hamming_Decoder_impl : public Hamming_Decoder {
private:
  // Nothing to declare in this block.

public:
  Hamming_Decoder_impl(int m);
  ~Hamming_Decoder_impl();

  // Where all the action really happens
  int work(int noutput_items, gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
};

} // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_HAMMING_DECODER_IMPL_H */
