document.addEventListener('DOMContentLoaded', () => {
    const fetchButton = document.getElementById('fetch-quote');
    const quoteDiv = document.getElementById('quote');
    const authorDiv = document.getElementById('author');

    async function fetchQuote() {
        const response = await fetch('https://api.quotable.io/random');
        const data = await response.json();
        quoteDiv.textContent = `"${data.content}"`;
        authorDiv.textContent = `- ${data.author}`;
    }

    fetchButton.addEventListener('click', fetchQuote);
    // Load a quote when the page loads
    fetchQuote();
});
