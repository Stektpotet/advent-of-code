#!/usr/bin/env bash
set -e

# Usage:   ./test-go.sh INPUT              OUTPUT             SOLUTION
# Example: ./test-go.sh /day-03/input.txt  /day-03/input.txt  /day-03/solutions/main.go

INPUT="$1"
OUTPUT="$2"
SOLUTION="$3"

cat $INPUT | go run $SOLUTION | diff - $OUTPUT
echo "cat INPUT | go run $SOLUTION ✅"
