const readline = require('readline');

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on('line', (input) => {
	console.log(`Received: ${input}`);
});

// rl.question('What is your name? ', (name) => {
//   console.log(`Your name is ${name}`);
//   rl.close();
// });

// SIGINT is the signal for the interrupted signal under nodejs event loop
rl.on('SIGINT', () => {
	rl.question('Are you sure you want to exit? ', (answer) => {
		if (answer.match(/^y(es)?$/i)) rl.close();
	});
});


// https://nodejs.org/api/readline.html#readline_readline