package main

import (
	array "ds"
	"fmt"
)

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 1}
	result := array.ContainsDuplicate(nums)
	fmt.Println(result)
}
