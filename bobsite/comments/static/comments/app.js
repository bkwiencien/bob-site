function checkEmail() {
	var commento = document.getElementById("id_comment").value;
	var emailo =  document.getElementById("id_your_name").value;
	console.log('commento = ' + commento)
	if (commento.length == 0) {
		alert("comment cannot be blank")
		return;
	}
}