# meowpow: C/C++ implementation of Meowpow, the Meowcoin Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

include(GNUInstallDirs)

add_library(
    meowpow
    bit_manipulation.h
    builtins.h
    endianness.hpp
    ${include_dir}/meowpow/meowpow.h
    ${include_dir}/meowpow/meowpow.hpp
    meowpow-internal.hpp
    meowpow.cpp
    ${include_dir}/meowpow/hash_types.h
    managed.cpp
    kiss99.hpp
    primes.h
    primes.c
    ${include_dir}/meowpow/progpow.hpp
    progpow.cpp
)

target_link_libraries(meowpow PRIVATE keccak)
target_include_directories(meowpow PUBLIC $<BUILD_INTERFACE:${include_dir}>$<INSTALL_INTERFACE:include>)
if(CABLE_COMPILER_GNULIKE AND NOT SANITIZE MATCHES undefined)
    target_compile_options(meowpow PRIVATE $<$<COMPILE_LANGUAGE:CXX>:-fno-rtti>)
endif()

install(
    TARGETS meowpow
    EXPORT meowpowTargets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
