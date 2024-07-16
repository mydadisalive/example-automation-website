document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    document.getElementById('form-response').textContent = `Thank you, ${name}! We will contact you at ${email}.`;
});

document.getElementById('fetch-repos').addEventListener('click', function() {
    const username = document.getElementById('github-username').value;
    if (!username) {
        alert('Please enter a GitHub username');
        return;
    }

    fetch(`https://api.github.com/users/${username}/repos`)
        .then(response => response.json())
        .then(repos => {
            const repoList = document.getElementById('repo-list');
            repoList.innerHTML = '';
            repos.forEach(repo => {
                const listItem = document.createElement('li');
                listItem.textContent = repo.name;
                repoList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching repos:', error));
});
