#!/usr/bin/env bash
set -e

# Usage:   ./test-rs.sh INPUT              OUTPUT             SOLUTION
# Example: ./test-rs.sh /day-03/input.txt  /day-03/input.txt  /day-03/solutions/main.rs

INPUT="$1"
OUTPUT="$2"
SOLUTION="$3"
OUT="/tmp/aoc2020.rustc.out"

rustc $SOLUTION -o $OUT;
cat $INPUT | $OUT | diff - $OUTPUT
rm $OUT;
echo "cat INPUT | rustc $SOLUTION ✅"
