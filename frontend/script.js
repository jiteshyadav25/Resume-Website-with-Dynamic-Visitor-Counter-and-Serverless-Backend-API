const API_URL = "https://1w8egyu7w0.execute-api.us-east-1.amazonaws.com/visits";

async function updateVisitorCount() {
    const counter = document.getElementById("visitor-count");

    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("API request failed");
        }

        const data = await response.json();
        counter.textContent = data.visits;

    } catch (error) {
        console.error(error);
        counter.textContent = "Unavailable";
    }
}

updateVisitorCount();

