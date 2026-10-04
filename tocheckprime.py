def isprime(n):
    if n < 2:
        return False

    for q in range(2,n):
        if n%q==0:
            return False
    return True
    

print(isprime(7))