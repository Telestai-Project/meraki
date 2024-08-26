// meraki: C/C++ implementation of Meraki, the Telestai Proof of Work algorithm.
// Copyright 2019 Pawel Bylica.
// Licensed under the Apache License, Version 2.0.

#include <meraki/version.h>

#include <gtest/gtest.h>

TEST(libmeraki, version)
{
    static_assert(meraki::version[0] != 0, "incorrect meraki::version");

    EXPECT_EQ(MERAKI_VERSION, TEST_PROJECT_VERSION);
    EXPECT_EQ(meraki::version, TEST_PROJECT_VERSION);
}
