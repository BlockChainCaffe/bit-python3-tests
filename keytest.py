#!/usr/bin/python3

import sys
import bit
from bit import utils


def main():
    key = bit.Key.from_hex('a0dc65ffca799873cbea0ac274015b9526505daaaed385155425f7337704883e')
    # key = bit.Key.from_bytes(b'Satoshi Nakamoto')
    print("Private key: ", key)
    print("Public key:  ", utils.bytes_to_hex(key.public_key, True))
    print("WIF:         ", key.to_wif())
    print("Address:     ", key.address)

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__": 
    main()