// meowpow: C/C++ implementation of Meowpow, the Meowcoin Proof of Work algorithm.
// Copyright 2019 Pawel Bylica.
// Licensed under the Apache License, Version 2.0.

#include <meowpow/version.h>

#include <gtest/gtest.h>

TEST(libmeowpow, version)
{
    static_assert(meowpow::version[0] != 0, "incorrect meowpow::version");

    EXPECT_EQ(MEOWPOW_VERSION, TEST_PROJECT_VERSION);
    EXPECT_EQ(meowpow::version, TEST_PROJECT_VERSION);
}
