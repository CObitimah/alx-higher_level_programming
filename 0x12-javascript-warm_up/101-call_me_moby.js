#!/usr/bin/node
// Executes a function x times.

exports.callMeMoby = function (x, theFunction) {
  for (let counter = 0; counter < x; counter++) {
    theFunction();
  }
};
