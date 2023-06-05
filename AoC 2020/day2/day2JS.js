const fs = require('fs')

fs.readFile('input2.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    const numbers = data.trim().split('\r\n');
    let valid_password_count = 0
    let valid_password_count_2 = 0;
    for (let i = 0; i < numbers.length; i++) {
      const values = numbers[i].split(' '); // split by space
      const range = values[0].split('-'); // split range by dash
      const min = parseInt(range[0]);
      const max = parseInt(range[1]);
      const char = values[1][0]; // get first character of second value
      const password = values[2];
      let count = 0;

      for(let j = 0; j < password.length; j++) {
          if (password[j] === char) {
              count++;
          }
      }
      if (password[min - 1] === char ^ password[max - 1] != char) {
          valid_password_count_2++;
      }
      if(min <= count && count <= max){
          valid_password_count++
      }
      console.log(min, max, char, password);
    }
    console.log("Answer to Part 1:" + valid_password_count)
    console.log("Answer to Part 2:" + valid_password_count_2)
    /*This one is somehow coming out wrong -> needs to be fixed later */
})