# meowpow: C/C++ implementation of Meowpow, the Meowcoin Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

# The CFFI build script for meowpow library.
# It expects the library is installed in the dist/ directory.
# The installation can be performed by
#
#     cmake . -DCMAKE_INSTALL_PREFIX=dist
#     make
#     make install

from cffi import FFI
import sys

ffibuilder = FFI()

stdlib = []
if sys.platform == 'linux':
    stdlib.append('stdc++')

ffibuilder.set_source(
    "_meowpow",
    r"""
    #include <meowpow/keccak.h>
    #include <meowpow/meowpow.h>
     """,
    include_dirs=['include'],
    libraries=['meowpow', 'keccak'] + stdlib,
)

ffibuilder.cdef("""

union meowpow_hash256
{
    ...;
    char str[32];
};

union meowpow_hash512
{
    ...;
    char str[64];
};

struct meowpow_result
{
    union meowpow_hash256 final_hash;
    union meowpow_hash256 mix_hash;
};


union meowpow_hash256 meowpow_keccak256(const uint8_t* data, size_t size);

union meowpow_hash512 meowpow_keccak512(const uint8_t* data, size_t size);

const struct meowpow_epoch_context* meowpow_get_global_epoch_context(int epoch_number);

struct meowpow_result meowpow_hash(const struct meowpow_epoch_context* context,
    const union meowpow_hash256* header_hash, uint64_t nonce);
    
bool meowpow_verify(const struct meowpow_epoch_context* context,
    const union meowpow_hash256* header_hash, const union meowpow_hash256* mix_hash, uint64_t nonce,
    const union meowpow_hash256* boundary);

union meowpow_hash256 light_verify(const union meowpow_hash256* header_hash, const union meowpow_hash256* mix_hash, uint64_t nonce);                            

""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
