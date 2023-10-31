#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 gr-ITpp author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr

class Hard_Receiver(gr.basic_block):
    """
    docstring for block Hard_Receiver
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="Hard_Receiver",
            in_sig=[np.float32],
            out_sig=[np.byte ])

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

        input = input_items[0]
        r = input > 0

        output_items[0][:noutput_items] = r[:noutput_items]
        self.consume_each(noutput_items)
        return noutput_items

