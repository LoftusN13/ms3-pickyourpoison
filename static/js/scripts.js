function sendEmail(contactForm){
    emailjs.send("gmail", "pick-your-poison",{
        "from_name": contactForm.fullname.value,
        "from_email": contactForm.email.value,
        "user_message": contactForm.message.value
    })

    document.getElementById("contactForm").reset();
    return false;
}