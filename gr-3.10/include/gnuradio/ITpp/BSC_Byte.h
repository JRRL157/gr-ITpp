/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_ITPP_BSC_BYTE_H
#define INCLUDED_ITPP_BSC_BYTE_H

#include <gnuradio/ITpp/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
namespace ITpp {

/*!
 * \brief <+description of block+>
 * \ingroup ITpp
 *
 */
class ITPP_API BSC_Byte : virtual public gr::sync_block {
public:
  typedef std::shared_ptr<BSC_Byte> sptr;

  /*!
   * \brief Return a shared_ptr to a new instance of ITpp::BSC_Byte.
   *
   * To avoid accidental use of raw pointers, ITpp::BSC_Byte's
   * constructor is in a private implementation
   * class. ITpp::BSC_Byte::make is the public interface for
   * creating new instances.
   */
  static sptr make(int bits, float probability);
};

} // namespace ITpp
} // namespace gr

#endif /* INCLUDED_ITPP_BSC_BYTE_H */
