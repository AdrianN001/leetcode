



def topKFrequent(nums: list[int], k: int) -> list[int]:

    freq = {}

    for elem in nums: 
        if elem in freq: 
            freq[ elem ] += 1 
        else: 

            freq[ elem ] = 1 
    
    freq_list =  list( sorted( freq.items(), key = lambda x: x[1], reverse=True) )

    return freq_list [ : k]


print(topKFrequent([1,1,1,1,1,1,1,2,2,2,2,2], 4))