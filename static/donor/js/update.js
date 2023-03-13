function validateUName(name) {
	let nameRegEx = /^[a-zA-Z0-9_]+$/;

	if (nameRegEx.test(name))
		return true;
	else
		return false;
}

function validateContact(contact_no) {
	let numberRegEx = /^\d{3}-\d{3}-\d{4}$/;

	if (nameRegEx.test(contact_no))
		return true;
	else
		return false;
}


function validateNumber(num) {
	let numRegEx = /^[0-9]+$/;

	if (numRegEx.test(num))
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


//Edit function ....


function validateEdit(event) {

	let tfname = document.getElementById("donor_first_name");
	let tlname = document.getElementById("donor_last_name");
	let tpc = document.getElementById("donor_postal");
	let tdob = document.getElementById("donor_birthday");
    let tcontact_phone = document.getElementById("donor_contact_phone");
    let theight = document.getElementById("donor_height");
    let tweight = document.getElementById("donor_weight");
    let temergency_contact_name = document.getElementById("emergency_contact_name");
    let temergency_contact_phone = document.getElementById("emergency_contact_phone");


	let formIsValid = true;

   let btfname = firstNameHandler(document.getElementById("donor_first_name")); 
   let btlname = lastNameHandler(tlname);
   let btpc = pcHandler(tpc);
   let btdob = dobHandler(tdob);
   let btcontact_phone = contactEVHandler(tcontact_phone);
   let btheight = heightEVHandler(theight);
   let btweight = weightEVHandler(tweight);
   let btemergency_contact_name = enameEVHandler(temergency_contact_name);
   let btemergency_contact_phone = contactEVHandler(temergency_contact_phone);

   

   if (btfname == false || btlname == false || btpc == false || btdob == false || btcontact_phone == false || btheight == false || btweight == false ||btemergency_contact_name == false || btemergency_contact_phone == false) 
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
		document.querySelector('#myBtn').disabled = true;
		return false;
	}
	else {

		fname.classList.remove("class", "red");
		document.getElementById("invalidfirstName").classList.add("hidden");
		document.getElementById("invalidfirstName").textContent= "";
		document.querySelector('#myBtn').disabled = false;
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
		document.querySelector('#myBtn').disabled = true;
		return false;
	}
	else {

		lname.classList.remove("class", "red")
		document.getElementById("invalidlastName").classList.add("hidden");
		document.getElementById("invalidlastName").textContent= "";
		document.querySelector('#myBtn').disabled = false;
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
		document.querySelector('#myBtn').disabled = true;
		return false;
	}
	else {
		pc.classList.remove("class", "red")
		document.getElementById("invalidpc").classList.add("hidden");
		document.getElementById("invalidpc").textContent= "";
		document.querySelector('#myBtn').disabled = false;
		return true;
	}
}
function EmailEVHandler(event) {
	let t = event.target;
	return EmailHandler(t);
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
		document.querySelector('#myBtn').disabled = true;
		return false;
	}
	else if (!dobEligible(dob.value)) {
		dob.classList.add("class", "red")
		document.getElementById("invalidDob").classList.remove("hidden");
		document.getElementById("invalidDob").textContent= "Cannot register if not over 18 years !";
		document.querySelector('#myBtn').disabled = true;
		return false;
	}
	else {
		dob.classList.remove("class", "red")
		document.getElementById("invalidDob").classList.add("hidden");
		document.getElementById("invalidDob").textContent= "";
		document.querySelector('#myBtn').disabled = false;
		return true;
	}
}

function contactEVHandler(event){
	let t = event.target;
	return contactEVHandler(t);
}
function contactEVHandler(contact) {

	if(contact.value == null || contact.value ==""){
		contact.classList.add("class", "red")
		document.getElementById("invalidcontact").classList.remove("hidden");
		document.getElementById("invalidcontact").textContent= "Contact cannot be empty !";
		return false;
	}
	else if (!validateNumber(contact.value)) {
		contact.classList.add("class", "red")
		document.getElementById("invalidcontact").classList.remove("hidden");
		document.getElementById("invalidcontact").textContent= "Contact cannot have a letter character or space !";
		document.querySelector('#myBtn').disabled = true;
		return false;
	}
	else {

		contact.classList.remove("class", "red")
		document.getElementById("invalidcontact").classList.add("hidden");
		document.getElementById("invalidcontact").textContent= "";
		document.querySelector('#myBtn').disabled = false;
		return true;
	}
}

