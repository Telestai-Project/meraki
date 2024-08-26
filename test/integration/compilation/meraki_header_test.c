/* meraki: C/C++ implementation of Meraki, the Telestai Proof of Work algorithm.
 * Copyright 2018-2019 Pawel Bylica.
 * Licensed under the Apache License, Version 2.0.
 */

#include <meraki/meraki.h>

int test()
{
    int sum = 0;
    sum += MERAKI_EPOCH_LENGTH;
    sum += MERAKI_LIGHT_CACHE_ITEM_SIZE;
    sum += MERAKI_FULL_DATASET_ITEM_SIZE;
    return sum;
}
