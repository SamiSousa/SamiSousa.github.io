

var myImage = document.querySelector('img');

myImage.onclick = function(){
	var mySrc = myImage.getAttribute('src');
	if (mySrc === 'img/smile.png'){
		myImage.setAttribute ('src', 'img/ProfessionalCandid_large.png');
	} else {
		myImage.setAttribute('src', 'img/smile.png');
	}
}

