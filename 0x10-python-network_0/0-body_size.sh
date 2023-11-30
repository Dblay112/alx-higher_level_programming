#!/bin/bash
# Get the byte size of the HTTP response header of a URL.
curl -s "$1" | wc -c
