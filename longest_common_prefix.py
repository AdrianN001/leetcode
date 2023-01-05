sample: list = ["flower","flow","flight"]

def longest_common_prefix( strs: list ) -> str:
    pref = ""
    shortest_word = min( strs, key = len )

    for indx in range( shortest_word.__len__() ): 
        
        for word in strs: 
            if word[indx] != shortest_word[indx]:
                return pref
        pref += shortest_word[indx]
    return pref

print(" Lista: ", sample)
print(" Leghosszabb elotag: ", longest_common_prefix(sample) )
