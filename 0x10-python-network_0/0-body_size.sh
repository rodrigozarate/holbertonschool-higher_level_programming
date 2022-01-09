#!/bin/bash
# Example of getting bExample of getting body size
curl -sI "$1" | grep 'Content-Lenght:' | cut -f2 -d' '
