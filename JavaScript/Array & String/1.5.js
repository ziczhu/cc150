#!/usr/bin/env node

/************************************
              cc150
    1.5 compress string

************************************/


function compress(string) {

	var newSize = countCompression(string);

	if (string.length <= newSize) {
		return string;
	}

	var first = string.charAt(0);
	var count = 1;
	var newString = new Buffer(newSize);

	for (var i = 1, j = string.length, k = 0; i < j; i++) {
		if (string.charAt(i) === first) {
			count++;
		} else {
			newString.write((first + count), k);
			first = string.charAt(i);
			k += 1 + count.toString().length;;
			count = 1;
		}
	}
	newString.write((first + count), k);

	return newString.toString();
}


function countCompression(string) {
	var first = string.charAt(0);
	var count = 1;
	var size = 0;
	for (var i = 1, j = string.length; i < j; i++) {
		if (string.charAt(i) === first) {
			count++;
		} else {
			first = string.charAt(i);
			size += 1 + count.toString().length;
			count = 1;
		}
	}
	size += 1 + count.toString().length;
	return size;
}


var args = process.argv.slice(0, 3);

console.log(compress(args[2]));
