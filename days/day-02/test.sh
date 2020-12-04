#!/usr/bin/env bash
set -e

D=$(dirname $(realpath $0))

echo ""
echo "--- Day 2: Password Philosophy ---"
$D/../../languages/go.sh      $D/input.txt $D/output.txt $D/solutions/day02.go
$D/../../languages/c.sh       $D/input.txt $D/output.txt $D/solutions/day02.c
$D/../../languages/cpp.sh     $D/input.txt $D/output.txt $D/solutions/day02.cpp
$D/../../languages/python.sh  $D/input.txt $D/output.txt $D/solutions/day02.py
$D/../../languages/sml.sh     $D/input.txt $D/output.txt $D/solutions/day02.sml
echo ""
