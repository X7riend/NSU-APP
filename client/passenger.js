var seat = "";
const maxRow = 30;
const seatLetters = 'ABCDEF';
    
const randomRow = Math.floor(Math.random() * maxRow) + 1; // Random row from 1 to maxRow
const randomSeatLetter = seatLetters[Math.floor(Math.random() * seatLetters.length)]; // Random seat letter
    
seat = `${randomRow}${randomSeatLetter}`;

document.getElementById('myForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Stop the standard form submission
    getForm(); // Call your function to handle the form
  });
document.addEventListener('DOMContentLoaded', () => {


    const buttons = document.querySelectorAll('.choice-btn');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove 'selected' class from all buttons
            buttons.forEach(button => {
                button.classList.remove('selected');
            });

            // Add 'selected' class to the clicked button
            btn.classList.add('selected');
        });
    });
 
    let totalDrinks = 0;
    const drinkList = document.getElementById('drinkList');

    document.querySelectorAll('.counter').forEach(counter => {
        const label = counter.querySelector('.label');
        const decrementButton = counter.querySelector('.decrement');
        const incrementButton = counter.querySelector('.increment');
        const drinkName = counter.closest('.menu-item').querySelector('h3').textContent;

        decrementButton.addEventListener('click', () => {
            if (parseInt(label.textContent, 10) > 0) {
                changeLabelValue(label, -1);
                totalDrinks--;
                removeDrinkFromList(drinkName);
            }
        });

        incrementButton.addEventListener('click', () => {
            if (totalDrinks < 3) {
                changeLabelValue(label, 1);
                totalDrinks++;
                addDrinkToList(drinkName);
            } else {
                alert('No more than 3 drinks can be selected.');
            }
        });
    });

    function changeLabelValue(labelElement, change) {
        const currentValue = parseInt(labelElement.textContent, 10);
        labelElement.textContent = currentValue + change;
    }

    function addDrinkToList(drink) {
        const li = document.createElement('li');
        li.textContent = drink;
        li.className = 'listItem';
        drinkList.appendChild(li);
    }

    function removeDrinkFromList(drink) {
        // Find the list item with the matching drink name and remove it
        Array.from(drinkList.children).forEach(li => {
            if (li.textContent === drink) {
                drinkList.removeChild(li);
                return; // Exit the loop after removing the item
            }
        });
    }
});
function getForm() {
    let selectedDrinks = [];

    // Assuming each label has a data attribute 'data-drink-name'
    document.querySelectorAll('.menu-item .label').forEach(label => {
        if (parseInt(label.textContent) > 0) {
            selectedDrinks.push({
                drink: label.closest('.menu-item').querySelector('h3').textContent,
                quantity: parseInt(label.textContent)
            });
        }
    });

    // Assuming 'wakeupPreference' value is updated elsewhere in the code on button click
    const wakeupPreference = document.querySelector('.choice-btn.selected').getAttribute('data-wakeup');

    // Get the selected seat
    const seat = `${randomRow}${randomSeatLetter}`;

    // Construct the JSON body using the properties expected by your FastAPI endpoint
    const data = {
        seat: seat, // This should be a unique identifier for the seat
        drink: selectedDrinks.map(drink => drink.drink).join(', '), // Combines all drink choices
        quantity: selectedDrinks.map(drink => drink.quantity).reduce((a, b) => a + b, 0), // Sums up quantities
        wakeup: wakeupPreference
    };

    fetch('http://127.0.0.1:8000/passengers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data) // Send data as an object
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
        alert("Preferences submitted successfully!");
    })
    .catch(error => {
        console.error('Error:', error);
        alert("There was a problem submitting your preferences.");
    });
}
