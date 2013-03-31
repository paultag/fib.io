#!/bin/bash
shopt -s extglob

last=""
while [ true ]; do
    now=$(find notes themes/fib/less themes/fib/templates themes/fib/resources -type f -printf "%T@ %Tx %TX %p\n" | sort -n -r | head -1)
    if [ "$last" != "$now" ]; then
        make >/dev/null
        echo "Updated."
    fi
    last=$now
    sleep 1
done
