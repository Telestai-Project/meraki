# meraki: C/C++ implementation of Meraki, the Telestai Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

from _meraki import ffi, lib


def keccak_256(data):
    hash = lib.meraki_keccak256(ffi.from_buffer(data), len(data))
    return ffi.unpack(hash.str, len(hash.str))


def keccak_512(data):
    hash = lib.meraki_keccak512(ffi.from_buffer(data), len(data))
    return ffi.unpack(hash.str, len(hash.str))


def hash(epoch_number, header_hash, nonce):
    if len(header_hash) != 32:
        raise ValueError('header_hash must have length of 32')

    ctx = lib.meraki_get_global_epoch_context(epoch_number)
    c_header_hash = ffi.new('union meraki_hash256*')
    c_header_hash[0].str = header_hash
    result = lib.meraki_hash(ctx, c_header_hash, nonce)
    final_hash = ffi.unpack(result.final_hash.str, len(result.final_hash.str))
    mix_hash = ffi.unpack(result.mix_hash.str, len(result.mix_hash.str))
    return final_hash, mix_hash


def verify(epoch_number, header_hash, mix_hash, nonce, boundary):
    if len(header_hash) != 32:
        raise ValueError('header_hash must have length of 32')
    if len(mix_hash) != 32:
        raise ValueError('mix_hash must have length of 32')
    if len(boundary) != 32:
        raise ValueError('boundary must have length of 32')

    ctx = lib.meraki_get_global_epoch_context(epoch_number)
    c_header_hash = ffi.new('union meraki_hash256*')
    c_header_hash[0].str = header_hash
    c_mix_hash = ffi.new('union meraki_hash256*')
    c_mix_hash[0].str = mix_hash
    c_boundary = ffi.new('union meraki_hash256*')
    c_boundary[0].str = boundary

    return lib.meraki_verify(ctx, c_header_hash, c_mix_hash, nonce, c_boundary)

def light_verify(header_hash, mix_hash, nonce):
    if len(header_hash) != 32:
        raise ValueError('header_hash must have length of 32')

    c_header_hash = ffi.new('union meraki_hash256*')
    c_header_hash[0].str = header_hash

    c_mix_hash = ffi.new('union meraki_hash256*')
    c_mix_hash[0].str = mix_hash

    result = lib.light_verify(c_header_hash, c_mix_hash, nonce)
    final_hash = ffi.unpack(result.str, len(result.str))
    return final_hash
