#!/usr/bin/env python

"""Ex__1_compute_block_hash.py: Answer to Ch 15 Ex 1."""

# This is a solution for Bitcoin block 711735
# See https://bitaps.com/711735

import binascii
import hashlib    

# The block header copied from bitaps.com
header = '00000020505424e0dc22a7fb1598d3a048a31957315f737ec0d00b' + \
    '0000000000000000005f7fbc00ac45edd1f6ca7713f2b048d8a771c95e1' + \
    'afd9140d3a147a063f64a76781ea461139a0c17f666fc1afdbc08'

# The hash of the header copied from bitaps.com
header_hash = \
    '00000000000000000000bc01913c2e05a5d38d39a9df0c8ba4269abe9777f41f'

# Cut off any extra bytes beyond the 80-byte header
header = header[:160]

# Convert the header to binary
header = binascii.unhexlify(header)

# Compute the header hash (perform SHA-256 twice)
computed_hash = hashlib.sha256(header).digest()
computed_hash = hashlib.sha256(computed_hash).digest()

# Reverse the byte order
computed_hash = computed_hash[::-1]

# Convert the binary header hash to a hexadecimal string
computed_hash = binascii.hexlify(computed_hash).decode("utf-8")

# Print the result
if header_hash == computed_hash:
    result = 'Hashes match!'
else:
    result = 'Hashes DO NOT match!'

print(result)
