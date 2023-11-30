#!/bin/bash
# a GET request to a given URL and display the response status code.
curl -w "%{http_code}" "$1" -so /dev/null
