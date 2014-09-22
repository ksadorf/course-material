#!/bin/sh

if ! git remote -v | grep -q "upstream"
    then 
    git remote add upstream https://github.com/hackinscience/course-material.git
fi
git fetch upstream
git checkout master
git merge upstream/master
git push
echo "Done."
    
