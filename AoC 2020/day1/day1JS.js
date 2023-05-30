const fs = require('fs')

fs.readFile('input1.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    const numbers = data.trim().split('\n').map(Number);
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            if(numbers[i] + numbers[j] === 2020){
                console.log(numbers[i] + " + " + numbers[j] + " = 2020")
                console.log("Product: " + numbers[i]*numbers[j])
            }
        }
    }

    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            for (let k = j+1; k < numbers.length; k++) {
                if(numbers[i] + numbers[j] + numbers[k] === 2020){
                    console.log(numbers[i] + " + " + numbers[j]  + " + " + numbers[k] + " = 2020")
                    console.log("Product: " + numbers[i]*numbers[j]*numbers[k])
                }
            }
        }
    }
})