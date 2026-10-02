// Typewriter effect for the hero tagline; roles come from the element's data-roles attribute.
const element = document.getElementById("typewriter-text");
const roles = JSON.parse(element.dataset.roles);

const TYPE_DELAY = 100;
const DELETE_DELAY = 50;
const PAUSE_BEFORE_DELETE = 1000;

let role = 0;
let length = 0;
let deleting = false;

function tick() {
    const text = roles[role];
    length += deleting ? -1 : 1;
    element.textContent = text.slice(0, length);

    if (!deleting && length === text.length) {
        deleting = true;
        return setTimeout(tick, PAUSE_BEFORE_DELETE);
    }
    if (deleting && length === 0) {
        deleting = false;
        role = (role + 1) % roles.length;
    }
    setTimeout(tick, deleting ? DELETE_DELAY : TYPE_DELAY);
}

tick();
