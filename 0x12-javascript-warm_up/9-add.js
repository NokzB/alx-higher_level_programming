#!/usr/bin/node

// Script that adds two integers provided as command line args

function add (a, b) {
  return a + b;
}
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
