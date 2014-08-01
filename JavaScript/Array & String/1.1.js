#!/usr/bin/env node

/************************************
              cc150
  1.1 judge unique chars in a string
  Assume the string is ASCII

************************************/


function isUniqueChars (str) {

    var str = str.replace(/\s+/g, '');

    if (str.length > 256) return false;

    var charSet = Array.apply(null, new Array(256))
                  .map(Boolean.prototype.valueOf, false);

    for (var i = 0, j = str.length; i < j; i++) {
        var charVal = str.charCodeAt(i);
        if (charSet[charVal]) {
            return false
        }
        charSet[charVal] = true
    }

    return true
}

var args = process.argv.slice(0, 3);

console.log(isUniqueChars(args[2]));