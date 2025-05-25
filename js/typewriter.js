const roles = [
    "Computer Science & Engineering Graduate",
    "Software Engineer"
];

let part = 0;
let partIndex = 0;
let isDeleting = false;
const element = document.getElementById("typewriter-text");

function typeEffect() {
    const currentText = roles[part];
    const displayedText = isDeleting
        ? currentText.substring(0, partIndex--)
        : currentText.substring(0, partIndex++);

    element.textContent = displayedText;

    if (!isDeleting && partIndex === currentText.length) {
        setTimeout(() => isDeleting = true, 1000);
    } else if (isDeleting && partIndex === 0) {
        isDeleting = false;
        part = (part + 1) % roles.length;
    }

    const delay = isDeleting ? 50 : 100;
    setTimeout(typeEffect, delay);
}

document.addEventListener("DOMContentLoaded", typeEffect);
