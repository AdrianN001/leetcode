

def reverse_bit( n: int ) -> int: 
    res: str = bin(n)[2:] # bin return the string with the prefix of "0b"
    res = f"{'0'*(32-len(res))}{res}"

    # str is unmutable
    res = [ x for x in res ]
    copy = res.copy()


    for idx in range(32):
        res[idx] = copy[32 - idx - 1]
    return int("".join(res),2)

print(reverse_bit(43261596))
