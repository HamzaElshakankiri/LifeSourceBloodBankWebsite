var firstname = document.getElementById("donor_first_name");
var lastname = document.getElementById("donor_last_name");
var dob = document.getElementById("donor_birthday");
var pc = document.getElementById("donor_postal");
var contact_phone = document.getElementById("donor_contact_phone");
var height = document.getElementById("donor_height");
var weight = document.getElementById("donor_weight");
var emergency_contact_name = document.getElementById("emergency_contact_name");
var emergency_contact_phone = document.getElementById("emergency_contact_phone");


firstname.addEventListener("blur", firstNameEVHandler);
lastname.addEventListener("blur", lastNameEVHandler);
dob.addEventListener("blur", dobEVHandler);
pc.addEventListener("blur", pcEVHandler);
contact_phone.addEventListener("blur", contactEVHandler);
height.addEventListener("blur", heightEVHandler);
weight.addEventListener("blur", weightEVHandler);
emergency_contact_name.addEventListener("blur", enameEVHandler);
emergency_contact_phone.addEventListener("blur", econtactVHandler);


var form = document.getElementById("edit-form");
form.addEventListener("submit", validateEdit);



