

let str1 = prompt("A sentance with not and bad in it")


let not1 = str1.indexOf("not")
let bad1 = str1.indexOf("bad")


if (not1 > -1 && bad1 > -1 && bad1 > not1 ) { 
	console.log(str1.substr(0, not1) + "good");

}


