// Mobile navigation toggle (replaces jQuery + Bootstrap JS)
const toggler = document.querySelector(".navbar-toggler");
const menu = document.querySelector(".navbar-collapse");

toggler?.addEventListener("click", () => {
    const open = menu.classList.toggle("show");
    toggler.setAttribute("aria-expanded", open);
});
