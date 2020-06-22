let str1 = "the cake is not so bad!" 


let not1 = str1.indexOf("not")
let bad1 = str1.indexOf("bad")



if (not1 > -1 && bad1 > -1 && bad1 > not1 ) { 
	console.log(str1.substr(0, not1) + "good");

}


