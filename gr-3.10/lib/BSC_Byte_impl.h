/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_BSC_BYTE_IMPL_H
#define INCLUDED_ITPP_BSC_BYTE_IMPL_H

#include <gnuradio/ITpp/BSC_Byte.h>

namespace gr {
namespace ITpp {

class BSC_Byte_impl : public BSC_Byte {
private:
  int d_bits;
  float d_probability;

public:
  BSC_Byte_impl(int bits, float probability);
  ~BSC_Byte_impl();

  // Where all the action really happens
  int work(int noutput_items, gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
};

} // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_BSC_BYTE_IMPL_H */
