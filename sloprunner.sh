#!/bin/bash

export BASH_ENV="$HOME/.bashrc"


DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1


VENV_PY="$DIR/env/bin/python"
"$VENV_PY" "$DIR/main.py"