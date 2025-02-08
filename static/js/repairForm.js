// Repair form character count logic for problem description
document.addEventListener("DOMContentLoaded", () => {
    const problemDescription = document.querySelector("#id_problem_description");
    const charCount = document.querySelector("#charCount");
  
    if (problemDescription) {
      problemDescription.addEventListener("input", () => {
        const currentLength = problemDescription.value.length;
        charCount.textContent = `${currentLength}/500 characters used`;
      });
    }
  });
  