#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 JRRL.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr

class vector_source_adder(gr.basic_block):
    """
    docstring for block vector_source_adder
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="vector_source_adder",
            in_sig=[np.byte, np.byte],
            out_sig=[np.byte, ])

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
        ninput_items : np.int32 = min([len(items) for items in input_items])
        noutput_items : np.int32 = min(len(output_items[0]), ninput_items)

        print(ninput_items)
        print(noutput_items)

        in0 = input_items[0];
        in1 = input_items[1];
        
        try:
            sum = [x % 2 for x in (in0+in1)];
            print(int("".join(str(x) for x in sum), 2))
            output_items[0][:] = int("".join(str(x) for x in sum), 2)
        except Exception as e:
            output_items[0][:] = 0x00

        #output_items[0][:noutput_items] = input_items[0][:noutput_items]
        self.consume_each(noutput_items)
        return noutput_items

