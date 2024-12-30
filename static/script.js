document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    const resultText = document.getElementById('resultText');
    const predictionResult = document.getElementById('predictionResult');
    const predictButton = document.getElementById('predictButton');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); 

        const data = {
            gender: document.getElementById('gender').value,
            age: document.getElementById('age').value,
            course: document.getElementById('course').value,
            cgpa: document.getElementById('cgpa').value,
            year: document.getElementById('year').value,
            maritalStatus: document.getElementById('maritalStatus').value,
            depression: document.getElementById('depression').value,
            anxiety: document.getElementById('anxiety').value,
            panicAttack: document.getElementById('panicAttack').value,
            treatment: document.getElementById('treatment').value
        };

        // Disable the button while waiting for the response
        predictButton.disabled = true;

        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            // Enable the button after receiving the response
            predictButton.disabled = false;

            if (data.prediction) {
                resultText.textContent = `Prediction: ${data.prediction}`;
                if (data.prediction === "No Depression Detected") {
                    predictionResult.style.background = 'green';
                } else if (data.prediction === "Depression Detected") {
                    predictionResult.style.background = 'red';
                }
            } else if (data.error) {
                resultText.textContent = `Error: ${data.error}`;
            } else {
                resultText.textContent = 'Unexpected error occurred.';
            }
        })
        .catch(error => {
            predictButton.disabled = false;
            resultText.textContent = `Error: ${error.message}`;
        });
    });
});