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
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import testing
from math import log10
import numpy as np



from gnuradio import qtgui

class BER_Simulation_2(gr.top_block, Qt.QWidget):

    def __init__(self, max_Eb_N0_dB=10, min_Eb_N0_dB=0, step_Eb_N0_dB=1):
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

        self.settings = Qt.QSettings("GNU Radio", "BER_Simulation_2")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.max_Eb_N0_dB = max_Eb_N0_dB
        self.min_Eb_N0_dB = min_Eb_N0_dB
        self.step_Eb_N0_dB = step_Eb_N0_dB

        ##################################################
        # Variables
        ##################################################
        self.N = N = 7
        self.K = K = 4
        self.step_Ec_N0_dB = step_Ec_N0_dB = step_Eb_N0_dB
        self.samp_rate = samp_rate = 3200000
        self.min_Ec_N0_dB = min_Ec_N0_dB = min_Eb_N0_dB - 10*log10(N/K)
        self.max_Ec_N0_dB = max_Ec_N0_dB = max_Eb_N0_dB - 10*log10(N/K)
        self.m = m = N-K

        ##################################################
        # Blocks
        ##################################################
        self.testing_NoiseConverter_0 = testing.NoiseConverter()
        self.testing_HardReceiver_0 = testing.HardReceiver()
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
            64, #size
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
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(True)


        labels = ['Soft Decoding', 'Hard Decoding', ' Message', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 3, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, 2, -1, -1,
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
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            16, #size
            samp_rate, #samp_rate
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Hard Decoding', 'Soft Decoding', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, 0, 1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
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
        self.blocks_uchar_to_float_0_1_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_1_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_1 = blocks.uchar_to_float()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 0.5)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(-1)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 2, 2000000))), True)
        self.analog_const_source_x_0_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0.1)
        self.analog_const_source_x_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 10)
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0_0 = analog.sig_source_i(0, analog.GR_CONST_WAVE, 0, 0, 4)
        self.analog_const_source_x_0 = analog.sig_source_i(0, analog.GR_CONST_WAVE, 0, 0, 7)
        self.ITpp_Hamming_Soft_Decoder_0 = ITpp.Hamming_Soft_Decoder(m)
        self.ITpp_Hamming_Encoder_0 = ITpp.Hamming_Encoder(m)
        self.ITpp_Hamming_Decoder_0 = ITpp.Hamming_Decoder(m)
        self.ITpp_BER_Analyzer_0 = ITpp.BER_Analyzer()


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ITpp_BER_Analyzer_0, 2), (self.qtgui_time_sink_x_1, 2))
        self.connect((self.ITpp_BER_Analyzer_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.ITpp_BER_Analyzer_0, 1), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.ITpp_Hamming_Decoder_0, 0), (self.ITpp_BER_Analyzer_0, 2))
        self.connect((self.ITpp_Hamming_Decoder_0, 0), (self.blocks_uchar_to_float_0_1_0, 0))
        self.connect((self.ITpp_Hamming_Encoder_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0, 0), (self.ITpp_BER_Analyzer_0, 3))
        self.connect((self.ITpp_Hamming_Soft_Decoder_0, 0), (self.blocks_uchar_to_float_0_1, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.testing_NoiseConverter_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.testing_NoiseConverter_0, 1))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.testing_NoiseConverter_0, 2))
        self.connect((self.analog_const_source_x_0_0_0_0, 0), (self.testing_NoiseConverter_0, 3))
        self.connect((self.analog_const_source_x_0_0_0_0_0, 0), (self.testing_NoiseConverter_0, 4))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.ITpp_Hamming_Soft_Decoder_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.testing_HardReceiver_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.ITpp_BER_Analyzer_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.ITpp_Hamming_Encoder_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_uchar_to_float_0_1_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0_1, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.blocks_uchar_to_float_0_1_0, 0), (self.qtgui_time_sink_x_1_0, 1))
        self.connect((self.blocks_uchar_to_float_0_1_0_0, 0), (self.qtgui_time_sink_x_1_0, 2))
        self.connect((self.testing_HardReceiver_0, 0), (self.ITpp_Hamming_Decoder_0, 0))
        self.connect((self.testing_NoiseConverter_0, 1), (self.ITpp_BER_Analyzer_0, 0))
        self.connect((self.testing_NoiseConverter_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.testing_NoiseConverter_0, 1), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.testing_NoiseConverter_0, 0), (self.qtgui_time_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "BER_Simulation_2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_max_Eb_N0_dB(self):
        return self.max_Eb_N0_dB

    def set_max_Eb_N0_dB(self, max_Eb_N0_dB):
        self.max_Eb_N0_dB = max_Eb_N0_dB
        self.set_max_Ec_N0_dB(self.max_Eb_N0_dB - 10*log10(self.N/self.K))

    def get_min_Eb_N0_dB(self):
        return self.min_Eb_N0_dB

    def set_min_Eb_N0_dB(self, min_Eb_N0_dB):
        self.min_Eb_N0_dB = min_Eb_N0_dB
        self.set_min_Ec_N0_dB(self.min_Eb_N0_dB - 10*log10(self.N/self.K))

    def get_step_Eb_N0_dB(self):
        return self.step_Eb_N0_dB

    def set_step_Eb_N0_dB(self, step_Eb_N0_dB):
        self.step_Eb_N0_dB = step_Eb_N0_dB
        self.set_step_Ec_N0_dB(self.step_Eb_N0_dB)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_m(self.N-self.K)
        self.set_max_Ec_N0_dB(self.max_Eb_N0_dB - 10*log10(self.N/self.K))
        self.set_min_Ec_N0_dB(self.min_Eb_N0_dB - 10*log10(self.N/self.K))

    def get_K(self):
        return self.K

    def set_K(self, K):
        self.K = K
        self.set_m(self.N-self.K)
        self.set_max_Ec_N0_dB(self.max_Eb_N0_dB - 10*log10(self.N/self.K))
        self.set_min_Ec_N0_dB(self.min_Eb_N0_dB - 10*log10(self.N/self.K))

    def get_step_Ec_N0_dB(self):
        return self.step_Ec_N0_dB

    def set_step_Ec_N0_dB(self, step_Ec_N0_dB):
        self.step_Ec_N0_dB = step_Ec_N0_dB

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)

    def get_min_Ec_N0_dB(self):
        return self.min_Ec_N0_dB

    def set_min_Ec_N0_dB(self, min_Ec_N0_dB):
        self.min_Ec_N0_dB = min_Ec_N0_dB

    def get_max_Ec_N0_dB(self):
        return self.max_Ec_N0_dB

    def set_max_Ec_N0_dB(self, max_Ec_N0_dB):
        self.max_Ec_N0_dB = max_Ec_N0_dB

    def get_m(self):
        return self.m

    def set_m(self, m):
        self.m = m



def argument_parser():
    parser = ArgumentParser()
    return parser


def main(top_block_cls=BER_Simulation_2, options=None):
    if options is None:
        options = argument_parser().parse_args()

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
