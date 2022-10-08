#!/usr/bin/env sh

set -eu

echo "Format"
./format.py
echo "Validate"
./validate.py
