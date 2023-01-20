package main

import "fmt"

// It has to be solved in O(log n), which is the time complexity of a binary search
// https://leetcode.com/problems/search-insert-position/

func searchInsert(nums []int, target int) int {
	middle := int(len(nums) / 2)

	if nums[middle] == target {
		return middle
	} else if nums[middle] > target {
		return searchInsert(nums[middle:], target)
	} else {
		return searchInsert(nums[:middle], target)
	}
}

func main() {
	sample := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	index := 4

	fmt.Println(searchInsert(sample, index))
}
