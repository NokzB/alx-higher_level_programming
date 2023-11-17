#!/usr/bin/node

// Script that prints a square, "X".

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i += 1) {
    let line = '';
    for (let j = 0; i < size; j += 1) line += 'X';
    console.log(line);
  }
}
