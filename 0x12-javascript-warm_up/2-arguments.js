#!/usr/bin/node
// Check if any arguments are passed
if (process.argv[2] !== undefined) {
  console.log(process.argv[2]); // Print the first argument
} else {
  console.log('No argument'); // Print if no argument is passed
}
