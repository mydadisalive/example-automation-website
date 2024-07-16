document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('fetch-quote').addEventListener('click', function() {
        fetchRandomQuote();
    });
});

function fetchRandomQuote() {
    const url = 'https://api.quotable.io/random';

    fetch(url)
        .then(response => response.json())
        .then(data => {
            displayQuote(data);
        })
        .catch(error => console.error('Error fetching quote:', error));
}

function displayQuote(data) {
    const quote = document.getElementById('quote');
    const author = document.getElementById('author');

    quote.textContent = `"${data.content}"`;
    author.textContent = `— ${data.author}`;
}
