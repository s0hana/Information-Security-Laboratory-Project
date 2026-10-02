print("       DIFFIE-HELLMAN KEY EXCHANGE")
q = int(input("Enter the prime number q: "))
while True:
    if q < 2:
        prime = False
    else:
        prime = True
        i = 2
        while i*i <= q:
            if q % i == 0:
                prime = False
                break
            i += 1
    if prime:
        break
    q = int(input(str(q) + " is not prime, enter q again: "))


alpha = int(input("Enter the primitive root alpha: "))
while True:
    if alpha < 2 or alpha >= q:
        primitive = False
    else:
        values = []
        value = 1
        primitive = True
        i = 1
        while i < q:
            value = (value*alpha) % q
            if value in values:
                primitive = False
                break
            values.append(value)
            i += 1
    if primitive:
        break
    alpha = int(input(str(alpha) +" is not a primitive root of " +str(q) +", enter alpha again: "))

xa = int(input("Enter the private key of A (XA): "))
while xa < 1 or xa >= q:
    xa = int(input("XA must be between 1 and q-1, enter XA again: "))

xb = int(input("Enter the private key of B (XB): "))
while xb < 1 or xb >= q:
    xb = int(input("XB must be between 1 and q-1, enter XB again: "))

ya = 1
i = 0
while i < xa:
    ya = (ya*alpha) % q
    i += 1

yb = 1
i = 0
while i < xb:
    yb = (yb*alpha) % q
    i += 1

ka = 1
i = 0
while i < xa:
    ka = (ka*yb) % q
    i += 1

kb = 1
i = 0
while i < xb:
    kb = (kb*ya) % q
    i += 1

print("Global Public Elements")
print("q =", q)
print("alpha =", alpha)
print("User A Key Generation")
print("Private XA =", xa)
print("Public YA =", ya)
print("User B Key Generation")
print("Private XB =", xb)
print("Public YB =", yb)
print("Exchange")
print("A sends YA =", ya, "to B")
print("B sends YB =", yb, "to A")
print("Secret Key Calculation")
print("By A: K =", ka)
print("By B: K =", kb)
if ka == kb:
    print("Shared secret key =", ka)
else:
    print("Key exchange failed")
