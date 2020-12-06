package main

import (
  "bufio"
  "fmt"
  "os"
)

func readBatches(c chan <- []string) {
  scanner := bufio.NewScanner(os.Stdin)
  var arr []string
  for scanner.Scan() {
    txt := scanner.Text()
    if len(txt) == 0 {
      c <- arr
      arr = nil
      continue
    }
    arr = append(arr, txt)
  }
  c <- arr
  close(c)
}

func main() {
  c := make(chan []string)
  go readBatches(c)

  anyCount:=0
  everyCount:=0
  for groupAnswers := range c {
    o := make(map[rune]int, 100)
    for _, ans := range groupAnswers {
      for _, k := range ans {
        o[k]++
      }
    }
    anyCount += len(o)
    for _, v := range o {
      if v == len(groupAnswers) {
        everyCount++
      }
    }
  }
  fmt.Printf("%v\n%v\n", anyCount, everyCount)
}
