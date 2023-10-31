#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 gr-ITpp author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from math import log10
from gnuradio import gr

class NoiseGenerator(gr.basic_block):
    """
    docstring for block NoiseGenerator
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="NoiseGenerator",
            in_sig=[np.int32, np.int32, np.float32, np.float32, np.float32],
            out_sig=[np.float32, np.float32])
        
        self._current_eb_n0_db = 0
        self._amp = 0

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
        noutput_items = 0

        N = input_items[0][0]
        K = input_items[1][0]

        min_eb = input_items[2][0]
        max_eb = input_items[3][0]
        step_eb = input_items[4][0]

        output_arr0 = np.zeros(0)
        output_arr1 = np.zeros(0)

        if self._current_eb_n0_db > max_eb:
            self._current_eb_n0_db = min_eb

        if self._current_eb_n0_db < min_eb: self._current_eb_n0_db = min_eb

        ec_n0_db = self._current_eb_n0_db - 10.0 * log10(N / K)

        self._amp = (1.0/np.sqrt(2.0)) * 10.0 ** (-(ec_n0_db / 20.0))
        output_arr0 = np.append(output_arr0, self._amp)
        output_arr1 = np.append(output_arr1, self._current_eb_n0_db)

        self._current_eb_n0_db += step_eb

        noutput_items = min(len(output_items[0]), len(output_items[1]))
        noise = np.random.normal(scale=output_arr0[:noutput_items], size=noutput_items)

        output_items[0][:noutput_items] = noise.copy()[:noutput_items]
        output_items[1][:noutput_items] = output_arr1.copy()[:noutput_items]
        
        
        self.consume_each(noutput_items)
        return noutput_items

