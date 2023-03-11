function validateUName(name) {
	let nameRegEx = /^[a-zA-Z0-9_]+$/;

	if (nameRegEx.test(name))
		return true;
	else
		return false;
}
function validatepc(dob) {
	let pcEx = /^[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d$/i;

	if (pcEx.test(dob))
		return true;
	else
		return false;
}
function validateEmail(em) {

	let unameRegEx = /^[a-zA-Z0-9.!#$%&'+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;
	if (unameRegEx.test(em))
		return true;
	else
		return false;
}
function validateDOB(dob) {
	let dobRegEx = /^\d{4}[-]\d{2}[-]\d{2}$/;

	if (dobRegEx.test(dob))
		return true;
	else
		return false;
}
function dobEligible(b) {

	var today = new Date();
	var nowyear = today.getFullYear();
	var nowmonth = today.getMonth();
	var nowday = today.getDate();

	var birth = new Date(b);

	var birthyear = birth.getFullYear();
	var birthmonth = birth.getMonth();
	var birthday = birth.getDate();

	var age = nowyear - birthyear;
	var age_month = nowmonth - birthmonth;
	var age_day = nowday - birthday;

	if ((age == 18 && age_month <= 0 && age_day <= 0) || age < 18) {
		return false;
	}
	else
		return true;
}
function validatePWD(pwd) {

	if (pwd.length >= 8)
		return true;
	else
		return false;
}
function validateAvatar(avatar) {

	let avatarRegEx = /^[^\n]+.[a-zA-Z]{3,4}$/;

	if (avatarRegEx.test(avatar))
		return true;
	else
		return false;

}


//Signup function ....


function validateSignup(event) {

	let tfname = document.getElementById("name");
	let tlname = document.getElementById("lastName");
	let tpc = document.getElementById("pc");
	let tdob = document.getElementById("dob");
	let tem = document.getElementById("yourEmail");
	let tpwd = document.getElementById("yourPassword");
	let term = document.getElementById("acceptTerms");

	let formIsValid = true;

   let btfname = firstNameHandler(document.getElementById("name")); 
   let btlname = lastNameHandler(tlname);
   let btpc = pcHandler(tpc);
   let btdob = dobHandler(tdob);
   let btem = EmailHandler(tem);
   let btpwd = pwdHandler(tpwd);

   if (term.checked == false){
		term.classList.add("class", "red");
		document.getElementById("invalidTerms").textContent= "You must agree before submitting.";
		formIsValid = false;
   }
   else{
		term.classList.remove("class", "red");
		document.getElementById("invalidTerms").textContent= "";
		formIsValid = true;
   }

   if (btfname == false || btlname == false || btpc == false || btdob == false || btem == false || btpwd==false) 
		formIsValid = false;
		console.log("atleast one is false i see");

	if (!formIsValid) {
		event.preventDefault();
		console.log ("Something invalid")
	} else {
		console.log("Validation successful, sending data to the server");
	}
}
function firstNameEVHandler(event){
	let t = event.target;
	return firstNameHandler(t);
}

function firstNameHandler(fname) {

	if(fname.value == null || fname.value ==""){
		fname.classList.add("class", "red");
		document.getElementById("invalidfirstName").classList.remove("hidden");
		document.getElementById("invalidfirstName").textContent= "Name cannot be empty!";
		return false;
	}
	else if (!validateUName(fname.value)) {
		fname.classList.add("class", "red");
		document.getElementById("invalidfirstName").classList.remove("hidden");
		document.getElementById("invalidfirstName").textContent= "Firstname cannot use Non-word character or space !";
		return false;
	}
	else {

		fname.classList.remove("class", "red");
		document.getElementById("invalidfirstName").classList.add("hidden");
		document.getElementById("invalidfirstName").textContent= "";
		return true;
	}
}

function lastNameEVHandler(event){
	let t = event.target;
	return lastNameHandler(t);
}
function lastNameHandler(lname) {

	if(lname.value == null || lname.value ==""){
		lname.classList.add("class", "red")
		document.getElementById("invalidlastName").classList.remove("hidden");
		document.getElementById("invalidlastName").textContent= "Lastname cannot be empty !";
		return false;
	}
	else if (!validateUName(lname.value)) {
		lname.classList.add("class", "red")
		document.getElementById("invalidlastName").classList.remove("hidden");
		document.getElementById("invalidlastName").textContent= "Lastname cannot use Non-word character or space !";
		return false;
	}
	else {

		lname.classList.remove("class", "red")
		document.getElementById("invalidlastName").classList.add("hidden");
		document.getElementById("invalidlastName").textContent= "";
		return true;
	}
}
function pcEVHandler(event) {
	let t = event.target;
	return pcHandler(t);
}

function pcHandler(pc) {

	if (pc.value == null || pc.value == "") {
		pc.classList.add("class", "red")
		document.getElementById("invalidpc").classList.remove("hidden");
		document.getElementById("invalidpc").textContent= "Postal code cannot be empty !";
		return false;	
	}
	else if (!validatepc(pc.value)) {
		pc.classList.add("class", "red")
		document.getElementById("invalidpc").classList.remove("hidden");
		document.getElementById("invalidpc").textContent= "Invalid Postal Code !";
		return false;
	}
	else {
		pc.classList.remove("class", "red")
		document.getElementById("invalidpc").classList.add("hidden");
		document.getElementById("invalidpc").textContent= "";
		return true;
	}
}
function EmailEVHandler(event) {
	let t = event.target;
	return EmailHandler(t);
}

function EmailHandler(mail) {
	
	if(mail.value == null || mail.value ==""){
		mail.classList.add("class", "red")
		document.getElementById("invalidEmail").classList.remove("hidden");
		document.getElementById("invalidEmail").textContent= "Email cannot be empty !";
		return false;
	}
	else if (!validateEmail(mail.value)) {
		mail.classList.add("class", "red")
		document.getElementById("invalidEmail").classList.remove("hidden");
		document.getElementById("invalidEmail").textContent= "Invalid Email !";
		return false;
	}
	else {
		mail.classList.remove("class", "red")
		document.getElementById("invalidEmail").classList.add("hidden");
		document.getElementById("invalidEmail").textContent= "";
		return true;
	}
}
function dobEVHandler(event) {
	let t = event.target;
	return dobHandler(t);
}
function dobHandler(dob) {
	if (!validateDOB(dob.value)) {
		dob.classList.add("class", "red")
		document.getElementById("invalidDob").classList.remove("hidden");
		document.getElementById("invalidDob").textContent= "Invalid Date of Birth !";
		return false;
	}
	else if (!dobEligible(dob.value)) {
		dob.classList.add("class", "red")
		document.getElementById("invalidDob").classList.remove("hidden");
		document.getElementById("invalidDob").textContent= "Cannot register if not over 18 years !";
		return false;
	}
	else {
		dob.classList.remove("class", "red")
		document.getElementById("invalidDob").classList.add("hidden");
		document.getElementById("invalidDob").textContent= "";
		return true;
	}
}



function pwdEVHandler(event) {
	let t = event.target;
	return pwdHandler(t);
}
function pwdHandler(pwd) {

	if (pwd.value == null || pwd.value == "") {
		pwd.classList.add("class", "red")
		document.getElementById("invalidPwd").classList.remove("hidden");
		document.getElementById("invalidPwd").textContent= "Password cannot be empty !";
		return false;
	}
	else if ( (pwd.value.length)<8) {
		pwd.classList.add("class", "red")
		document.getElementById("invalidPwd").classList.remove("hidden");
		document.getElementById("invalidPwd").textContent= "Password must be atleast 8 characters long !";
		return false;
	}
	else if(!(/^(?=.*\d)(?=.*[a-zA-Z])[a-zA-Z0-9]{7,}$/.test(pwd.value))){
		pwd.classList.add("class", "red")
		document.getElementById("invalidPwd").classList.remove("hidden");
		document.getElementById("invalidPwd").textContent= "Invalid Password. Please follow the format !";
		return false;
	}
	else {
		pwd.classList.remove("class", "red")
		document.getElementById("invalidPwd").classList.add("hidden");
		document.getElementById("invalidPwd").textContent= "";
		return true;
	}
}
function cpwdHandler(event) {
	let pwd = document.getElementById("yourPassword");
	let cpwd = event.target;
	if (pwd.value !== cpwd.value) {
		cpwd.classList.add("class", "red")
		document.getElementById("invalidCpwd").classList.remove("hidden");
		document.getElementById("invalidCpwd").textContent= "Your passwords: " + pwd.value + " and " + cpwd.value + " do not match";
		return false;
	}
	else {
		cpwd.classList.remove("class", "red")
		document.getElementById("invalidCpwd").classList.add("hidden");
		document.getElementById("invalidCpwd").textContent= "";
		return true;
	}
}
/*
function avatarHandler(event) {
	let avatar = event.target;
	if (!validateAvatar(avatar.value)) {
		avatar.classList.add("class", "red")
		document.getElementById("text-avatar").classList.remove("hidden");
		console.log("'" + avatar.value + "' is not a valid avatar");
		flag = false;
	}
	else {

		avatar.classList.remove("class", "red")
		document.getElementById("text-avatar").classList.add("hidden");
	}
}*/


//login function


function validateLogin(event){

	let em = document.getElementById("Email");
	let pwd = document.getElementById("Password");
	let formIsValid = true;

	if (em.value == null || em.value == "") {
		em.classList.add("class", "red")
		document.getElementById("invalid-email").classList.remove("hidden");
		document.getElementById("invalid-email").textContent = "Email cannot be empty !";
		formIsValid = false;

	}
	else if (!validateEmail(em.value)) {

		em.classList.add("class", "red")
		document.getElementById("invalid-email").classList.remove("hidden");
		document.getElementById("invalid-email").textContent = "Email address wrong format! example: username@somewhere.sth";
		formIsValid = false;
	}
	else {
		em.classList.remove("class", "red")
		document.getElementById("invalid-email").classList.add("hidden");
		document.getElementById("invalid-email").textContent = "";

	}

	if (pwd.value == null || pwd.value == "") {
		pwd.classList.add("class", "red")
		document.getElementById("invalid-password").classList.remove("hidden");
		document.getElementById("invalid-password").textContent= "Password cannot be empty !";
		formIsValid = false;

	}
	else if (!validatePWD(pwd.value)) {

		pwd.classList.add("class", "red")
		document.getElementById("invalid-password").classList.remove("hidden");
		document.getElementById("invalid-password").textContent= "Password must be atleast 8 characters or more !";
		formIsValid = false;
	}
	else if (/\s/.test(pwd.value)){
		pwd.classList.add("class", "red")
		document.getElementById("invalid-password").classList.remove("hidden");
		document.getElementById("invalid-password").textContent= "Password cannot contain spaces !";
		formIsValid = false;
	}
	else {

		pwd.classList.remove("class", "red")
		document.getElementById("invalid-password").classList.add("hidden");
		document.getElementById("invalid-password").textContent= "";
	}

	if (!formIsValid) {
		event.preventDefault();
	} else {
		console.log("Validation successful, sending data to the server");
	}
}

