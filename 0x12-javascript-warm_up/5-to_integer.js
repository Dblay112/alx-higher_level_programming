#!/usr/bin/node
let arg = process.argv[2];
if (Number.isNaN(parseInt(arg))) {
    console.log('Not a number');
} else {
    console.log('My number:', parseInt(arg));
}
