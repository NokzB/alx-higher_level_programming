#!/usr/bin/node

// Script to print <My Number: "number"> if first arg can be converted to int.

if (!isNaN(process.argv[2])) {
  console.log('My number:', parseInt(process.argv[2]));
} else {
  console.log('Not a Number');
}
