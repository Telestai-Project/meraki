# meraki: C/C++ implementation of Meraki, the Telestai Proof of Work algorithm.
# Copyright 2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

import unittest

import meraki


class TestMeraki(unittest.TestCase):
    epoch_number = 0
    nonce = 902629
    header_hash = bytes.fromhex(
        '0db18c8408b6b9589132a9e7cf6a7d84a639b40e7fe2db5fe938af00c56bf667')
    mix_hash = bytes.fromhex(
        '36f97d67accf6a85bec0d73e305c7fdfa9ac387de9fe35aec6ca548a648ff25b')
    final_hash = bytes.fromhex(
        '000001ca2aa3249de0587423ac38f82846bb8597baa770187f99e997859c8170')

    def test_keccak(self):
        h256 = ('c5d2460186f7233c927e7db2dcc703c0'
                'e500b653ca82273b7bfad8045d85a470')
        h512 = ('0eab42de4c3ceb9235fc91acffe746b2'
                '9c29a8c366b7c60e4e67c466f36a4304'
                'c00fa9caf9d87976ba469bcbe06713b4'
                '35f091ef2769fb160cdab33d3670680e')

        self.assertEqual(meraki.keccak_256(b'').hex(), h256)
        self.assertEqual(meraki.keccak_512(b'').hex(), h512)

    def test_hash(self):
        f, m = meraki.hash(0, self.header_hash, self.nonce)
        self.assertEqual(m, self.mix_hash)
        self.assertEqual(f, self.final_hash)

    def test_verify(self):
        t = meraki.verify(0, self.header_hash, self.mix_hash, self.nonce,
                          self.final_hash)
        self.assertTrue(t)
        self.assertEqual(type(t), bool)


if __name__ == '__main__':
    unittest.main()
