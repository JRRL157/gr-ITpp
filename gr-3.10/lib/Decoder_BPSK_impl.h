/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_DECODER_BPSK_IMPL_H
#define INCLUDED_ITPP_DECODER_BPSK_IMPL_H

#include <gnuradio/ITpp/Decoder_BPSK.h>

namespace gr {
  namespace ITpp {

    class Decoder_BPSK_impl : public Decoder_BPSK
    {
     private:
      int d_m;
      int d_K, d_N;

     public:
      Decoder_BPSK_impl(int m);
      ~Decoder_BPSK_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);

    };

  } // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_DECODER_BPSK_IMPL_H */