function heightEVHandler(event){
	let t = event.target;
	return heightEVHandler(t);
}
function heightEVHandler(h) {

	if(h.value == null || h.value ==""){
		contact.classList.add("class", "red")
		document.getElementById("invalidheight").classList.remove("hidden");
		document.getElementById("invalidheight").textContent= "Height cannot be empty !";
		return false;
	}
	else if (!validateNumber(h.value)) {
		h.classList.add("class", "red")
		document.getElementById("invalidheight").classList.remove("hidden");
		document.getElementById("invalidheight").textContent= "Height cannot have a letter character or space !";
		document.querySelector('#myBtn').disabled = true;
		return false;
	}
	else {

		h.classList.remove("class", "red")
		document.getElementById("invalidheight").classList.add("hidden");
		document.getElementById("invalidheight").textContent= "";
		document.querySelector('#myBtn').disabled = false;
		return true;
	}
}

function weightEVHandler(event){
	let t = event.target;
	return weightEVHandler(t);
}
function weightEVHandler(w) {

	if(w.value == null || w.value ==""){
		w.classList.add("class", "red")
		document.getElementById("invalidweight").classList.remove("hidden");
		document.getElementById("invalidweight").textContent= "Weight cannot be empty !";
		return false;
	}
	else if (!validateNumber(w.value)) {
		w.classList.add("class", "red")
		document.getElementById("invalidweight").classList.remove("hidden");
		document.getElementById("invalidweight").textContent= "Weight cannot have a letter character or space !";
		document.querySelector('#myBtn').disabled = true;
		return false;
	}
	else {

		w.classList.remove("class", "red")
		document.getElementById("invalidweight").classList.add("hidden");
		document.getElementById("invalidweight").textContent= "";
		document.querySelector('#myBtn').disabled = false;
		return true;
	}
}

function enameEVHandler(event){
	let t = event.target;
	return enameEVHandler(t);
}
function enameEVHandler(ename) {

	if(ename.value == null || ename.value ==""){
		ename.classList.add("class", "red")
		document.getElementById("invalidename").classList.remove("hidden");
		document.getElementById("invalidename").textContent= "Emergency name cannot be empty !";
		return false;
	}
	else if (!validateUName(ename.value)) {
		ename.classList.add("class", "red")
		document.getElementById("invalidename").classList.remove("hidden");
		document.getElementById("invalidename").textContent= "Emergency name cannot have a letter character or space !";
		document.querySelector('#myBtn').disabled = true;
		return false;
	}
	else {

		ename.classList.remove("class", "red")
		document.getElementById("invalidename").classList.add("hidden");
		document.getElementById("invalidename").textContent= "";
		document.querySelector('#myBtn').disabled = false;
		return true;
	}
}

function econtactVHandler(event){
	let t = event.target;
	return econtactVHandler(t);
}
function econtactVHandler(econtact) {

	if(econtact.value == null || econtact.value ==""){
		econtact.classList.add("class", "red")
		document.getElementById("invalidecontact").classList.remove("hidden");
		document.getElementById("invalidecontact").textContent= "Emergency contact cannot be empty !";
		return false;
	}
	else if (!validateNumber(econtact.value)) {
		econtact.classList.add("class", "red")
		document.getElementById("invalidecontact").classList.remove("hidden");
		document.getElementById("invalidecontact").textContent= "Emergency contact cannot have a letter character or space !";
		document.querySelector('#myBtn').disabled = true;
		return false;
	}
	else {

		econtact.classList.remove("class", "red")
		document.getElementById("invalidecontact").classList.add("hidden");
		document.getElementById("invalidecontact").textContent= "";
		document.querySelector('#myBtn').disabled = false;
		return true;
	}
}






