
document.addEventListener("DOMContentLoaded", () => {
    const root = document.documentElement;
    const toggle = document.getElementById('theme-toggle');

    // Load saved preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        root.dataset.theme = savedTheme;
    }
    toggle.addEventListener('click', () => {
        const currentTheme = root.dataset.theme;
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

        root.dataset.theme = newTheme;
        localStorage.setItem('theme', newTheme);
    });
});
