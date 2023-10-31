# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT ITpp_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT ITpp_sources)

########################################################################
# Check for pygccxml
########################################################################
GR_PYTHON_CHECK_MODULE_RAW(
    "pygccxml"
    "import pygccxml"
    PYGCCXML_FOUND
    )

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND ITpp_python_files
    BCH_Decoder_python.cc
    BCH_Encoder_python.cc
    Hamming_Decoder_python.cc
    Hamming_Soft_Decoder_python.cc
    Hamming_Encoder_python.cc
    RS_Decoder_python.cc
    RS_Encoder_python.cc
    BSC_Byte_python.cc
    BER_Analyzer_cpp_python.cc python_bindings.cc)

GR_PYBIND_MAKE_OOT(ITpp
   ../../..
   gr::ITpp
   "${ITpp_python_files}")

# copy bindings extension for use in QA test module
add_custom_command(TARGET ITpp_python POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:ITpp_python>
    ${PROJECT_BINARY_DIR}/test_modules/gnuradio/ITpp/
)

install(TARGETS ITpp_python DESTINATION ${GR_PYTHON_DIR}/gnuradio/ITpp COMPONENT pythonapi)
