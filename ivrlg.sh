#!/bin/bash
# Ask the user for the file name

FILE=$1

iverilog -o "${FILE%.*}" $1
vvp "${FILE%.*}"

