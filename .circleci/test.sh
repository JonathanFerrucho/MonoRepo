#!/bin/sh

set -o nounset
set -o errexit
set -o xtrace

cd services/publish_component
echo "*** Coverage test for lambda publish_component ***"
poetry install --no-ansi
mutmut run
