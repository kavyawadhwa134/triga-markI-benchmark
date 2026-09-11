#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CARDINAL_OPT="${CARDINAL_OPT:-$HOME/cardinal/cardinal-opt}"

cd "$HERE"
export NEKRS_HOME="${NEKRS_HOME:-$HOME/cardinal/install}"
export OMP_NUM_THREADS=1
export MAKEFLAGS=-j1
exec mpiexec -n 1 "$CARDINAL_OPT" -i nek.i
