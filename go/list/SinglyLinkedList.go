package list

import "fmt"

type Node struct {
	Value int
	Next  *Node
}

func main() {
	aa := Node{Value: 1}
	bb := Node{Value: 2}
	cc := Node{Value: 3}
	aa.Next = &bb
	bb.Next = &cc
}
func Print(root *Node) {
	nodeWalk := root
	for nodeWalk.Next != nil {
		fmt.Println(nodeWalk.Value)
		nodeWalk = nodeWalk.Next
	}
	x := []int{1, 2, 3}
	x = append([]int{0}, x...)
	fmt.Println(x)
	fmt.Println(nodeWalk.Value)
}
func Len(root *Node) int {
	nodeWalk := root
	count := 1
	for nodeWalk.Next != nil {
		count = count + 1
		nodeWalk = nodeWalk.Next
	}

	return count
}
