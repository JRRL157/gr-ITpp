/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include <gnuradio/io_signature.h>
#include "Decoder_BPSK_impl.h"

#include <itpp/itbase.h>
#include <itpp/comm/hammcode.h>

namespace gr {
  namespace ITpp {

    using input_type = unsigned char;
    using output_type = unsigned char;
    Decoder_BPSK::sptr Decoder_BPSK::make(int m){
      return gnuradio::make_block_sptr<Decoder_BPSK_impl>(m);
    }


    /*
     * The private constructor
     */
    Decoder_BPSK_impl::Decoder_BPSK_impl(int m)
      : gr::block("Decoder_BPSK",
              gr::io_signature::make(1 /* min inputs */, 1 /* max inputs */, sizeof(input_type)),
              gr::io_signature::make(1 /* min outputs */, 1 /*max outputs */, sizeof(output_type)))
    {
      d_m = m;

      itpp::Hamming_Code block(d_m);
      d_K = block.get_k();
      d_N = block.get_n();

      set_output_multiple(d_K);
    }

    /*
     * Our virtual destructor.
     */
    Decoder_BPSK_impl::~Decoder_BPSK_impl()
    {
    }

    void
    Decoder_BPSK_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = (int)(noutput_items * ((float)d_N)/((float)d_K));
    }

    int
    Decoder_BPSK_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        auto in = static_cast<const input_type *>(input_items[0]);
        auto out = static_cast<output_type *>(output_items[0]);

        itpp::bvec decoded, encoded;
        encoded.set_length(d_N);
        encoded.zeros();
        decoded.set_length(d_K);
        decoded.zeros();
        itpp::Hamming_Code block(d_m);

        for(int i = 0; i < noutput_items/d_K; i++){
          for(int j = 0; j < d_K; j++){
            out[d_K*i+j] = 0;
          }

          for(int j = 0; j < d_N; j++){
            encoded(j) = in[d_N*i+j];
          }
          for(int j = 0;j < d_K;j++){
            decoded(j) = (int)encoded.get(j);
          }

          decoded = block.decode(encoded);

          for(int j = 0; j < d_K; j++){
            out[d_K*i+j] = (int)decoded.get(j);
          }
        }
      consume(0, (int)(noutput_items * ((float)d_N)/((float)d_K)));

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace ITpp */
} /* namespace gr */
