# meraki: C/C++ implementation of Meraki, the Telestai Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

string(REPLACE "-fsanitize=fuzzer-no-link" "-fsanitize=fuzzer" CMAKE_EXE_LINKER_FLAGS ${CMAKE_EXE_LINKER_FLAGS})

add_executable(keccak-fuzzer keccak_fuzzer.cpp keccak_tiny.c keccak_rhash.c)
target_link_libraries(keccak-fuzzer PRIVATE meraki)
