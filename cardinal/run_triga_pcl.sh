#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CARDINAL_OPT="${CARDINAL_OPT:-$HOME/cardinal/cardinal-opt}"

cd "$HERE"
export TRIGA_PARTICLES=8000
export TRIGA_BATCHES=70
export TRIGA_INACTIVE=20
python make_triga_model.py
exec mpiexec -n 1 "$CARDINAL_OPT" -i triga_openmc_pcl.i
