# meowpow: C/C++ implementation of Meowpow, the Meowcoin Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

hunter_add_package(GTest)
find_package(GTest CONFIG REQUIRED)

add_executable(
    meowpow-test
    helpers.hpp
    test_bit_manipulation.cpp
    test_cases.hpp
    test_meowpow.cpp
    test_keccak.cpp
    test_kiss.cpp
    test_managed.cpp
    test_primes.cpp
    test_progpow.cpp
    test_version.cpp
)

set_source_files_properties(test_version.cpp PROPERTIES COMPILE_DEFINITIONS TEST_PROJECT_VERSION="${PROJECT_VERSION}")

target_link_libraries(meowpow-test PRIVATE meowpow GTest::gtest_main)
target_include_directories(meowpow-test PRIVATE ${MEOWPOW_PRIVATE_INCLUDE_DIR})
set_target_properties(meowpow-test PROPERTIES RUNTIME_OUTPUT_DIRECTORY ..)
