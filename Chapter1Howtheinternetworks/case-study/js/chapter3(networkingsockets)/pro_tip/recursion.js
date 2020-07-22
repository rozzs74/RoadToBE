(function royce(n) {
    while (n !== 0) {
        console.log('I am recursively running' + 'count=' + n);
        royce(n - 1)
        break;
    }
})(50);
// recursion is not recommended for big items.