package array

import _ "fmt"

func ContainsArray(arr []int, subArr []int) bool {
	m := make(map[int]bool)
	for _, v := range arr {
		if m[v] {
			return true
		}
		m[v] = true
	}
	return false
}
