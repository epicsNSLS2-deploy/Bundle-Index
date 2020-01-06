#!/bin/bash

if [ "$#" != "1" ];
then
echo "ERROR - One argument (path to production folder) required."
else
echo "Starting update + push"
for d in $1/./*
do
python3 mass_update_docs.py $d
done
DATE=$(date '+%Y-%m-%d-%H:%M:%S')
git add -A
git commit -m "Updating AD Bundle Index on $DATE"
git push
python3 -m mkdocs gh-deploy
fi
