#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 gr-ITpp author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from math import erfc,sqrt,pow,log10
from time import sleep
from gnuradio import gr

class Uncoded_BPKS(gr.basic_block):
    """
    docstring for block Uncoded_BPKS
    """
    def __init__(self, Eb_N0):
        gr.basic_block.__init__(self,
            name="Uncoded_BPKS",
            in_sig=[],
            out_sig=[numpy.float32, ])
        
        self.Eb_N0 = Eb_N0

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
        #ninput_items = min([len(items) for items in input_items])
        #noutput_items = min(len(output_items[0]), ninput_items)
        ninput_items = 0
        noutput_items = len(output_items[0])
        
        theoreticalError = log10(0.5*erfc(sqrt(pow(10.0,self.Eb_N0/10.0))))

        print(theoreticalError)
        sleep(0.05)

        output_items[0][:noutput_items] = noutput_items*[theoreticalError]
        self.consume_each(noutput_items)
        return noutput_items

