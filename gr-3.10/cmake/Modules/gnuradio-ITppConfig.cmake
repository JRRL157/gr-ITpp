find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_ITPP gnuradio-ITpp)

FIND_PATH(
    GR_ITPP_INCLUDE_DIRS
    NAMES gnuradio/ITpp/api.h
    HINTS $ENV{ITPP_DIR}/include
        ${PC_ITPP_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_ITPP_LIBRARIES
    NAMES gnuradio-ITpp
    HINTS $ENV{ITPP_DIR}/lib
        ${PC_ITPP_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-ITppTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_ITPP DEFAULT_MSG GR_ITPP_LIBRARIES GR_ITPP_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_ITPP_LIBRARIES GR_ITPP_INCLUDE_DIRS)
