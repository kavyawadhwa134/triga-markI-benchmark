#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CARDINAL_OPT="${CARDINAL_OPT:-$HOME/cardinal/cardinal-opt}"

cd "$HERE"
python make_triga_model.py
exec "$CARDINAL_OPT" -i triga_openmc.i
