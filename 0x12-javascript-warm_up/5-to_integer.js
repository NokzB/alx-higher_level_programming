#!/usr/bin/node

// Script to print <My Number: "number"> if first arg can be converted to int.

const input = process.argv[2];

if (!isNaN(parseInt(input))) {
  console.log('My number:', parseInt(input));
} else {
  console.log('Not a Number');
}
