#!/bin/bash

# DESCRIPTION
# SCRIPT CHECKER LOGS OF WEB SERVER, CREATE LOGS

# FOR USE SCRIPT, NEED WRITE PATH THIS SCRIPT BELOW. FOR RUN IN CONSOLE NEED CHANGE CURRENT DIRECTORY IN CONSOLE AND NEED TO REMOVE STRING BELOW (cd /c/Users/dev/Desktop/dir1)
# CHANGE PATH FOR THIS SCRIPT AND LOGS (my windows path for example).
cd /c/Users/dev/Desktop/dir1

# CREATE FILE ip_and_quantity.log (top 10 ip - quantity)
awk '{print $1}' log.log | sort | uniq -c | sort -r | head > temp.log
awk '{temp_var=$1; $1=$2; $2=" - "temp_var} 1' temp.log > ip_and_quantity.log

# CREAT FILE links_and_quantity.log (top 10 links - quantity). NEED CHANGE PATH FOR log.log IN GREP
grep -o 'http://[a-zA-Z.\d-]*' log.log | sort | uniq -c | sort -r | head > temp.log
awk '{temp_var=$1; $1=$2; $2=" - "temp_var} 1' temp.log > links_and_quantity.log

echo '\nQuantity||Requests' > kolichestvo_usp_bash.log
awk '{print $9}' log.log | sort | uniq -c | sort -r | head >> kolichestvo_usp_bash.log

rm temp.log