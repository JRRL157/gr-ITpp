/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_BER_ANALYZER_CPP_H
#define INCLUDED_ITPP_BER_ANALYZER_CPP_H

#include <gnuradio/ITpp/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace ITpp {

    /*!
     * \brief <+description of block+>
     * \ingroup ITpp
     *
     */
    class ITPP_API BER_Analyzer_cpp : virtual public gr::block
    {
     public:
      typedef std::shared_ptr<BER_Analyzer_cpp> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of ITpp::BER_Analyzer_cpp.
       *
       * To avoid accidental use of raw pointers, ITpp::BER_Analyzer_cpp's
       * constructor is in a private implementation
       * class. ITpp::BER_Analyzer_cpp::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_BER_ANALYZER_CPP_H */
