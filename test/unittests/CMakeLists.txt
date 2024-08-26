# meraki: C/C++ implementation of Meraki, the Telestai Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

hunter_add_package(GTest)
find_package(GTest CONFIG REQUIRED)

add_executable(
    meraki-test
    helpers.hpp
    test_bit_manipulation.cpp
    test_cases.hpp
    test_meraki.cpp
    test_keccak.cpp
    test_kiss.cpp
    test_managed.cpp
    test_primes.cpp
    test_progpow.cpp
    test_version.cpp
)

set_source_files_properties(test_version.cpp PROPERTIES COMPILE_DEFINITIONS TEST_PROJECT_VERSION="${PROJECT_VERSION}")

target_link_libraries(meraki-test PRIVATE meraki GTest::gtest_main)
target_include_directories(meraki-test PRIVATE ${MERAKI_PRIVATE_INCLUDE_DIR})
set_target_properties(meraki-test PROPERTIES RUNTIME_OUTPUT_DIRECTORY ..)
