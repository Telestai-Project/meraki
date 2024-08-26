# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

cmake_minimum_required(VERSION 3.5)

project(meraki-cmake-config-test)

find_package(meraki CONFIG REQUIRED)

add_executable(meraki-cmake-config-test cmake_config_test.cpp)
target_link_libraries(meraki-cmake-config-test meraki::meraki)
set_target_properties(meraki-cmake-config-test PROPERTIES CXX_STANDARD 11 CXX_EXTENSIONS OFF)
