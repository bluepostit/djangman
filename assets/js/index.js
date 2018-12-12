console.log("Hello, world");
import 'bootstrap/dist/css/bootstrap.min.css';
import '../css/styles.css';

document.addEventListener('DOMContentLoaded', function() {
    var txtGuess = document.getElementById('id_guess')
    if (!!txtGuess) {
        txtGuess.focus();
    }
});