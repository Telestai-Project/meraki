/* meowpow: C/C++ implementation of Meowpow, the Meowcoin Proof of Work algorithm.
 * Copyright 2018-2019 Pawel Bylica.
 * Licensed under the Apache License, Version 2.0.
 */

#include <meowpow/meowpow.h>

int test()
{
    int sum = 0;
    sum += MEOWPOW_EPOCH_LENGTH;
    sum += MEOWPOW_LIGHT_CACHE_ITEM_SIZE;
    sum += MEOWPOW_FULL_DATASET_ITEM_SIZE;
    return sum;
}
