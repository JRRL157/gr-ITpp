/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_BER_ANALYZER_CPP_IMPL_H
#define INCLUDED_ITPP_BER_ANALYZER_CPP_IMPL_H

#include <gnuradio/ITpp/BER_Analyzer_cpp.h>

namespace gr {
  namespace ITpp {

    class BER_Analyzer_cpp_impl : public BER_Analyzer_cpp
    {
     private:
      std::map<float,int[3]> records;

     public:
      BER_Analyzer_cpp_impl();
      ~BER_Analyzer_cpp_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);

    };

  } // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_BER_ANALYZER_CPP_IMPL_H */
