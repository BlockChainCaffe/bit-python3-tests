from Crypto.Hash import SHA256
from perkle import MerkleTree
from binascii import hexlify
import pprint

pp = pprint.PrettyPrinter(indent=4)

data_list = [] 
for d in range (1,4096*4):
    data_list.append(bytes(str(d),'utf-8'))
[b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9']
sha256 = lambda x : SHA256.new(x).digest() 

mt = MerkleTree(data_list, sha256, random_padding=False, padding_byte=b'0')

#70cc27c03c0444d1dfc63f58e373a2882a7b9f4f7f6ed1a4dfc1a94a5ac5875c

E = data_list[0]
index, proof_hashes = mt.proof(E)

print()
print()

print(hexlify(sha256(E)).decode("utf-8"),"(your leaf)")
for p in proof_hashes:
    print(hexlify(p).decode("utf-8"))
print(hexlify(mt.root()).decode("utf-8"),"(root)")

# print(MerkleTree.verify(E,index,proof_hashes,mt.root(),sha256))

i = data_list.index(E)

# print()
# print()
# if i%2 :
#     print(hexlify(sha256(data_list[i-1])))
#     print(hexlify(sha256(data_list[i])))
#     print (hexlify(  sha256 ( sha256(data_list[i-1]) + sha256(data_list[i]) ) ) )
# else :
#     print(hexlify(sha256(data_list[i])))
#     print(hexlify(sha256(data_list[i+1])))
#     print (hexlify(  sha256 ( sha256(data_list[i]) + sha256(data_list[i+1]) ) ) )
    
print()
print()

s = '│ ' * (len(proof_hashes)-1) # + '└─' # '├─'
m = ' (leaf)'
h = sha256(E)
t = []
for p in proof_hashes:
    if index % 2:
        t.insert(0, s+'├─'+hexlify(p).decode("utf-8")+'*')
        t.append(s+ '└─'+hexlify(h).decode("utf-8")+m)
        h = sha256(p + h)
    else:
        t.insert(0, s+'├─'+hexlify(h).decode("utf-8")+m)
        t.append(s+ '└─'+hexlify(p).decode("utf-8")+'*')
        h = sha256(h + p)
    index //= 2
    s = s[2:]
    m = ''

t.insert(0, s+hexlify(h).decode("utf-8")+' (root)')
# t.reverse()
for b in t:
    print(b)
