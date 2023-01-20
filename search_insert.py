
# It has to be solved in O(log n), which is the time complexity of a binary search
# https://leetcode.com/problems/search-insert-position/

def searchInsert(nums: list[int], target: int) -> int:
    middle =  nums.__len__() // 2

    if nums[middle] == target :
        return middle
    elif nums[middle] > target :
        return searchInsert(nums[middle:], target)
    else :
        return searchInsert(nums[:middle], target)
	


def main() -> None:

    SAMPLE = [1,2,3,4,5,6,7]
    INDX = 4

    print(searchInsert(SAMPLE,INDX))


if __name__ == "__main__":
    main()