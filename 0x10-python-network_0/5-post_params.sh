#!/bin/bash
# Bash scripts that sends a POST request to a URL 
curl -s -X POST -d "subject=I will always be here for PLD&email=test@gmail.com" "$1"
