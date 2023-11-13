#!/usr/bin/node
const argNum = process.argv.length
if (argNum === 2) {
	console.log('No Argument');
}
else if (argNum === 3) {
	console.log('Argument found');
}
else {
	console.log('Arguments found');
}
