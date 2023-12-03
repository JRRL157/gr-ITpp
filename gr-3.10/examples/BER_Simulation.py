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
from gnuradio.filter import firdes
import sip
from gnuradio import ITpp
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from math import log10
import numpy as np



from gnuradio import qtgui

class BER_Simulation(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "BER_Simulation")

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
        self.N = N = 7
        self.K = K = 4
        self.samp_rate = samp_rate = 3200000
        self.m = m = N-K

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(0, 3)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(True)


        labels = ['Soft Decoding', 'Hard Decoding', 'Uncoded - Theory', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [3, 3, 3, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 1, 0, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Sinal de ruído', 'Eb/N0(dB)', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_uchar_to_float_1 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_int_to_float_0_0_0 = blocks.int_to_float(1, 1)
        self.blocks_int_to_float_0_0 = blocks.int_to_float(1, 1)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 0.5)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0_1_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_1 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(-1)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 2, 10000000))), True)
        self.analog_const_source_x_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, -1)
        self.analog_const_source_x_0_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0.01)
        self.analog_const_source_x_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 7)
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0_0 = analog.sig_source_i(0, analog.GR_CONST_WAVE, 0, 0, 4)
        self.analog_const_source_x_0 = analog.sig_source_i(0, analog.GR_CONST_WAVE, 0, 0, 7)
        self.ITpp_NoiseGenerator_0 = ITpp.NoiseGenerator()
        self.ITpp_Hamming_Soft_Decoder_0 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Encoder_0 = ITpp.Hamming_Encoder(m)
        self.ITpp_Hamming_Decoder_0 = ITpp.Hamming_Decoder(m)
        self.ITpp_BER_Analyzer_cpp_0 = ITpp.BER_Analyzer_cpp()


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ITpp_BER_Analyzer_cpp_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.ITpp_BER_Analyzer_cpp_0, 1), (self.blocks_int_to_float_0_0, 0))
        self.connect((self.ITpp_BER_Analyzer_cpp_0, 2), (self.blocks_int_to_float_0_0_0, 0))
        self.connect((self.ITpp_Hamming_Decoder_0, 0), (self.blocks_uchar_to_float_0_0, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.ITpp_NoiseGenerator_0, 1), (self.ITpp_BER_Analyzer_cpp_0, 0))
        self.connect((self.ITpp_NoiseGenerator_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.ITpp_NoiseGenerator_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.ITpp_NoiseGenerator_0, 1), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.analog_const_source_x_0, 0), (self.ITpp_NoiseGenerator_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.ITpp_NoiseGenerator_0, 1))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.ITpp_NoiseGenerator_0, 2))
        self.connect((self.analog_const_source_x_0_0_0_0, 0), (self.ITpp_NoiseGenerator_0, 3))
        self.connect((self.analog_const_source_x_0_0_0_0_0, 0), (self.ITpp_NoiseGenerator_0, 4))
        self.connect((self.analog_const_source_x_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_const_source_x_1, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_add_xx_0_1, 0), (self.ITpp_BER_Analyzer_cpp_0, 1))
        self.connect((self.blocks_add_xx_0_1_0, 0), (self.ITpp_BER_Analyzer_cpp_0, 2))
        self.connect((self.blocks_add_xx_1, 0), (self.ITpp_Hamming_Soft_Decoder_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.blocks_int_to_float_0_0, 0), (self.qtgui_time_sink_x_1_0, 1))
        self.connect((self.blocks_int_to_float_0_0_0, 0), (self.qtgui_time_sink_x_1_0, 2))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0_1, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0_1_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.ITpp_Hamming_Encoder_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_uchar_to_float_1, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_uchar_to_float_1, 0), (self.blocks_add_xx_0_1, 0))
        self.connect((self.blocks_uchar_to_float_1, 0), (self.blocks_add_xx_0_1_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.ITpp_Hamming_Decoder_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "BER_Simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_m(self.N-self.K)

    def get_K(self):
        return self.K

    def set_K(self, K):
        self.K = K
        self.set_m(self.N-self.K)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)

    def get_m(self):
        return self.m

    def set_m(self, m):
        self.m = m




def main(top_block_cls=BER_Simulation, options=None):

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
