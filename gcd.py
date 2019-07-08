# Greatest common divisor ptogram : gcd(2,5) = 1
def gcd(a,b):
    while(b):
       a, b = b, a%b
    return a

print(gcd(300, 400))
