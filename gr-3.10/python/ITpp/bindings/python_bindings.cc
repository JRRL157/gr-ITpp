/*
 * Copyright 2020 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

#include <pybind11/pybind11.h>

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <numpy/arrayobject.h>

namespace py = pybind11;

// Headers for binding functions
/**************************************/
// The following comment block is used for
// gr_modtool to insert function prototypes
// Please do not delete
/**************************************/
// BINDING_FUNCTION_PROTOTYPES(
    void bind_BCH_Decoder(py::module& m);
    void bind_BCH_Encoder(py::module& m);
    void bind_Hamming_Decoder(py::module& m);
    void bind_Hamming_Soft_Decoder(py::module& m);
    void bind_Hamming_Encoder(py::module& m);
    void bind_RS_Decoder(py::module& m);
    void bind_RS_Encoder(py::module& m);
    void bind_BSC_Byte(py::module& m);
    void bind_BER_Analyzer_cpp(py::module& m);
    void bind_Decoder_BPSK(py::module& m);
// ) END BINDING_FUNCTION_PROTOTYPES


// We need this hack because import_array() returns NULL
// for newer Python versions.
// This function is also necessary because it ensures access to the C API
// and removes a warning.
void* init_numpy()
{
    import_array();
    return NULL;
}

PYBIND11_MODULE(ITpp_python, m)
{
    // Initialize the numpy C API
    // (otherwise we will see segmentation faults)
    init_numpy();

    // Allow access to base block methods
    py::module::import("gnuradio.gr");

    /**************************************/
    // The following comment block is used for
    // gr_modtool to insert binding function calls
    // Please do not delete
    /**************************************/
    // BINDING_FUNCTION_CALLS(
    bind_BCH_Decoder(m);
    bind_BCH_Encoder(m);
    bind_Hamming_Decoder(m);
    bind_Hamming_Soft_Decoder(m);
    bind_Hamming_Encoder(m);
    bind_RS_Decoder(m);
    bind_RS_Encoder(m);
    bind_BSC_Byte(m);
    bind_BER_Analyzer_cpp(m);
    bind_Decoder_BPSK(m);
    // ) END BINDING_FUNCTION_CALLS
}