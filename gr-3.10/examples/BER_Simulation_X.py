#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
import numpy
from gnuradio import ITpp
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from math import log10
import numpy as np



from gnuradio import qtgui

class BER_Simulation_X(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "BER_Simulation_X")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.ebn0_db = ebn0_db = numpy.arange(0, 10, 1)
        self.N = N = 7
        self.K = K = 4
        self.samp_rate = samp_rate = 3200000
        self.esno = esno = ebn0_db - 10*log10(N/K)
        self.num_curves = num_curves = 1
        self.m = m = N-K
        self.amp = amp = (1.0/numpy.sqrt(2.0)) * 10.0 ** (-esno/ 20.0)
        self.B = B = samp_rate/2

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_bercurve_sink_0_0 = qtgui.ber_sink_b(
            esno, #range of esnos
            num_curves, #number of curves
            100, #ensure at least
            -7.0, #cutoff
            [], #indiv. curve names
            None # parent
        )
        self.qtgui_bercurve_sink_0_0.set_update_time(0.10)
        self.qtgui_bercurve_sink_0_0.set_y_axis(-10, 0)
        self.qtgui_bercurve_sink_0_0.set_x_axis(esno[0], esno[-1])

        labels = ['Soft Decoding', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]

        for i in range(num_curves):
            if len(labels[i]) == 0:
                self.qtgui_bercurve_sink_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_bercurve_sink_0_0.set_line_label(i, labels[i])
            self.qtgui_bercurve_sink_0_0.set_line_width(i, widths[i])
            self.qtgui_bercurve_sink_0_0.set_line_color(i, colors[i])
            self.qtgui_bercurve_sink_0_0.set_line_style(i, styles[i])
            self.qtgui_bercurve_sink_0_0.set_line_marker(i, markers[i])
            self.qtgui_bercurve_sink_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_bercurve_sink_0_0_win = sip.wrapinstance(self.qtgui_bercurve_sink_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_bercurve_sink_0_0_win)
        self.qtgui_bercurve_sink_0 = qtgui.ber_sink_b(
            esno, #range of esnos
            num_curves, #number of curves
            100, #ensure at least
            -7.0, #cutoff
            [], #indiv. curve names
            None # parent
        )
        self.qtgui_bercurve_sink_0.set_update_time(0.10)
        self.qtgui_bercurve_sink_0.set_y_axis(-10, 0)
        self.qtgui_bercurve_sink_0.set_x_axis(esno[0], esno[-1])

        labels = ['Hard Decoding', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]

        for i in range(num_curves):
            if len(labels[i]) == 0:
                self.qtgui_bercurve_sink_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_bercurve_sink_0.set_line_label(i, labels[i])
            self.qtgui_bercurve_sink_0.set_line_width(i, widths[i])
            self.qtgui_bercurve_sink_0.set_line_color(i, colors[i])
            self.qtgui_bercurve_sink_0.set_line_style(i, styles[i])
            self.qtgui_bercurve_sink_0.set_line_marker(i, markers[i])
            self.qtgui_bercurve_sink_0.set_line_alpha(i, alphas[i])

        self._qtgui_bercurve_sink_0_win = sip.wrapinstance(self.qtgui_bercurve_sink_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_bercurve_sink_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_char_to_float_0_0_1_5 = blocks.char_to_float(1, 0.5)
        self.blocks_char_to_float_0_0_1_4 = blocks.char_to_float(1, 0.5)
        self.blocks_char_to_float_0_0_1_3 = blocks.char_to_float(1, 0.5)
        self.blocks_char_to_float_0_0_1_2 = blocks.char_to_float(1, 0.5)
        self.blocks_char_to_float_0_0_1_1 = blocks.char_to_float(1, 0.5)
        self.blocks_char_to_float_0_0_1_0 = blocks.char_to_float(1, 0.5)
        self.blocks_char_to_float_0_0_1 = blocks.char_to_float(1, 0.5)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 0.5)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 0.5)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 0.5)
        self.blocks_add_xx_1_0_1_5 = blocks.add_vff(1)
        self.blocks_add_xx_1_0_1_4 = blocks.add_vff(1)
        self.blocks_add_xx_1_0_1_3 = blocks.add_vff(1)
        self.blocks_add_xx_1_0_1_2 = blocks.add_vff(1)
        self.blocks_add_xx_1_0_1_1 = blocks.add_vff(1)
        self.blocks_add_xx_1_0_1_0 = blocks.add_vff(1)
        self.blocks_add_xx_1_0_1 = blocks.add_vff(1)
        self.blocks_add_xx_1_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_1_0 = blocks.add_vff(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0_0_1_5 = blocks.add_const_ff(-1)
        self.blocks_add_const_vxx_0_0_1_4 = blocks.add_const_ff(-1)
        self.blocks_add_const_vxx_0_0_1_3 = blocks.add_const_ff(-1)
        self.blocks_add_const_vxx_0_0_1_2 = blocks.add_const_ff(-1)
        self.blocks_add_const_vxx_0_0_1_1 = blocks.add_const_ff(-1)
        self.blocks_add_const_vxx_0_0_1_0 = blocks.add_const_ff(-1)
        self.blocks_add_const_vxx_0_0_1 = blocks.add_const_ff(-1)
        self.blocks_add_const_vxx_0_0_0 = blocks.add_const_ff(-1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_ff(-1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(-1)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 2, 10000000))), True)
        self.analog_noise_source_x_0_0_1_5 = analog.noise_source_f(analog.GR_GAUSSIAN, amp[9], 0)
        self.analog_noise_source_x_0_0_1_4 = analog.noise_source_f(analog.GR_GAUSSIAN, amp[8], 0)
        self.analog_noise_source_x_0_0_1_3 = analog.noise_source_f(analog.GR_GAUSSIAN, amp[7], 0)
        self.analog_noise_source_x_0_0_1_2 = analog.noise_source_f(analog.GR_GAUSSIAN, amp[6], 0)
        self.analog_noise_source_x_0_0_1_1 = analog.noise_source_f(analog.GR_GAUSSIAN, amp[5], 0)
        self.analog_noise_source_x_0_0_1_0 = analog.noise_source_f(analog.GR_GAUSSIAN, amp[4], 0)
        self.analog_noise_source_x_0_0_1 = analog.noise_source_f(analog.GR_GAUSSIAN, amp[3], 0)
        self.analog_noise_source_x_0_0_0 = analog.noise_source_f(analog.GR_GAUSSIAN, amp[2], 0)
        self.analog_noise_source_x_0_0 = analog.noise_source_f(analog.GR_GAUSSIAN, amp[1], 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, amp[0], 0)
        self.ITpp_Hard_Receiver_0_0_1_5 = ITpp.Hard_Receiver()
        self.ITpp_Hard_Receiver_0_0_1_4 = ITpp.Hard_Receiver()
        self.ITpp_Hard_Receiver_0_0_1_3 = ITpp.Hard_Receiver()
        self.ITpp_Hard_Receiver_0_0_1_2 = ITpp.Hard_Receiver()
        self.ITpp_Hard_Receiver_0_0_1_1 = ITpp.Hard_Receiver()
        self.ITpp_Hard_Receiver_0_0_1_0 = ITpp.Hard_Receiver()
        self.ITpp_Hard_Receiver_0_0_1 = ITpp.Hard_Receiver()
        self.ITpp_Hard_Receiver_0_0_0 = ITpp.Hard_Receiver()
        self.ITpp_Hard_Receiver_0_0 = ITpp.Hard_Receiver()
        self.ITpp_Hard_Receiver_0 = ITpp.Hard_Receiver()
        self.ITpp_Hamming_Soft_Decoder_0_0_1_5 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Soft_Decoder_0_0_1_4 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Soft_Decoder_0_0_1_3 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Soft_Decoder_0_0_1_2 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Soft_Decoder_0_0_1_1 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Soft_Decoder_0_0_1_0 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Soft_Decoder_0_0_1 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Soft_Decoder_0_0_0 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Soft_Decoder_0_0 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Soft_Decoder_0 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Encoder_0 = ITpp.Hamming_Encoder(m)
        self.ITpp_Hamming_Decoder_0_0_1_5 = ITpp.Hamming_Decoder(m)
        self.ITpp_Hamming_Decoder_0_0_1_4 = ITpp.Hamming_Decoder(m)
        self.ITpp_Hamming_Decoder_0_0_1_3 = ITpp.Hamming_Decoder(m)
        self.ITpp_Hamming_Decoder_0_0_1_2 = ITpp.Hamming_Decoder(m)
        self.ITpp_Hamming_Decoder_0_0_1_1 = ITpp.Hamming_Decoder(m)
        self.ITpp_Hamming_Decoder_0_0_1_0 = ITpp.Hamming_Decoder(m)
        self.ITpp_Hamming_Decoder_0_0_1 = ITpp.Hamming_Decoder(m)
        self.ITpp_Hamming_Decoder_0_0_0 = ITpp.Hamming_Decoder(m)
        self.ITpp_Hamming_Decoder_0_0 = ITpp.Hamming_Decoder(m)
        self.ITpp_Hamming_Decoder_0 = ITpp.Hamming_Decoder(m)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ITpp_Hamming_Decoder_0, 0), (self.qtgui_bercurve_sink_0, 1))
        self.connect((self.ITpp_Hamming_Decoder_0_0, 0), (self.qtgui_bercurve_sink_0, 3))
        self.connect((self.ITpp_Hamming_Decoder_0_0_0, 0), (self.qtgui_bercurve_sink_0, 5))
        self.connect((self.ITpp_Hamming_Decoder_0_0_1, 0), (self.qtgui_bercurve_sink_0, 7))
        self.connect((self.ITpp_Hamming_Decoder_0_0_1_0, 0), (self.qtgui_bercurve_sink_0, 9))
        self.connect((self.ITpp_Hamming_Decoder_0_0_1_1, 0), (self.qtgui_bercurve_sink_0, 11))
        self.connect((self.ITpp_Hamming_Decoder_0_0_1_2, 0), (self.qtgui_bercurve_sink_0, 13))
        self.connect((self.ITpp_Hamming_Decoder_0_0_1_3, 0), (self.qtgui_bercurve_sink_0, 15))
        self.connect((self.ITpp_Hamming_Decoder_0_0_1_4, 0), (self.qtgui_bercurve_sink_0, 17))
        self.connect((self.ITpp_Hamming_Decoder_0_0_1_5, 0), (self.qtgui_bercurve_sink_0, 19))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0_0_1, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0_0_1_0, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0_0_1_1, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0_0_1_2, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0_0_1_3, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0_0_1_4, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0_0_1_5, 0))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0, 0), (self.qtgui_bercurve_sink_0_0, 1))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0_0, 0), (self.qtgui_bercurve_sink_0_0, 3))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0_0_0, 0), (self.qtgui_bercurve_sink_0_0, 5))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0_0_1, 0), (self.qtgui_bercurve_sink_0_0, 7))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0_0_1_0, 0), (self.qtgui_bercurve_sink_0_0, 9))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0_0_1_1, 0), (self.qtgui_bercurve_sink_0_0, 11))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0_0_1_2, 0), (self.qtgui_bercurve_sink_0_0, 13))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0_0_1_3, 0), (self.qtgui_bercurve_sink_0_0, 15))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0_0_1_4, 0), (self.qtgui_bercurve_sink_0_0, 17))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0_0_1_5, 0), (self.qtgui_bercurve_sink_0_0, 19))
        self.connect((self.ITpp_Hard_Receiver_0, 0), (self.ITpp_Hamming_Decoder_0, 0))
        self.connect((self.ITpp_Hard_Receiver_0_0, 0), (self.ITpp_Hamming_Decoder_0_0, 0))
        self.connect((self.ITpp_Hard_Receiver_0_0_0, 0), (self.ITpp_Hamming_Decoder_0_0_0, 0))
        self.connect((self.ITpp_Hard_Receiver_0_0_1, 0), (self.ITpp_Hamming_Decoder_0_0_1, 0))
        self.connect((self.ITpp_Hard_Receiver_0_0_1_0, 0), (self.ITpp_Hamming_Decoder_0_0_1_0, 0))
        self.connect((self.ITpp_Hard_Receiver_0_0_1_1, 0), (self.ITpp_Hamming_Decoder_0_0_1_1, 0))
        self.connect((self.ITpp_Hard_Receiver_0_0_1_2, 0), (self.ITpp_Hamming_Decoder_0_0_1_2, 0))
        self.connect((self.ITpp_Hard_Receiver_0_0_1_3, 0), (self.ITpp_Hamming_Decoder_0_0_1_3, 0))
        self.connect((self.ITpp_Hard_Receiver_0_0_1_4, 0), (self.ITpp_Hamming_Decoder_0_0_1_4, 0))
        self.connect((self.ITpp_Hard_Receiver_0_0_1_5, 0), (self.ITpp_Hamming_Decoder_0_0_1_5, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_add_xx_1_0, 0))
        self.connect((self.analog_noise_source_x_0_0_0, 0), (self.blocks_add_xx_1_0_0, 0))
        self.connect((self.analog_noise_source_x_0_0_1, 0), (self.blocks_add_xx_1_0_1, 0))
        self.connect((self.analog_noise_source_x_0_0_1_0, 0), (self.blocks_add_xx_1_0_1_0, 0))
        self.connect((self.analog_noise_source_x_0_0_1_1, 0), (self.blocks_add_xx_1_0_1_1, 0))
        self.connect((self.analog_noise_source_x_0_0_1_2, 0), (self.blocks_add_xx_1_0_1_2, 0))
        self.connect((self.analog_noise_source_x_0_0_1_3, 0), (self.blocks_add_xx_1_0_1_3, 0))
        self.connect((self.analog_noise_source_x_0_0_1_4, 0), (self.blocks_add_xx_1_0_1_4, 0))
        self.connect((self.analog_noise_source_x_0_0_1_5, 0), (self.blocks_add_xx_1_0_1_5, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_add_xx_1_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_0, 0), (self.blocks_add_xx_1_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1, 0), (self.blocks_add_xx_1_0_1, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0, 0), (self.blocks_add_xx_1_0_1_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_1, 0), (self.blocks_add_xx_1_0_1_1, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_2, 0), (self.blocks_add_xx_1_0_1_2, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_3, 0), (self.blocks_add_xx_1_0_1_3, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_4, 0), (self.blocks_add_xx_1_0_1_4, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_5, 0), (self.blocks_add_xx_1_0_1_5, 1))
        self.connect((self.blocks_add_xx_1, 0), (self.ITpp_Hamming_Soft_Decoder_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.ITpp_Hard_Receiver_0, 0))
        self.connect((self.blocks_add_xx_1_0, 0), (self.ITpp_Hamming_Soft_Decoder_0_0, 0))
        self.connect((self.blocks_add_xx_1_0, 0), (self.ITpp_Hard_Receiver_0_0, 0))
        self.connect((self.blocks_add_xx_1_0_0, 0), (self.ITpp_Hamming_Soft_Decoder_0_0_0, 0))
        self.connect((self.blocks_add_xx_1_0_0, 0), (self.ITpp_Hard_Receiver_0_0_0, 0))
        self.connect((self.blocks_add_xx_1_0_1, 0), (self.ITpp_Hamming_Soft_Decoder_0_0_1, 0))
        self.connect((self.blocks_add_xx_1_0_1, 0), (self.ITpp_Hard_Receiver_0_0_1, 0))
        self.connect((self.blocks_add_xx_1_0_1_0, 0), (self.ITpp_Hamming_Soft_Decoder_0_0_1_0, 0))
        self.connect((self.blocks_add_xx_1_0_1_0, 0), (self.ITpp_Hard_Receiver_0_0_1_0, 0))
        self.connect((self.blocks_add_xx_1_0_1_1, 0), (self.ITpp_Hamming_Soft_Decoder_0_0_1_1, 0))
        self.connect((self.blocks_add_xx_1_0_1_1, 0), (self.ITpp_Hard_Receiver_0_0_1_1, 0))
        self.connect((self.blocks_add_xx_1_0_1_2, 0), (self.ITpp_Hamming_Soft_Decoder_0_0_1_2, 0))
        self.connect((self.blocks_add_xx_1_0_1_2, 0), (self.ITpp_Hard_Receiver_0_0_1_2, 0))
        self.connect((self.blocks_add_xx_1_0_1_3, 0), (self.ITpp_Hamming_Soft_Decoder_0_0_1_3, 0))
        self.connect((self.blocks_add_xx_1_0_1_3, 0), (self.ITpp_Hard_Receiver_0_0_1_3, 0))
        self.connect((self.blocks_add_xx_1_0_1_4, 0), (self.ITpp_Hamming_Soft_Decoder_0_0_1_4, 0))
        self.connect((self.blocks_add_xx_1_0_1_4, 0), (self.ITpp_Hard_Receiver_0_0_1_4, 0))
        self.connect((self.blocks_add_xx_1_0_1_5, 0), (self.ITpp_Hamming_Soft_Decoder_0_0_1_5, 0))
        self.connect((self.blocks_add_xx_1_0_1_5, 0), (self.ITpp_Hard_Receiver_0_0_1_5, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.blocks_add_const_vxx_0_0_0, 0))
        self.connect((self.blocks_char_to_float_0_0_1, 0), (self.blocks_add_const_vxx_0_0_1, 0))
        self.connect((self.blocks_char_to_float_0_0_1_0, 0), (self.blocks_add_const_vxx_0_0_1_0, 0))
        self.connect((self.blocks_char_to_float_0_0_1_1, 0), (self.blocks_add_const_vxx_0_0_1_1, 0))
        self.connect((self.blocks_char_to_float_0_0_1_2, 0), (self.blocks_add_const_vxx_0_0_1_2, 0))
        self.connect((self.blocks_char_to_float_0_0_1_3, 0), (self.blocks_add_const_vxx_0_0_1_3, 0))
        self.connect((self.blocks_char_to_float_0_0_1_4, 0), (self.blocks_add_const_vxx_0_0_1_4, 0))
        self.connect((self.blocks_char_to_float_0_0_1_5, 0), (self.blocks_add_const_vxx_0_0_1_5, 0))
        self.connect((self.blocks_throttle_0, 0), (self.ITpp_Hamming_Encoder_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0, 6))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0, 2))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0, 8))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0, 18))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0, 10))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0, 14))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0, 12))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0, 16))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0, 4))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0_0, 8))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0_0, 10))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0_0, 6))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0_0, 12))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0_0, 16))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0_0, 2))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0_0, 18))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0_0, 4))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_bercurve_sink_0_0, 14))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "BER_Simulation_X")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_ebn0_db(self):
        return self.ebn0_db

    def set_ebn0_db(self, ebn0_db):
        self.ebn0_db = ebn0_db
        self.set_esno(self.ebn0_db - 10*log10(self.N/self.K))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_esno(self.ebn0_db - 10*log10(self.N/self.K))
        self.set_m(self.N-self.K)

    def get_K(self):
        return self.K

    def set_K(self, K):
        self.K = K
        self.set_esno(self.ebn0_db - 10*log10(self.N/self.K))
        self.set_m(self.N-self.K)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_B(self.samp_rate/2)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_esno(self):
        return self.esno

    def set_esno(self, esno):
        self.esno = esno
        self.set_amp((1.0/numpy.sqrt(2.0)) * 10.0 ** (-self.esno/ 20.0))

    def get_num_curves(self):
        return self.num_curves

    def set_num_curves(self, num_curves):
        self.num_curves = num_curves

    def get_m(self):
        return self.m

    def set_m(self, m):
        self.m = m

    def get_amp(self):
        return self.amp

    def set_amp(self, amp):
        self.amp = amp
        self.analog_noise_source_x_0.set_amplitude(self.amp[0])
        self.analog_noise_source_x_0_0.set_amplitude(self.amp[1])
        self.analog_noise_source_x_0_0_0.set_amplitude(self.amp[2])
        self.analog_noise_source_x_0_0_1.set_amplitude(self.amp[3])
        self.analog_noise_source_x_0_0_1_0.set_amplitude(self.amp[4])
        self.analog_noise_source_x_0_0_1_1.set_amplitude(self.amp[5])
        self.analog_noise_source_x_0_0_1_2.set_amplitude(self.amp[6])
        self.analog_noise_source_x_0_0_1_3.set_amplitude(self.amp[7])
        self.analog_noise_source_x_0_0_1_4.set_amplitude(self.amp[8])
        self.analog_noise_source_x_0_0_1_5.set_amplitude(self.amp[9])

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B




def main(top_block_cls=BER_Simulation_X, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
