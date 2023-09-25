#!/bin/sh

set -o nounset
set -o errexit
set -o xtrace

cd services/app1
echo "*** RUN MUTMUT ***"
mutmut run
