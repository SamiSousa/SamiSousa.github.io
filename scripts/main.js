

var myImage = document.querySelector('img');

myImage.onclick = function(){
	var mySrc = myImage.getAttribute('src');
	if (mySrc === 'img/smile.png'){
		myImage.setAttribute ('src', 'img/ProfessionalCandid_large.png');
	} else {
		myImage.setAttribute('src', 'img/smile.png');
	}
}



var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

function setUserName(){
	var myName = prompt('Please enter your name.');
	localStorage.setItem('name', myName);
	myHeading.textContent = 'You\'re cool, ' + myName;
}

if (!localStorage.getItem('name')){
	setUserName();
}else {

	// username set, so load it
	var storedName = localStorage.getItem('name');
	myHeading.textContent = 'You\'re cool, ' + storedName;
}

// on clicking button, prompt user for new username
myButton.onclick = function(){
	setUserName();
}