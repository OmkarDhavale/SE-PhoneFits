function sendFeedback() {
    var params = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        feedback: document.getElementById("feedback").value,
    };

    const serviceID = "service_47wj1pc";
    const templateID = "template_hhr1esn";

    emailjs.send(serviceID, templateID, params)
        .then(
            res => {
                document.getElementById("name").value = "";
                document.getElementById("email").value = "";
                document.getElementById("feedback").value = "";

                console.log("Feedback Form entries : ", res);
                alert("Your feedback has been sent. Thank you!");
            }
        )
        .catch((err) => console.log("Error occured : ", err));
}
