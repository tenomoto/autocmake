# (c) https://github.com/dev-cafe/autocmake/blob/master/AUTHORS.md
# licensed under BSD-3: https://github.com/dev-cafe/autocmake/blob/master/LICENSE

#.rst:
#
# Find and link to CBLAS.
#
# Variables defined::
#
#   CBLAS_FOUND - describe me, uncached
#   CBLAS_LIBRARIES - describe me, uncached
#   CBLAS_INCLUDE_DIR - describe me, uncached
#
# autocmake.yml configuration::
#
#   url_root: https://github.com/dev-cafe/autocmake/raw/master/
#   docopt: "--cblas Find and link to CBLAS [default: False]."
#   define: "'-DENABLE_CBLAS={0}'.format(arguments['--cblas'])"
#   fetch:
#     - "%(url_root)modules/find/find_libraries.cmake"
#     - "%(url_root)modules/find/find_include_files.cmake"

option(ENABLE_CBLAS "Find and link to CBLAS" OFF)

if(ENABLE_CBLAS)
    include(${CMAKE_CURRENT_LIST_DIR}/find_libraries.cmake)
    include(${CMAKE_CURRENT_LIST_DIR}/find_include_files.cmake)

    set(CBLAS_FOUND FALSE)
    set(CBLAS_LIBRARIES "NOTFOUND")
    set(CBLAS_INCLUDE_DIR "NOTFOUND")

    _find_library(cblas cblas_dgemm CBLAS_LIBRARIES)
    _find_include_dir(cblas.h /usr CBLAS_INCLUDE_DIR)

    if(NOT "${CBLAS_LIBRARIES}" MATCHES "NOTFOUND")
        if(NOT "${CBLAS_INCLUDE_DIR}" MATCHES "NOTFOUND")
            set(CBLAS_FOUND TRUE)
        endif()
    endif()
endif()
