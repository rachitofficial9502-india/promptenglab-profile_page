
const themeToggle = document.getElementById("themeToggle");

if (themeToggle) {
    themeToggle.addEventListener("click", function () {
        document.body.classList.toggle("dark");

        themeToggle.textContent = document.body.classList.contains("dark")
            ? "Switch to light mode"
            : "Switch to dark mode";
    });
}
