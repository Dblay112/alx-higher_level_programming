#!/usr/bin/node
exports.esrever = function (list) {
  const li = [];
  for (let x = list.length - 1; x >= 0; x--) {
    li.push(list[x]);
  }
  return li;
};
