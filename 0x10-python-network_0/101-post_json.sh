#!/bin/bash
# a JSON POST request to a given URL with a given JSON file
curl -s -d @"$2" -H "Content-Type: application/json" "$1" -X POST
