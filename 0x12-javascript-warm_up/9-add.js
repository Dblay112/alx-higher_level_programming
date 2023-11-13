#!/usr/bin/node
function add(a, b) {
    const result = parseInt(a) + parseInt(b);
    console.log(result);
}

const argNum = process.argv.slice(2);

if (argNum.length === 2) {
    add(argNum[0], argNum[1]);
} else {
    console.log('NaN');
}
