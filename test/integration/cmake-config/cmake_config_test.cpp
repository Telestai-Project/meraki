// meraki: C/C++ implementation of Meraki, the Telestai Proof of Work algorithm.
// Copyright 2018-2019 Pawel Bylica.
// Licensed under the Apache License, Version 2.0.

#include <meraki/meraki.hpp>
#include <meraki/version.h>

int main()
{
    static_assert(sizeof(meraki::version) >= 6, "incorrect meraki::version");

    uint8_t seed_bytes[32] = {0};
    meraki::hash256 seed = meraki::hash256_from_bytes(seed_bytes);
    return meraki::find_epoch_number(seed);
}
