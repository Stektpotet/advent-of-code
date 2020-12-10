#!/usr/bin/env bash
set -euo pipefail

D=$(dirname $(realpath $0))


echo ""
echo "--- Day 9: Encoding Error ---"
$D/../../languages/python.sh $D/input.txt $D/output.txt $D/solutions/day09.stektpotet.py
echo ""
