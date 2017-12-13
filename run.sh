#! /bin/sh

for i in $( cat pods ); do
    echo collect pod: $i
    python podstats.py $i      >> data/$i
done
