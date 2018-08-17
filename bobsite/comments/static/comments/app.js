function checkEmail() {
	var commento = document.getElementById("id_comment").value;
	var emailo =  document.getElementById("id_your_name").value;
	console.log('emailo = ' + emailo)
	if (commento.length == 0) {
		alert("comment cannot be blank")
		return;
	}
    var res = validateEmail(emailo)
    if (!res) {
    	alert('email invalid')
    	return;
    }
    $.post("/comments/getcomment/",
    {
        comment: commento,
        your_name:  emailo,
    },
    function(data, status){
    	console.log(data)
        //window.location.href = data;
        document.write(data)
    });

}
function validateEmail(email) {
  var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(email);
}