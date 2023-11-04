/* -*- c++ -*- */
/*
 * Copyright 2023 gr-ITpp author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include <gnuradio/io_signature.h>
#include "BER_Analyzer_cpp_impl.h"
#include <cmath>

namespace gr {
  namespace ITpp {
    using input_type = float;
    using output_type = int32_t;
    BER_Analyzer_cpp::sptr
    BER_Analyzer_cpp::make()
    {
      return gnuradio::make_block_sptr<BER_Analyzer_cpp_impl>(
        );
    }


    /*
     * The private constructor
     */
    BER_Analyzer_cpp_impl::BER_Analyzer_cpp_impl()
      : gr::block("BER_Analyzer_cpp",
              gr::io_signature::make(3 /* min inputs */, 3 /* max inputs */, sizeof(input_type)),
              gr::io_signature::make(3 /* min outputs */, 3 /*max outputs */, sizeof(output_type)))
    {
      this->records = std::map<float,int[3]>();
    }

    /*
     * Our virtual destructor.
     */
    BER_Analyzer_cpp_impl::~BER_Analyzer_cpp_impl()
    {
    }

    void
    BER_Analyzer_cpp_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = noutput_items;
    }

    int
    BER_Analyzer_cpp_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {      
      auto in0 = static_cast<const input_type*>(input_items[0]);
      auto in1 = static_cast<const input_type*>(input_items[1]);
      auto in2 = static_cast<const input_type*>(input_items[2]);
      
      auto out0 = static_cast<output_type*>(output_items[0]);
      auto out1 = static_cast<output_type*>(output_items[1]);
      auto out2 = static_cast<output_type*>(output_items[2]);

      auto Eb_N0 = in0[0];

      int in1_cnt = 0;
      int in2_cnt = 0;

      // Calculate all the errors
      for(int index = 0; index < noutput_items; index++){        
        in1_cnt += in1[index] != 0;        
        in2_cnt += in2[index] != 0;
      }

      
      // Feed the records map
      auto it = records.find(Eb_N0);      
      if(it != records.end()){
        int triplet[3] = {records.at(Eb_N0)[0],records.at(Eb_N0)[1],records.at(Eb_N0)[2]};
        const int ntriplet[3] = {triplet[0]+noutput_items,triplet[1]+in1_cnt,triplet[2]+in2_cnt};
        records[Eb_N0][0] = ntriplet[0];
        records[Eb_N0][1] = ntriplet[1];
        records[Eb_N0][2] = ntriplet[2];
      }else{
        int triplet[3] = {noutput_items,in1_cnt,in2_cnt};
        records[Eb_N0][0] = triplet[0];
        records[Eb_N0][1] = triplet[1];
        records[Eb_N0][2] = triplet[2];
      }

      // (Optional) Iterate through the map in sorted order and print it out to the console
      for (const auto& pair : records) {
          float Eb_N0_db = pair.first;
          int value[3] = {pair.second[0],pair.second[1],pair.second[2]};
          int numSamples = value[0];
          int numError1 = value[1];
          int numError2 = value[2];
          double theoreticalError = (0.5*std::erfc(std::sqrt(std::pow(10.0,Eb_N0_db/10.0))));
          //printf("Eb_N0 = %.2f\t#Samples = %d\t\tTheoreticalError = %f\t\tError1 = %d/%d\t\tError2 = %d/%d\n",Eb_N0_db,numSamples,theoreticalError,numError1,numSamples,numError2,numSamples);
      }

      //Gather all the information to plot the graph through GNURadio
      int records_size = records.size();
      auto records_it = records.begin();

      for(int i = 0;i<noutput_items;i++){
        const auto& pair = *records_it;
        int value[3] = {pair.second[0],pair.second[1],pair.second[2]};

        float Eb_N0_db = pair.first;
        int numSamples = value[0];
        double numError1 = value[1] == 0 ? 1 : value[1];
        double numError2 = value[2] == 0 ? 1 : value[2];
        double error1 = (numError1/numSamples);
        int error1e6 = 1000000*error1;
        double log10error1 = log10(error1);
        double error2 = (numError2/numSamples);
        int error2e6 = 1000000*error2;
        double log10error2 = log10(error2);
        double theoreticalError = (0.5*std::erfc(std::sqrt(std::pow(10.0,Eb_N0_db/10.0))));
        int theoreticalError1e6 = 1000000*theoreticalError;
        double log10theory = log10(theoreticalError);
        
        out0[i] = 1000*log10error1;
        out1[i] = 1000*log10error2;
        out2[i] = 1000*log10theory;
        ++records_it;

        if(records_it == records.end())
          records_it = records.begin();
      }
            
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace ITpp */
} /* namespace gr */