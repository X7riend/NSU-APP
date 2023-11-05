var seat = "";
const maxRow = 30;
const seatLetters = 'ABCDEF';
    
const randomRow = Math.floor(Math.random() * maxRow) + 1; // Random row from 1 to maxRow
const randomSeatLetter = seatLetters[Math.floor(Math.random() * seatLetters.length)]; // Random seat letter
    
seat = `${randomRow}${randomSeatLetter}`;

document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('myForm').addEventListener('submit', function(e) {
      e.preventDefault(); // Stop the standard form submission
      getForm(); // Call your function to handle the form
    });
  });


function getForm(){
  // First, find which drink is selected
  let drinkPreference;
  document.querySelectorAll('.drinks').forEach((drink) => {
    if (drink.checked) {
      drinkPreference = drink.value;
    }
  });

  // Then, find which snack is selected
  let sleepPreference;
  document.querySelectorAll('input[name="sleep"]').forEach((sleep) => {
    if (sleep.checked) {
      sleepPreference = sleep.value;
    }
  });
  // Create a data object to send as JSON
  var data = {
    "seat": seat,
    "drink": drinkPreference,
    "wakeup": sleepPreference
  };
     fetch('http://127.0.0.1:8000/passengers', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(data) // Send data as an object
      })
      .then(response => response.json())
      .then(data => {
          console.log(data);
      })
      .catch(error => {
          console.error('Error:', error);
      });
      alert("Success");
}
function generateRandomAirlineSeat() {
  // Assuming rows go from 1 to 30 and seats from A to F
  const maxRow = 30;
  const seatLetters = 'ABCDEF';

  const randomRow = Math.floor(Math.random() * maxRow) + 1; // Random row from 1 to maxRow
  const randomSeatLetter = seatLetters[Math.floor(Math.random() * seatLetters.length)]; // Random seat letter

  return `${randomRow}${randomSeatLetter}`;
}