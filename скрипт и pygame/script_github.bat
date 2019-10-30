@echo off 
title adding new repository on github

set /p url="Enter repository url: "

git init
git add .
git commit -m "init"
git remote add origin %url%
git push -u origin --all

if ERRORLEVEL 1 git fetch

echo End.
timeout /t 10 /nobreak