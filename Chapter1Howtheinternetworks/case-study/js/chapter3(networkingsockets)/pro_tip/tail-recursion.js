'use strict';
function factorial(n, total = 1) {
    // console.trace();
    if (n === 0) {
        return total;
    }
    // proper tail call
    console.log('n', n);
    return factorial(n - 1, n * total);
}
factorial(100);

// https://hackernoon.com/es6-tail-call-optimization-43f545d2f68b
// https://medium.com/javascript-in-plain-english/javascript-optimizations-tail-call-optimization-tco-471b4f8e4f37
// Before applying any optimization you have to understand if your code is running on a critical path. If it’s not on a critical path, chances are your optimizations are not worth much and premature optimization in general is a bad idea.
// optimise algorithm
// a tail call is a function call that appears at the tail of another function, such that after the call finishes, there’s nothing left to do.