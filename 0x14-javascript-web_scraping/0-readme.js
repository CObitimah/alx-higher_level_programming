#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

if (!filePath) {
  console.error('Error: No file path provided. Usage: node script.js <file-path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(`Error reading file: ${err.message}`);
    process.exit(1);
  } else {
    console.log(data);
  }
});
