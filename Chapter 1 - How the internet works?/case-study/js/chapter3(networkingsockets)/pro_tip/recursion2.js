
// let t = [];
// Author: John Royce C. Punay
// Date: March 11, 2020 5:38 PM


// (function royce(n, arr) {
//     while (n !== 0) {
//         n = n - 1;
//         let collections = arr[n];
//         for (let item in collections) {
//             console.log(collections[item]);
//             if (collections[item] && typeof collections[item] === "object") {
//                 console.log(collections[item]);
//                 // royce((Object.keys(collections.item).length + n) - 1, arr);
//             } else {
//                 console.log('else', collections[item]);
//             }
//         }
//         // royce(n, arr);
//         break;
//     }
// })([1, 2, 3, 4, 5].length, [{ name: 'apple' }, { fruit: 'mango', t3: { t5: { t6: { t7: 100 } } } }, 3, { t2: 'avocado' }, { o9: 'melon', o1: { a: 'a' } }]);


let items = [{ name: 'apple' }, { fruit: 'mango', t3: { t5: { t6: { t7: 100 } } } }, 3, { t2: 'avocado' }, { o9: 'melon', o1: { a: 'a' } }]
let c = [];
const recursive = (obj) => {
    for (let k in obj) {
        if (obj[k] && typeof obj[k] === 'object') {
            // parent
            recursive(obj[k])
        } else {
            // child
            c.push(obj[k])
        }
    }
}
let i = 0;
do {
    recursive(items[i])
    i++;
} while (i < items.length);