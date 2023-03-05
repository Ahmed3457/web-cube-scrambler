let startTime, timerInterval;
function startTimer() {
    let currentTime = Date.now();
    startTime = currentTime;
    timerInterval = setInterval(updateTimer, 10);
  }
  
  function stopTimer() {
    clearInterval(timerInterval);
  }
  
  function updateTimer() {
    let currentTime = Date.now();
    let elapsedTime = currentTime - startTime;
  
    let minutes = Math.floor(elapsedTime / 60000);
    let seconds = ((elapsedTime % 60000) / 1000).toFixed(2);
  
    document.getElementById("timer").innerHTML = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
  }
  
  document.addEventListener("keydown", function (event) {
    if (event.code === "Space") {
      if (timerInterval) {
        stopTimer();
      } else {
        startTimer();
      }
    }
  });