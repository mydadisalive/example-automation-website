document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('fetch-quote').addEventListener('click', function() {
        fetchRandomQuote();
    });

    // Load a quote when the page first loads
    fetchRandomQuote();
});

async function fetchRandomQuote() {
    const url = 'https://api.quotable.io/random';

    console.log('Fetching random quote from:', url);

    try {
        const response = await fetch(url);
        console.log('Received response:', response);
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }
        const data = await response.json();
        console.log('Received data:', data);
        displayQuote(data);
    } catch (error) {
        console.error('Error fetching quote:', error);
        alert('Failed to fetch quote. Please try again later.');
    }
}

function displayQuote(data) {
    const quote = document.getElementById('quote');
    const author = document.getElementById('author');

    quote.textContent = `"${data.content}"`;
    author.textContent = `— ${data.author}`;

    console.log('Displayed quote:', data.content);
    console.log('Displayed author:', data.author);
}

module.exports = { fetchRandomQuote, displayQuote };
