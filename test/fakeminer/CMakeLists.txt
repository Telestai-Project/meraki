# meowpow: C/C++ implementation of Meowpow, the Meowcoin Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

find_package(Threads)

add_executable(meowpow-fakeminer fakeminer.cpp)
target_link_libraries(meowpow-fakeminer PRIVATE meowpow Threads::Threads)
set_target_properties(meowpow-fakeminer PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)
