document.addEventListener('DOMContentLoaded', function() {
    fetchPassengers();
});

function fetchPassengers() {
    fetch('http://127.0.0.1:8000/passengers/')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        displayPassengers(data);
    })
    .catch(error => {
        console.error('Error fetching data: ', error);
    });
}

function displayPassengers(passengers) {
    // Sort passengers by seat number
    passengers.sort((a, b) => {
        const seatA = parseInt(a.seat.match(/\d+/), 10); // Extract number from seat (e.g., "12A" becomes 12)
        const seatB = parseInt(b.seat.match(/\d+/), 10);
        return seatA - seatB;
    });

    const passengerList = document.getElementById('passengerList');
    passengerList.innerHTML = ''; // Clear the list first
    passengers.forEach(passenger => {
        const passengerDiv = document.createElement('div');
        passengerDiv.className = 'passenger';
        passengerDiv.innerHTML = `
            <p>ID: ${passenger.id}</p>
            <p>Seat: ${passenger.seat}</p>
            <p>Drink: ${passenger.drink}</p>
            <p>Wakeup: ${passenger.wakeup}</p>
        `;
        passengerList.appendChild(passengerDiv);
    });
}
