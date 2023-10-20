#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 JRRL.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from time import sleep
from gnuradio import gr

class BER_Analyzer(gr.basic_block):
    """
    docstring for block BER_Analyzer
    """
    def __init__(self, Eb_N0_dB=10):
        gr.basic_block.__init__(self,name="BER_Analyzer",in_sig=[np.int32,np.int32,np.int32,np.byte,np.byte,np.byte],
            out_sig=[np.byte])
        self.Eb_N0_dB = Eb_N0_dB

    def forecast(self, noutput_items, ninputs):
        # ninputs is the number of input connections
        # setup size of input_items[i] for work call
        # the required number of input items is returned
        #   in a list where each element represents the
        #   number of required items for each input
        ninput_items_required = [noutput_items] * ninputs
        return ninput_items_required

    def general_work(self, input_items, output_items):
        # For this sample code, the general block is made to behave like a sync block
        ninput_items = min([len(items) for items in input_items])
        noutput_items = min(len(output_items[0]), ninput_items)
        
        in3 = input_items[3]
        in4 = input_items[4]
        in5 = input_items[5]
        sleep(1)
        sum = in3+in4+in5;
        sum = sum % 2
        print(sum,len(sum))
        try:
            #np.random.seed(7)
            output_items[0][:] = 0xFF
            print(type(output_items)[0][:])
        except:
            None
        
        #self.consume_each(noutput_items)
        return noutput_items

