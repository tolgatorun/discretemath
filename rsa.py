import random

message = random.randrange(1, 100)
print("Message:", message)

primes100_150 = [101,103,107,109,113,127,131,137,139,149]

p = random.choice(primes100_150)
q = random.choice(primes100_150)

while p == q:
    q = random.choice(primes100_150)
print("p: ",p," q: ",q)
n = p * q
r = (p - 1) * (q - 1) 
print("n: ",n,"r: ",r)

def gcd(a, b): 
    if (a == 0):
        return b
    return gcd(b % a, a)

def phi(n): 
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result

e = random.randrange(2, phi(n))
while gcd(e, phi(n)) != 1:
    e = random.randrange(2, phi(n))

print("e: ", e)


def exten_euc(a,b):
    if(a%b==0): 
        return(b,0,1) 
    else:
        gcd,s,t = exten_euc(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
def mult_inv(e,r):
    gcd,s,_=exten_euc(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("d=%d. Since %d is less than 0, d = d(modr), i.e., d=%d."%(s,s,s%r))
        elif(s>0):
            print("d=%d"%(s))
        return s%r

d = mult_inv(e,r)

public_key = (e,n)
private_key = (d,n)
print("Pulic key is: ", public_key,"Private key is", private_key)

encrypted_message = pow(message,e)
encrypted_message = encrypted_message % n

decrypted_message = pow(encrypted_message, d)
decrypted_message = decrypted_message % n

print("Encrypted message is: ",encrypted_message,"\n","Decrypted message is: ", decrypted_message, sep="")