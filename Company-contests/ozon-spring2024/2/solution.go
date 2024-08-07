package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var in *bufio.Reader
	var out *bufio.Writer
	in = bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var s string
	fmt.Fscan(in, &s)
	arr := []byte(s)

	var n int
	fmt.Fscan(in, &n)

	for i := 0; i < n; i++ {
		var start, end int
		var r string
		fmt.Fscan(in, &start, &end, &r)

		for j := 0; j < end-start+1; j++ {
			arr[start+j-1] = r[j]
		}
	}

	fmt.Fprintln(out, string(arr))
}
