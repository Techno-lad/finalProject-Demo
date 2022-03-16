function sumInput() {
    let numbers0 = [];
    let numbers = [];
    var i = 0;
    var counter = 0;
    alert('enter value types as instructed,when done clear input and press enter');
    while (true) {
        let value0 = prompt("Grade:", 0);
        let value = prompt("Weighting:", 0);
        // should we cancel?
        if (value0 === "" || value0 === null || !isFinite(value0))
            break;
        numbers0.push(+value0);
        numbers.push(+value);
        counter++;
    }
    let sum = 0;
    for (i = 0; i < counter; i++) {
        sum += ((numbers0[i] / 100) * (numbers[i] / 100))*100;
    }
    alert(sum+'%');
}


