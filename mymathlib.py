import math

def is_prime(n):
        #push new feature into master
        if n < 2:
            return False

        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
