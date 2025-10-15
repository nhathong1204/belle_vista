$(document).ready(function() {
    $(document).on("submit","#contact-form-ajax",function(e){
        e.preventDefault()
        console.log("Submited...")
        let first_name = $("#first_name").val()
        let last_name = $("#last_name").val()
        let email = $("#email").val()
        let subject = $("#subject").val()
        let message = $("#message").val()
        console.log(first_name, last_name, email, subject, message)

        $.ajax({
            url: "/ajax-contact-form",
            data: {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "subject": subject,
                "message": message,
            },
            dataType: "json",
            success: function(res) {
                console.log("Sent data to server...")
                if(res.success == true) {
                    alert("Email sent successfully!")
                    location.reload();
                }
            }
        })
    })
})