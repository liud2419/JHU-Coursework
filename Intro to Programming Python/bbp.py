import math

def recursive_bbp(k):
    if k < 0:
        return 0
    else:
        current_term = ((4/(8*k+1)) - (2/(8*k+4)) - (1/(8*k+5)) - (1/(8*k+6))) * (1/16**k)
        print(f"{k}\t{current_term}".expandtabs(4))
        return current_term + recursive_bbp(k-1)

def main():
    n = 10
    print("k\tcontribution to the value of π".expandtabs(4))
    bbp_pi = recursive_bbp(n)
    print("\nThe BBP value of π = {}".format(bbp_pi))
    print("The Math module value of π = {}".format(math.pi))

if __name__ == '__main__':
    main()