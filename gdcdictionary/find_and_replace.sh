#!/bin/bash
#https://superuser.com/questions/428493/how-can-i-do-a-recursive-find-and-replace-from-the-command-line
# make sure you are in the schemas directory
echo "Find and replace in current directory!"
echo "File pattern to look for? (eg '*.yaml' for schemas)"
read filepattern
echo "Existing string?"
read existing
echo "Replacement string?"
read replacement
echo "Replacing all occurences of $existing with $replacement in files matching $filepattern"

find . -type f -name $filepattern  -print0 | \
    xargs -0 sed -i'' -e "s/$existing/$replacement/g"