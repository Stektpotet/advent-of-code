#!/usr/bin/env bash
set -euo pipefail

D=$(dirname $(realpath $0))

echo "# Day 12: Passage Pathing -------------------------------------"
$D/../../lang/rust.sh   "$D/solutions/arxcis.rs"      "$D/io/*"
$D/../../lang/python.sh "$D/solutions/stektpotet.py"  "$D/io/*"
