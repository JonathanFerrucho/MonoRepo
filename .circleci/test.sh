#!/bin/sh

set -o nounset
set -o errexit
set -o xtrace

cd services/publish_component
echo "*** RUN MUTMUT ***"
poetry install --no-ansi
mutmut run
