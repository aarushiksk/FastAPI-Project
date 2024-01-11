document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("myForm");
    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        // Get form input values
        const variance = parseFloat(document.getElementById("variance").value);
        const skewness = parseFloat(document.getElementById("skewness").value);
        const curtosis = parseFloat(document.getElementById("curtosis").value);
        const entropy = parseFloat(document.getElementById("entropy").value);

        // Create a JSON object similar to your BankNote model
        const data = {
            variance: variance,
            skewness: skewness,
            curtosis: curtosis,
            entropy: entropy
        };

        // Send the JSON object to the /predict endpoint
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            const result = await response.json();
            // Handle the received result here
            document.getElementById("output").innerText = `Prediction: ${result.prediction}`;
        } else {
            console.error("Error occurred.");
        }
    });
});