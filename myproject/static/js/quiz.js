document.addEventListener("DOMContentLoaded", () => {
  const quizForm = document.getElementById("quizForm");
  if (quizForm) {
    quizForm.addEventListener("submit", () => {
      const submitBtn = quizForm.querySelector("button[type='submit']");
      submitBtn.disabled = true;
      submitBtn.textContent = "Submitting...";
    });
  }

  //  60-second timer

  let timerDisplay = document.createElement("div");
  timerDisplay.className = "alert alert-info mt-3";
  timerDisplay.innerText = "Time left: 60s";
  if (quizForm) quizForm.prepend(timerDisplay);

  let time = 60;
  const interval = setInterval(() => {
    time--;
    timerDisplay.innerText = `Time left: ${time}s`;
    if (time <= 0) {
      clearInterval(interval);
      quizForm.submit();
    }
  }, 1000);
});


 
