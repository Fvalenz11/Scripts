#make a Bash script that takes input a text file. Each line of the text is an IP. Ping each line and save the results in a new file.
#use the following command to ping a machine
#ping -c 1 <ip address>

#! /bin/bash

echo "enter the name of the file to be processed"
read file
echo "enter the name of the file to be saved"
read filename

while read -r line
do
    ping -c 1 "$line" > temp.txt
    if [ "$?" -eq 0 ]; then
        echo "machine $line is up" >> "$filename"
    else
        echo "machine $line is down" >> "$filename"
    fi
done < "$file"

rm temp.txt
