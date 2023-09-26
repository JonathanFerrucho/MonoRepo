#!/bin/sh

set -o nounset
set -o errexit
set -o xtrace

cd services/app1
echo "*** RUN cosmic-ray ***"
cosmic-ray init tutorial.toml tutorial.sqlite
cosmic-ray exec tutorial.toml tutorial.sqlite
cr-report tutorial.sqlite
