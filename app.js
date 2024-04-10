document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Ajoutez ici la logique pour vérifier l'authentification du utilisateur
        if (username === 'user' && password === 'password') {
            window.location.href = 'quiz.html'; // Rediriger vers la page de quiz si l'authentification réussit
        } else {
            alert('Invalid username or password. Please try again.'); // Afficher une alerte si l'authentification échoue
        }
    });
});
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const selectedAnswer = document.querySelector('input[name="capital"]:checked');

        // Ajoutez ici la logique pour vérifier la réponse sélectionnée
        if (selectedAnswer && selectedAnswer.value === 'paris') {
            alert('Correct answer! You win 10000 francs CFA.'); // Afficher un message si la réponse est correcte
            // Ajoutez ici la logique pour enregistrer les gains de l'utilisateur
        } else {
            alert('Incorrect answer. Please try again.'); // Afficher un message si la réponse est incorrecte
        }
    });
});
