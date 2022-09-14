#!/usr/bin/env bash
set -euo pipefail

D=$(dirname $(realpath $0))

echo "# Day 1: Sonar Sweep ------------------------------------------"
$D/../../lang/zig.sh     $D/solutions/*.zig  "$D/io/*"
$D/../../lang/rust.sh    $D/solutions/*.rs   "$D/io/*"
$D/../../lang/python.sh  $D/solutions/*.py   "$D/io/*"
