/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_BCH_ENCODER_IMPL_H
#define INCLUDED_ITPP_BCH_ENCODER_IMPL_H

#include <gnuradio/ITpp/BCH_Encoder.h>

namespace gr {
namespace ITpp {

class BCH_Encoder_impl : public BCH_Encoder {
private:
  // Nothing to declare in this block.

public:
  BCH_Encoder_impl(n, t);
  ~BCH_Encoder_impl();

  // Where all the action really happens
  int work(int noutput_items, gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
};

} // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_BCH_ENCODER_IMPL_H */
