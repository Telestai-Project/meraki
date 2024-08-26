# meraki: C/C++ implementation of Meraki, the Telestai Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

find_package(Threads)

add_executable(meraki-fakeminer fakeminer.cpp)
target_link_libraries(meraki-fakeminer PRIVATE meraki Threads::Threads)
set_target_properties(meraki-fakeminer PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)
