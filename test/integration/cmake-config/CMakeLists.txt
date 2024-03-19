# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

cmake_minimum_required(VERSION 3.5)

project(meowpow-cmake-config-test)

find_package(meowpow CONFIG REQUIRED)

add_executable(meowpow-cmake-config-test cmake_config_test.cpp)
target_link_libraries(meowpow-cmake-config-test meowpow::meowpow)
set_target_properties(meowpow-cmake-config-test PROPERTIES CXX_STANDARD 11 CXX_EXTENSIONS OFF)
