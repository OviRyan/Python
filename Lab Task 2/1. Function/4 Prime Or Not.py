def IzPrime(num):
    if num <= 1:
        return "Not Prime"  # Numbers <= 1 are not prime
    for i in range(2, int(num**0.5) + 1):  # Iterate from 2 to √num
        if num % i == 0:
            return "Not Prime"  # Found a divisor, not prime
    return "Prime"  # No divisors found, number is prime

# Test 
print(IzPrime(7))  # Should print "Prime"
print(IzPrime(10))  # Should print "Not Prime"
print(IzPrime(1))  # Should print "Not Prime"
