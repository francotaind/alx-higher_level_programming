#!/usr/bin/node
// Check if the first and second arguments are passed
if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
    console.log(process.argv[2] + " is " + process.argv[3]); // Print both arguments in the specified format
} else if (process.argv[2] !== undefined && process.argv[3] === undefined) {
    console.log(process.argv[2] + " is undefined"); // Print the first argument followed by "is undefined" if only one argument is passed
} else {
    console.log("undefined is undefined"); // Print "undefined is undefined" if no arguments are passed
}
