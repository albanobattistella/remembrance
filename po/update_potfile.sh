#!/usr/bin/env bash

dir=$(dirname "$(realpath "$0")")

cd "${dir}"
cd '../'

xgettext -f "${dir}/POTFILES" -o "${dir}/remembrance.pot" --keyword=_ --from-code=UTF-8 --package-name="remembrance"

