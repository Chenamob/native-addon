// import native addon
const addonGreet = require('bindings')('greet');

// expose module API
exports.hello = addonGreet.greetHello;

console.log("hello");
console.log(exports.hello("yyyy"));
console.log(addonGreet.greetHello("zzzzz"));