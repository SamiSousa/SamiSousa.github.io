

function multiply(num1, num2){
	var result = num1 * num2;
	return result;
}


var myHeading = document.querySelector('h1');

myHeading.textContent = "Hello world";

myHeading.onclick = function(){
	alert("Ouch! Stop poking me!");
}

alert("6 times 7 is " + multiply(6, 7));