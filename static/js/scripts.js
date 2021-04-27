function sendEmail(contactForm){
    emailjs.send("gmail", "pick-your-poison",{
        "from_name": contactForm.fullname.value,
        "from_email": contactForm.email.value,
        "user_message": contactForm.message.value
    })
    .then(
        /* Alert user to successful form submission */
        function(response) {
            document.getElementById("submit-msg").innerHTML = "It's on the way! Your message has been sent!";
        },
        /* Alert user to unsuccessful form submission */
        function(error) {
             document.getElementById("submit-msg").innerHTML = "Uh-oh! Something went wrong; message has not been sent!";
        }
    );

    document.getElementById("contactForm").reset();
    return false;
}