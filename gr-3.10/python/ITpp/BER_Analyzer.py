import gnuradio.grc.core.blocks
import numpy as np
from time import sleep

from gnuradio import blocks
from gnuradio import analog
from gnuradio import gr
from gnuradio.ITpp.ITpp_python import Hamming_Soft_Decoder, Hamming_Decoder, Hamming_Encoder


class BER_Analyzer(gr.basic_block):
    """
    docstring for block BER_Analyzer
    """

    def __init__(self, Eb_N0_dB=10):
        gr.basic_block.__init__(self, name="BER_Analyzer",
                                in_sig=[np.int32, np.int32, np.int32, np.byte, np.byte, np.byte],
                                out_sig=[])
        self.Eb_N0_dB = Eb_N0_dB

    def forecast(self, noutput_items, ninputs):
        ninput_items_required = [noutput_items] * ninputs
        return ninput_items_required

    def general_work(self, input_items, output_items):
        ninput_items = min([len(items) for items in input_items])
        noutput_items = 1

        tb = gr.top_block()

        n: np.int32 = input_items[0][0]
        k: np.int32 = input_items[1][0]
        num_bits: np.int32 = input_items[2][0]

        m: np.int32 = n - k

        throttle_block = blocks.throttle(itemsize=1,samples_per_sec=320000)
        
        #ATENÇÃO AQUI!!!
        add_const_block = blocks.blocks_python.add_const_vff([1,1,1])
        
        float2uchar_block = blocks.float_to_uchar()
        uchar2float_block = blocks.uchar_to_float()
        adder_block = blocks.add_vff()
        noise_source_float_block = analog.noise_source_f(type=analog.noise_type_t.GR_GAUSSIAN, ampl=0.5, seed=-1)
        random_source_block = gr.random(seed=7, min_integer=0, max_integer=2)
        encoder_block = Hamming_Encoder(m)
        hard_decoder_block = Hamming_Decoder(m)
        soft_decoder_block = Hamming_Soft_Decoder(m)

        #tb.connect()

        tb.run()
        output_data1 = random_source_block.ran1().real

        print("CHEGOU AQUI!")
        in3 = input_items[3]
        in4 = input_items[4]
        in5 = input_items[5]
        sleep(1)
        try:
            print("in3 = ", in3)
            print("in4 = ", in4)
            print("in5 = ", in5)
            print("CHEGOU AQUI 2!")
        except Exception as e:
            print("OPA, pegou uma exceção!")
            print(e)

        print("CHEGOU AQUI 3")
        self.consume_each(noutput_items)
        return noutput_items
