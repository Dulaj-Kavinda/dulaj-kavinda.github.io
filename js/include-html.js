function includeHTML() {
    const elements = document.querySelectorAll("[w3-include-html]");
    elements.forEach(el => {
        const file = el.getAttribute("w3-include-html");
        if (file) {
            fetch(file)
                .then(response => {
                    if (!response.ok) throw new Error("Page not found.");
                    return response.text();
                })
                .then(data => {
                    el.innerHTML = data;
                    el.removeAttribute("w3-include-html");
                    includeHTML(); // Recursively include nested includes
                })
                .catch(error => {
                    el.innerHTML = error.message;
                });
        }
    });
}
