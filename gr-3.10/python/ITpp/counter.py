#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 JRRL.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr
from time import sleep

class counter(gr.basic_block):
    """
    docstring for block counter
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="counter",
            in_sig=[np.byte, np.byte,np.byte],
            out_sig=[np.byte])
        self.iteration = 0

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
        ninput_items : np.int = min([len(items) for items in input_items])
        noutput_items : np.int = min(len(output_items[0]), ninput_items)

        #sleep(1)
        initial = input_items[0];
        step = input_items[1][0]
        n = input_items[2][0];
        
        try:
            output_items[0][:] = np.array([(x + self.iteration) % n for x in initial],dtype=np.byte)
            #print(output_items)
            #print(self.iteration)
        except Exception as e:
            output_items[0][:] = 0x00

        self.iteration += step
        self.consume_each(noutput_items)
        return noutput_items

