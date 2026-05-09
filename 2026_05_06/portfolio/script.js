// 1. Licznik
let count = 0;
function incrementCounter() {
    count++;
    document.getElementById('counter-text').innerText = `Kliknięć: ${count}`;
}

// 2. Generator Cytatów
const quotes = [
    "Programowanie to sztuka zrozumienia problemu.",
    "Błędy są dowodem na to, że tworzysz coś nowego.",
    "Najpierw rozwiązuj problem, potem pisz kod.",
    "Dobry programista to taki, który umie zadawać pytania.",
    "Kod to poezja napisana w logice.",
    "Zawsze pisz kod tak, jakby czytał go psychopata z Twoim adresem.",
    "Iteracja jest ludzka, rekurencja boska.",
    "Nie bój się zmian, bój się braku postępu.",
    "Małe kroki prowadzą do wielkich systemów.",
    "AI to Twój asystent, nie zastępca."
];

function drawQuote() {
    const random = quotes[Math.floor(Math.random() * quotes.length)];
    document.getElementById('quote-display').innerText = `"${random}"`;
}

// 3. Walidacja formularza
function validateForm(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const status = document.getElementById('form-status');
    
    if (!email.includes('@')) {
        status.innerText = "Podaj poprawny email!";
        status.style.color = "red";
    } else {
        status.innerText = "Wiadomość wysłana (symulacja)!";
        status.style.color = "#38bdf8";
    }
}

// 4. Animacje przy przewijaniu
window.addEventListener('scroll', () => {
    document.querySelectorAll('.reveal').forEach(el => {
        if(el.getBoundingClientRect().top < window.innerHeight - 50) {
            el.classList.add('active');
        }
    });
});

// 5. Dark Mode (Inwersja kolorów dla uproszczenia)
function toggleDarkMode() {
    document.body.classList.toggle('light-theme');
    // W CSS musiałbyś dodać definicję .light-theme, ale inwersja filtra jest szybsza:
    if (document.body.style.filter === 'invert(1)') {
        document.body.style.filter = 'invert(0)';
    } else {
        document.body.style.filter = 'invert(1)';
    }
}