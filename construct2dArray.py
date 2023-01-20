def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    if m * n != original.__len__(): 
        return []

    res = [[]]

    for indx, item in original: 
        if indx % m != 0:
            res[-1].append(item)
        else:
            res.append([])
    return res 


