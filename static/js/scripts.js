/* EmailJS funtion on contact form submission */
function sendEmail(contactForm){
    emailjs.send("gmail", "pick-your-poison",{
        "from_name": contactForm.fullname.value,
        "from_email": contactForm.email.value,
        "user_message": contactForm.message.value
    })
    .then(
        /* Alert user to successful form submission */
        function(response) {
            let msg = document.getElementById("submit-msg");
            msg.style.display = "block";

        },
        /* Alert user to unsuccessful form submission */
        function(error) {
            document.getElementById("submit-msg");innerHTML = "Uh-oh! Something went wrong; message has not been sent!";
        }
    );

    document.getElementById("contactForm").reset();
    return false;
}

/* Scroll to top of page button function,
target the scroll button, trigger button to appear
when user starts scrolling down, when clicked it
returns user to top of page */
let scrollButton = document.getElementById("scroll-btn")

window.onscroll = function() {
    scrollFunction();
}

/* display button once user has started scrolling */
function scrollFunction() {
    if (document.body.scrollTop > 140  || document.documentElement.scrollTop > 140) {
        scrollButton.style.display = "block";
    }
    else {
        scrollButton.style.display = "none";
    }
}
/* bring user to top of bage when button is clicked */
function scrollToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}