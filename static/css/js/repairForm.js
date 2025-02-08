// Basic Form Validation
function validateForm(event) {
    event.preventDefault();

    let productName = document.getElementById('id_product_name').value.trim();
    let problemDescription = document.getElementById('id_problem_description').value.trim();
    let location = document.getElementById('id_location').value.trim();

    if (!productName || !problemDescription || !location) {
        alert("Please fill in all required fields.");
        return false;
    }

    alert("Form successfully submitted!");
    document.getElementById('repairForm').submit();
}

// Character Counter for Problem Description
function updateCharCount() {
    const maxChars = 500;
    let currentLength = document.getElementById('id_problem_description').value.length;
    let charCountDisplay = document.getElementById('charCount');
    charCountDisplay.textContent = `${currentLength}/${maxChars} characters used`;
}

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('repairForm').addEventListener('submit', validateForm);
    document.getElementById('id_problem_description').addEventListener('input', updateCharCount);
});
