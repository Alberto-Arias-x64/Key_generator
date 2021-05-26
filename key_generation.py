import random
import math
import os

def initial_values():

    prime_list = (13,17,19,23)

    p, q= random.sample(prime_list, 2)
    return p, q

#____________________________________________________________________________________________________________________________________
def public_key(p, q):

    n = p*q
    phin = (p-1)*(q-1)
    e = random.randrange(2, phin)

    while math.gcd(phin, e) != 1:
        e = random.randrange(2, phin)

    pub_key= str(n)+'-'+str(e)

    return pub_key, phin, e

#____________________________________________________________________________________________________________________________________
def private_key(phin, e):

    i = random.randrange(2,50)
    priv_key = ((i*phin)+1)/e

    while int(priv_key) != priv_key:
        i += 1
        priv_key = ((i*phin)+1)/e

    return priv_key

#____________________________________________________________________________________________________________________________________
if __name__ == '__main__':

    p,q = initial_values()
    pub_key, phin, e = public_key(p, q)
    priv_key = private_key(phin, e)

    print('your public key is: {} \nyour private key is: {}'.format(pub_key,priv_key))
    os.system('pause')