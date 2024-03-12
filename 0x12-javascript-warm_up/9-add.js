#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  const num1 = parseInt(a);
  const num2 = parseInt(b);
  return num1 + num2;
}
const firstnum = parseInt(process.argv[2]);
const secondnum = parseInt(process.argv[3]);

const sum = add(firstnum, secondnum);
console.log(sum);
