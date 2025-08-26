#!/bin/bash

app=${1}
loop="${2:-uvloop}"

uv run granian --interface asgi --loop ${loop} granian_reproducers.${app}
