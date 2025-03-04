document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("signupForm").addEventListener("submit", function(event) {
        let panInput = document.getElementById("pan").value.toUpperCase();
        let panPattern = /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/;

        if (!panPattern.test(panInput)) {
            alert("Invalid PAN number! Example: ABCDE1234F");
            event.preventDefault();  // Stop form submission
        }
    });
});
