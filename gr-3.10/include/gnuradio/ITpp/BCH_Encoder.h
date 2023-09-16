/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_BCH_ENCODER_H
#define INCLUDED_ITPP_BCH_ENCODER_H

#include <gnuradio/ITpp/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
namespace ITpp {

/*!
 * \brief <+description of block+>
 * \ingroup ITpp
 *
 */
class ITPP_API BCH_Encoder : virtual public gr::block {
public:
  typedef std::shared_ptr<BCH_Encoder> sptr;

  /*!
   * \brief Return a shared_ptr to a new instance of ITpp::BCH_Encoder.
   *
   * To avoid accidental use of raw pointers, ITpp::BCH_Encoder's
   * constructor is in a private implementation
   * class. ITpp::BCH_Encoder::make is the public interface for
   * creating new instances.
   */
  static sptr make(int n, int t);
};

} // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_BCH_ENCODER_H */
