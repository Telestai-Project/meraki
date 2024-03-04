# meowpow: C/C++ implementation of Meowpow, the Meowcoin Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

hunter_add_package(benchmark)
find_package(benchmark CONFIG REQUIRED)

add_executable(meowpow-bench
    meowpow_benchmarks.cpp
    keccak_benchmarks.cpp
    keccak_utils.hpp
    keccak_utils.cpp
    managed_benchmarks.cpp
    progpow_benchmarks.cpp
    threadsync_benchmarks.cpp
    threadsync_utils.hpp
    threadsync_utils.cpp)
target_link_libraries(meowpow-bench PRIVATE meowpow benchmark::benchmark)
target_include_directories(meowpow-bench PRIVATE ${MEOWPOW_PRIVATE_INCLUDE_DIR})
set_target_properties(meowpow-bench PROPERTIES RUNTIME_OUTPUT_DIRECTORY ..)
