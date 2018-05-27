#!/usr/bin/env bash

# usr input for file name
echo What is the dir name? 

# writes var $dirname
read dirname

#user input for file name
echo What is the file name?

#wites var $filename
read filename

#commands to execute

mkdir -p "/home/student/mycode/$dirname/" 
touch "/home/student/mycode/$dirname/$filename" 
chmod u+x "/home/student/mycode/$dirname/$filename"
leafpad "/home/student/mycode/$dirname/$filename" &