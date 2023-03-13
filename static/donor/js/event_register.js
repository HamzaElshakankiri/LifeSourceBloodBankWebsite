var firstname = document.getElementById("firstName");
var lastname = document.getElementById("lastName");
var pc = document.getElementById("pc");
var mail = document.getElementById("yourEmail");
var username = document.getElementById("yourUsername");
var dob = document.getElementById("dob");
var pwd = document.getElementById("yourPassword");
var cpwd = document.getElementById("yourCPassword");
var contact_phone = document.getElementById("yourContact");
var height = document.getElementById("yourHeight");
var weight = document.getElementById("yourWeight");
var emergency_contact_name = document.getElementById("emergencyContact");
var emergency_contact_phone = document.getElementById("emergencyNumber");


firstname.addEventListener("blur", firstNameEVHandler);
lastname.addEventListener("blur", lastNameEVHandler);
pc.addEventListener("blur", pcEVHandler);
mail.addEventListener("blur", EmailEVHandler);
username.addEventListener("blur",UsernameEVHandler);
dob.addEventListener("blur", dobEVHandler);
pwd.addEventListener("blur", pwdEVHandler);
cpwd.addEventListener("blur", cpwdHandler);
contact_phone.addEventListener("blur", contactEVHandler);
height.addEventListener("blur", heightEVHandler);
weight.addEventListener("blur", weightEVHandler);
emergency_contact_name.addEventListener("blur", enameEVHandler);
emergency_contact_phone.addEventListener("blur", econtactVHandler);

var form = document.getElementById("signup-form");
form.addEventListener("submit", validateSignup);



var form2 = document.getElementById("login-form");
form2.addEventListener("submit", validateLogin,false);
