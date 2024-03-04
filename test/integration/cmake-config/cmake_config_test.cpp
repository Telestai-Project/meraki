// meowpow: C/C++ implementation of Meowpow, the Meowcoin Proof of Work algorithm.
// Copyright 2018-2019 Pawel Bylica.
// Licensed under the Apache License, Version 2.0.

#include <meowpow/meowpow.hpp>
#include <meowpow/version.h>

int main()
{
    static_assert(sizeof(meowpow::version) >= 6, "incorrect meowpow::version");

    uint8_t seed_bytes[32] = {0};
    meowpow::hash256 seed = meowpow::hash256_from_bytes(seed_bytes);
    return meowpow::find_epoch_number(seed);
}
