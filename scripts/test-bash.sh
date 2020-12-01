#!/usr/bin/env bash
set -e

# Usage:   ./test-bash.sh INPUT              OUTPUT             SOLUTION
# Example: ./test-bash.sh /day-03/input.txt  /day-03/input.txt  /day-03/solutions/main.bash

INPUT="$1"
OUTPUT="$2"
SOLUTION="$3"

cat "$INPUT" | bash "$SOLUTION" | diff - "$OUTPUT"
echo "cat INPUT | bash $SOLUTION ✅"
