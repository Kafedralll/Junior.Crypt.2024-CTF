# pip install lightphe

from lightphe import LightPHE
import pickle
 
# build a cryptosystem
with open(f'vote/cs.pickle', 'rb') as f:
    cs = pickle.load(f) 

# load votes
with open(f'vote/vote.{0}.pickle', 'rb') as f:
    res = pickle.load(f)
for i in range(1, N):
    with open(f'vote/vote.{i}.pickle', 'rb') as f:
        res = res + pickle.load(f)

# calculate plaintexts
res = cs.decrypt(res)
v = (hex(res)[2:]).zfill(16)
vv = [int(v[i:i+2], 16) for i in range(0, len(v),2)]
print (vv)
