var firstname = document.getElementById("firstName");
var lastname = document.getElementById("lastName");
var pc = document.getElementById("pc");
var mail = document.getElementById("yourEmail");
var dob = document.getElementById("dob");
var pwd = document.getElementById("yourPassword");
var cpwd = document.getElementById("yourCPassword");


firstname.addEventListener("blur", firstNameEVHandler);
lastname.addEventListener("blur", lastNameEVHandler);
pc.addEventListener("blur", pcEVHandler);
mail.addEventListener("blur", EmailEVHandler);
dob.addEventListener("blur", dobEVHandler);
pwd.addEventListener("blur", pwdEVHandler);
cpwd.addEventListener("blur", cpwdHandler);

var form = document.getElementById("signup-form");
form.addEventListener("submit", validateSignup);



var form2 = document.getElementById("login-form");
form2.addEventListener("submit", validateLogin,false);
