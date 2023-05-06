function submitForm(event) {
    event.preventDefault();
  
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const gender = document.getElementById("gender").value;
    const location = document.getElementById("location").value;
    const bio = document.getElementById("bio").value;
  
    console.log("Name:", name);
    console.log("Age:", age);
    console.log("Gender:", gender);
    console.log("Location:", location);
    console.log("Bio:", bio);
  
    document.getElementById("registrationForm").reset();
}

