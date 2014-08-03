#!/usr/bin/env node

/************************************
              cc150
    1.4 replace spaces

************************************/


function replaceSpaces(string) {

    var spaceCount = 0;

    for (var i = 0, j = string.length; i < j; i++) {
        if (string.charAt(i) === ' ') {
            spaceCount++;
        }
    }

    var stringBuffer = new Buffer(string.length + spaceCount * 2);

    for (var i = 0, k = 0, j = string.length; i < j; i++) {
        if (string.charAt(i) === ' ') {
            stringBuffer.write('%20', k);
            k += 3;
        } else {
            stringBuffer.write(string.charAt(i), k);
            k += 1;
        }
    }

    return stringBuffer.toString();

}

var args = process.argv.slice(0, 3);

console.log(replaceSpaces(args[2]));