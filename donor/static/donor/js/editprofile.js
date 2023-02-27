var hasNumber = /\d/;
var hasSpecial = /^[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]*$/;

function ValidateEmail(input) {

    var validRegex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
  
    if (input.value.match(validRegex)) {
  
        document.getElementById("emailInvalid").innerHTML="";
        document.getElementById("subBut").innerHTML="";

        if(isGood())
        {
            document.querySelector('#submitB').disabled = false;
        }

    } else {
  
       document.getElementById("emailInvalid").innerHTML="Please Enter A proper Email";
       document.getElementById("subBut").innerHTML="New info cannot be saved while invalid inputs!";
       document.querySelector('#submitB').disabled = true;
  
      return false;
  
    }
  
} // Working
function ValidatefirstName(input) {
  
    if ( (input.value.length === 0) || (hasNumber.test(input.value)) || (hasSpecial.test(input.value)) ) {
  
        document.getElementById("fnameInvalid").innerHTML="Please a valid first name";
        document.getElementById("subBut").innerHTML="New info cannot be saved while invalid inputs!";
        document.querySelector('#submitB').disabled = true;
        return false;
  

    } else {
  
       document.getElementById("fnameInvalid").innerHTML="";
       if(isGood())
        {
            document.querySelector('#submitB').disabled = false;
        }
      return true;
  
    }
  
} // working
function ValidatelastName(input) {
  
    if ((input.value.length === 0) || (hasNumber.test(input.value)) || (hasSpecial.test(input.value))) {
  
        document.getElementById("lnameInvalid").innerHTML="Please a valid last name";
        document.getElementById("subBut").innerHTML="New info cannot be saved while invalid inputs!";
        document.querySelector('#submitB').disabled = true;
        
        return false;

    } else {
  
       document.getElementById("lnameInvalid").innerHTML="";
       if(isGood())
        {
            document.querySelector('#submitB').disabled = false;
        }
      return true;
  
    }

} // working
function ValidateDOB(input) {
  
    if (input.value.length === 0) {
  
        document.getElementById("DOBInvalid").innerHTML="Please a valid Date of Birth";
        
        return false;

    } else {
  
       document.getElementById("DOBInvalid").innerHTML="";
  
      return true;
  
    }

}
function ValidateEmergName(input) {
  
    if(input.value.length === 0)
    {
        document.getElementById("enameInvalid").innerHTML="";
        document.querySelector('#submitB').disabled = false;
        return true;
    }
    else if ((hasNumber.test(input.value)) || (hasSpecial.test(input.value)) ) {
  
        document.getElementById("enameInvalid").innerHTML="Please a valid name if you would like an Emergency Contact";
        document.getElementById("subBut").innerHTML="New info cannot be saved while invalid inputs!";
        document.querySelector('#submitB').disabled = true;

        return false;
  
    } else {
  
       document.getElementById("enameInvalid").innerHTML="";
       if(isGood())
        {
            document.querySelector('#submitB').disabled = false;
        }
  
      return true;
  
    }
  
} //working
function ValidatePhone(input) {
  
    var phoneRegex = /^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$/;
    if(input.value.length === 0)
    {
        document.getElementById("phoneInvalid").innerHTML="";
        document.getElementById("subBut").innerHTML="";
        if(isGood())
        {
            document.querySelector('#submitB').disabled = false;
        }
        return true;
    }
    else if (input.value.match(phoneRegex) ) {
  
        document.getElementById("phoneInvalid").innerHTML="";
        document.getElementById("subBut").innerHTML="";
        if(isGood())
        {
            document.querySelector('#submitB').disabled = false;
        }

        return true;
  
    } else {
  
       document.getElementById("phoneInvalid").innerHTML="An Emergency Phone Number must be valid if used";
       document.getElementById("subBut").innerHTML="New info cannot be saved while invalid inputs!";
       document.querySelector('#submitB').disabled = true;
  
      return false;
  
    }
  
}

function isGood()
{
   
    if(ValidateEmail() & ValidatefirstName() & ValidatelastName() & ValidateDOB() & ValidatePhone())
    {
        return true;
    }
    else
    {
        return false;
    }



}