document.addEventListener('DOMContentLoaded', function() {
    fetchNewQuestion();

    document.getElementById('quiz-form').addEventListener('submit', function(event) {
        event.preventDefault();
        checkAnswer();
    });

    document.getElementById('new-question').addEventListener('click', function() {
        fetchNewQuestion();
    });
});

function fetchNewQuestion() {
    fetch('https://opentdb.com/api.php?amount=1&type=multiple')
        .then(response => response.json())
        .then(data => {
            const questionData = data.results[0];
            displayQuestion(questionData);
        })
        .catch(error => console.error('Error fetching question:', error));
}

function displayQuestion(questionData) {
    const questionElement = document.getElementById('question');
    questionElement.innerHTML = questionData.question;

    const answersContainer = document.getElementById('answers');
    answersContainer.innerHTML = '';

    const correctAnswer = questionData.correct_answer;
    const incorrectAnswers = questionData.incorrect_answers;
    const allAnswers = [...incorrectAnswers, correctAnswer].sort(() => Math.random() - 0.5);

    allAnswers.forEach(answer => {
        const label = document.createElement('label');
        const input = document.createElement('input');
        input.type = 'radio';
        input.name = 'answer';
        input.value = answer;
        label.appendChild(input);
        label.appendChild(document.createTextNode(answer));
        answersContainer.appendChild(label);
    });

    document.getElementById('feedback').innerHTML = '';
}

function checkAnswer() {
    const selectedAnswer = document.querySelector('input[name="answer"]:checked');
    if (!selectedAnswer) {
        alert('Please select an answer!');
        return;
    }

    const questionElement = document.getElementById('question');
    const questionText = questionElement.textContent;

    fetch(`https://opentdb.com/api.php?amount=1&type=
