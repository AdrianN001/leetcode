#https://leetcode.com/problems/longest-consecutive-sequence

def longestConsecutive( nums: list[int]) -> int:
        if not nums: 
            return 0
        nums = list(set(nums))
        # there's no need for the duplicates

        nums.sort() 

        # Grouping the into list of consecutive integers 
        groups: list[list[int]]= [[nums[0]]] 

        for i in nums[1:]:
            last_number = groups[-1][-1]

            if i - 1 == last_number: 
                groups[-1].append(i)
            else: 
                groups.append( [i] )
        
        # return the longest group
        return  max( groups, key=lambda x: x.__len__()).__len__()