#!/usr/bin/env node

/************************************
              cc150
    1.3 judge anagram string
    Assume the string is ASCII
    No space or capital

************************************/


function permutation(string1, string2) {

    var string1 = string1.replace(/\s+/g, '').toLowerCase();
    var string2 = string2.replace(/\s+/g, '').toLowerCase();

    if (string1.length !== string2.length) {
        return false
    }

    var charSet = Array.apply(null, new Array(128))
                  .map(Number.prototype.valueOf, 0);

    for (i = 0, j = string1.length; i < j; i++) {
        var charVal = string1.charCodeAt(i);
        ++charSet[charVal];
    }

    for (i = 0, j = string2.length; i < j; i++) {
        var charVal = string2.charCodeAt(i);
        if (--charSet[charVal] < 0) {
            return false;
        }
    }

    return true;
}

var args = process.argv.slice(0, 4);

console.log(permutation(args[2], args[3]));