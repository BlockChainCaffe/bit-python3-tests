#!/usr/bin/python3

'''
https://github.com/ofek/bit
https://ofek.github.io/bit/index.html
'''

import sys
import bit
import hashlib
from bit import utils


def main():
	# echo -n "Satoshi Nakamoto" | sha256sum
    # key = bit.Key.from_hex('a0dc65ffca799873cbea0ac274015b9526505daaaed385155425f7337704883e')
    # key = bit.Key.from_bytes(b'Satoshi Nakamoto')

    seed = ''.join(sys.argv[1:])
    priv = hashlib.sha256(seed.encode('utf-8')).hexdigest()
    key = bit.Key.from_hex(priv)
	 
    #priv="a0dc65ffca799873cbea0ac274015b9526505daaaed385155425f7337704883e"
    #key = bit.Key.from_hex(priv)

    print("Private key: ", priv)
    print("Public key:  ", utils.bytes_to_hex(key.public_key, True))
    print("WIF:         ", key.to_wif())
    print("Address:     ", key.address)

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if __name__ == "__main__": 
    main()