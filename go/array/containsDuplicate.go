package array

import "fmt"

func ContainsDuplicate(nums []int) bool {
	m := make(map[int]bool)
	for _, v := range nums {
		if m[v] {
			return true
		}
		m[v] = true
	}
	return false
}
func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 1}
	result := ContainsDuplicate(nums)
	fmt.Println(result)
}
