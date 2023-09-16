/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_RS_ENCODER_IMPL_H
#define INCLUDED_ITPP_RS_ENCODER_IMPL_H

#include <gnuradio/ITpp/RS_Encoder.h>

#include <itpp/itcomm.h>

namespace gr {
namespace ITpp {

class RS_Encoder_impl : public RS_Encoder {
private:
  int d_N, d_K, d_T;
  itpp::Reed_Solomon bloco;
  itpp::bvec uncoded, encoded;

public:
  RS_Encoder_impl(int m, int t);
  ~RS_Encoder_impl();

  // Where all the action really happens
  void forecast (int noutput_items, gr_vector_int &ninput_items_required);

  int general_work(int noutput_items,
        gr_vector_int &ninput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items);
};

} // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_RS_ENCODER_IMPL_H */
