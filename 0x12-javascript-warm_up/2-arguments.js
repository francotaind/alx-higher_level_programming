#!/usr/bin/node
// Check if any arguments are passed
if (process.argv[2] === undefined) {
  console.log('No argument'); // Print the first argument
} else if (process.argv[3] === undefined) {
  console.log('Argument found');
} else {
  console.log('Arguments found'); // Print if no argument is passed
}
