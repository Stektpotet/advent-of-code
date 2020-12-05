package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
	"regexp"
)

func onNewBatch(data []byte, atEOF bool) (advance int, token []byte, err error) {
  for i := 0; i < len(data)-1; i++ {
		if (data[i] == '\n') && (data[i+1] == '\n') {
			return i+2, data[:i+1], nil
		}
	}
	if !atEOF {
		return 0, nil, nil
	}
		// There is one final token to be delivered, which may be the empty string.
		// Returning bufio.ErrFinalToken here tells Scan there are no more tokens after this
		// but does not trigger an error to be returned from Scan itself.
	return 0, data, bufio.ErrFinalToken
}

func outOfRange(val string, low, high int) bool {
  i, err := strconv.Atoi(val)
  if err != nil {
    return true
  }
  return i < low || high < i
}

func validate(fields []string) {
  for _, f := range fields {
    fmt.Println(f[:3], "=", f[4:])
  }
  //fmt.Println(fields, len(fields))
}

type Range struct {
  Min int
  Max int
}


func main() {
  eye_colors := map[string]struct{}{
    "amb": struct{}{},
    "blu": struct{}{},
    "brn": struct{}{},
    "gry": struct{}{},
    "grn": struct{}{},
    "hzl": struct{}{},
    "oth": struct{}{},
  }
  height_limits := map[string]Range {
    "cm": Range{Min:150, Max:193},
    "in": Range{Min:59, Max:76},
  }
  validation_lookup := map[string]func(val string)bool {
    "byr": func(val string) bool { return outOfRange(val, 1920, 2002) },
    "iyr": func(val string) bool { return outOfRange(val, 2010, 2020) },
    "eyr": func(val string) bool { return outOfRange(val, 2020, 2030) },
    "ecl": func(val string) bool {
      _, ok := eye_colors[val]
      return !ok
    },
    "hgt": func(val string) bool {
      limits, ok := height_limits[val[len(val)-2:]]
      return !ok || outOfRange(val[:len(val)-2], limits.Min, limits.Max)
    },
    "hcl": func(val string) bool {
      match, err := regexp.MatchString(`^#[0-9a-f]{6}$`, val)
      if err != nil {
        return true
      }
      return !match
    },
    "pid": func(val string) bool {
      match, err := regexp.MatchString(`^[0-9]{9}$`, val)
      if err != nil {
        return true
      }
      return !match
    },
  }

	// Initialization and input reading
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(onNewBatch)
  entries := []string{}
	for scanner.Scan() {
	  entries = append(entries, scanner.Text())
	}
	for _, entry := range entries {
	  validate(strings.Fields(entry))
	  break
	}
}
