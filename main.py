# a python sikript for making a simple obsidian index file.
# 2023-12-27
# Author: miv403

file = open("./list.txt", "r", encoding="utf-8")
# i assuming the content of list.txt file is output of `ls` command that
# executed in a folder which contains only `*.md` files.
# the script may not work properly if the input file contains file types other than `markdown`

output = open("./output.txt", "w", encoding="utf-8")
file = file.read()

# reading a list from list.txt file then creating a output file.

titleList = file.split("\n")
# all file names should be seperated a newline character in list.txt file. 

length = len(titleList)
# we will need index numbers of this list so we should keep the length of this list.

replace = "" # temporary string variable for list item changes.
for i in range(0,length):
    # some file names may have single quote charater.
    # `ls` is putting this character especially for file names which have blank character.
    # so this character should be striped.
    replace = titleList[i] 
    replace = replace.strip("'")
    titleList[i] = replace

tmpList =[] # temporary list variable for list item changes
for i in range(0,length):
    # i am assuming that all file names have `.md` at the end.
    # so this `for` loop converting each string item to list then
    # removes the last three characters from it. the last three character is `.md`
    replace = titleList[i] 
    tmpList = list(replace)
    tmpList = tmpList[0:-3]
    replace = "".join(tmpList)
    titleList[i] = replace
    # it might not be a good solution for removing the characthers but
    # i couldn't use rstrip properly. and also it was all about fun.

for i in range(0,length):
    # eventually we can build internal page link from this altered file names.
    replace = titleList[i] 
    replace = replace.strip()
    replace = "[[" + replace + "]]" 
    titleList[i] = replace

for i in titleList:
    # then writing the final list to output file.
    output.write(i + "\n")
