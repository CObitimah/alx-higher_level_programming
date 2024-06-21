#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.error('Error: Missing arguments. Usage: node script.js <file-path> <content>');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(`Error writing to file: ${err.message}`);
    process.exit(1);
  } else {
    console.log('File has been written successfully.');
  }
});
