#!/usr/bin/node
// Executes a function x times.

exports.addMeMaybe = function (number, theFunction) {
  let incrementedNumber = number + 1;
  theFunction(incrementedNumber);
};

