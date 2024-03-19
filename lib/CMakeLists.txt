# meowpow: C/C++ implementation of Meowpow, the Meowcoin Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

add_subdirectory(keccak)
add_subdirectory(meowpow)

get_filename_component(MEOWPOW_PRIVATE_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR} ABSOLUTE)
set(MEOWPOW_PRIVATE_INCLUDE_DIR ${MEOWPOW_PRIVATE_INCLUDE_DIR} PARENT_SCOPE)
