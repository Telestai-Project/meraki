# meraki: C/C++ implementation of Meraki, the Telestai Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

hunter_add_package(benchmark)
find_package(benchmark CONFIG REQUIRED)

add_executable(meraki-bench
    meraki_benchmarks.cpp
    keccak_benchmarks.cpp
    keccak_utils.hpp
    keccak_utils.cpp
    managed_benchmarks.cpp
    progpow_benchmarks.cpp
    threadsync_benchmarks.cpp
    threadsync_utils.hpp
    threadsync_utils.cpp)
target_link_libraries(meraki-bench PRIVATE meraki benchmark::benchmark)
target_include_directories(meraki-bench PRIVATE ${MERAKI_PRIVATE_INCLUDE_DIR})
set_target_properties(meraki-bench PROPERTIES RUNTIME_OUTPUT_DIRECTORY ..)
