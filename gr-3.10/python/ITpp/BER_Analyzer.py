import gnuradio.grc.core.blocks
import numpy as np
import matplotlib.pyplot as plt
import traceback

from time import sleep

from gnuradio import blocks
from gnuradio import analog
from gnuradio import gr


class BER_Analyzer(gr.basic_block):
    """
    docstring for block BER_Analyzer
    """

    def __init__(self):
        gr.basic_block.__init__(self, name="BER_Analyzer",
                                in_sig=[np.float32, np.byte, np.byte, np.byte],
                                out_sig=[np.float32, np.float32, np.float32])
        self._errorCnt1 = 0
        self._errorCnt0 = 0
        self._samplesCnt = 0

    def forecast(self, noutput_items, ninputs):
        ninput_items_required = [noutput_items] * ninputs
        return ninput_items_required

    def general_work(self, input_items, output_items):
        ninput_items = min([len(items) for items in input_items])
        #noutput_items = min(ninput_items, min([len(items) for items in output_items]))
        noutput_items = 3

        Eb_N0_dB: np.float32 = input_items[0][0]

        message = input_items[1]
        decoded0 = input_items[2]
        decoded1 = input_items[3]

        #sleep(1)
        try:
            Lmin = min(len(message),len(decoded0),len(decoded1))
            error0 = (message[:Lmin] - decoded0[:Lmin]) % 2
            error1 = (message[:Lmin] - decoded1[:Lmin]) % 2
            samplesCnt = Lmin
            errorCnt0 = np.count_nonzero(error1)
            errorCnt1 = np.count_nonzero(error0)

            self._samplesCnt += samplesCnt
            self._errorCnt0 += errorCnt0
            self._errorCnt1 += errorCnt1

            output_items[0][:] = 254
            output_items[1][:] = self._errorCnt0
            output_items[2][:] = self._errorCnt0

            #print(output_items[0])
            #print(output_items[1])
            #print(output_items[2])
        except Exception as e:
            #print(e)
            #traceback.print_exc()
            None

        output_items[0][:noutput_items] = 254
        output_items[1][:noutput_items] = self._errorCnt0
        output_items[2][:noutput_items] = self._errorCnt1

        self.consume_each(noutput_items)
        return noutput_items
