/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_BCH_DECODER_IMPL_H
#define INCLUDED_ITPP_BCH_DECODER_IMPL_H

#include <gnuradio/ITpp/BCH_Decoder.h>

#include <itpp/itbase.h>
#include <itpp/comm/bch.h>

namespace gr {
namespace ITpp {

class BCH_Decoder_impl : public BCH_Decoder {
private:
    int d_N, d_K, d_T;
    itpp::BCH bloco;
    itpp::bvec decoded, encoded;

public:
  BCH_Decoder_impl(int n, int t);
  ~BCH_Decoder_impl();

  // Where all the action really happens
  void forecast (int noutput_items, gr_vector_int &ninput_items_required);

  int general_work(int noutput_items, gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items, gr_vector_void_star &output_items);
};

} // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_BCH_DECODER_IMPL_H */
