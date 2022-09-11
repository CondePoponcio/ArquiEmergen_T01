#!/bin/bash
#
# Do a ping and output results as CSV.
#
# Original Script Author: dsimmons@squiz.co.uk
# 2011-12-23
#
# Update Script Author: felipe.condore@mail.udp.cl
# 2022-09-10

trap echo 0

contador=0
data="$1"
min=$2
max=$3

echo "$2 $3 == $1"
