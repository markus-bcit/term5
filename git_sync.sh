#!/bin/bash

echo -n "Enter commit message: "
read message

git pull origin main
git add .

timestamp=$(date "+%Y-%m-%d %H:%M:%S")
git commit -m "$message // $timestamp"

git push origin main

echo -n "Press Enter to exit..."
read
