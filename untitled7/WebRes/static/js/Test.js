console.log("HALO 1!");


function sum1(a,b) {
    return a+b
}


console.log(sum1(3,4));


console.log("HALO 2!");


function sum2(a) {
    return a*4
}


console.log(sum2(3));


console.log("HALO 3!");


function sum3(a,b,c) {
    return (a+b+c)/3
}


console.log(sum3(3,5,7));


console.log("HALO 4!");


function sum4() {
    return 7
}


console.log(sum4());


console.log("HALO 5!");


function sum5(a) {
    return a%5
}

console.log(sum5(16));


console.log("HALO 7!");

function sum7(a){
    x = prompt('Введите число');
    if(x == 34){
        return ("Kir")
    } else{
        return ("Olga")
    }

}

console.log(sum7());


function sum8(z,y){
    z = prompt('Введите число');
    y = prompt('Введите число');
    z = parseInt(z, 10);
    y = parseInt(y, 10);

    if(z+y == 5){
        return 5/2
    } else{
        return z+y
    }

}

console.log(sum8());


console.log("HALO 9!");

function sum9(a) {
    x = prompt('Введите строку');
    if (x.length <= 5) {
        return x
    } else {
        return ("Я устал")
    }
}
console.log(sum9());




