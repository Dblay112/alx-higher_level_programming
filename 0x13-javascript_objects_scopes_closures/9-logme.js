#!/usr/bin/node
exports.logMe = function (item) {
  if (this.arg === undefined) {
    this.arg = 0;
  }
  console.log(`${this.arg}: ${item}`);
  this.arg++;
};
