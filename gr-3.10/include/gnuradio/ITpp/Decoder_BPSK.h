/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_DECODER_BPSK_H
#define INCLUDED_ITPP_DECODER_BPSK_H

#include <gnuradio/ITpp/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace ITpp {

    /*!
     * \brief <+description of block+>
     * \ingroup ITpp
     *
     */
    class ITPP_API Decoder_BPSK : virtual public gr::block
    {
     public:
      typedef std::shared_ptr<Decoder_BPSK> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of ITpp::Decoder_BPSK.
       *
       * To avoid accidental use of raw pointers, ITpp::Decoder_BPSK's
       * constructor is in a private implementation
       * class. ITpp::Decoder_BPSK::make is the public interface for
       * creating new instances.
       */
      static sptr make(int m);
    };

  } // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_DECODER_BPSK_H */
