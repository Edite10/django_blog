document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElement = document.querySelector('html');
    
    // Check for saved theme preference or respect OS theme settings
    const savedTheme = localStorage.getItem('theme') || 'auto';
    
    // Apply theme
    function applyTheme(theme) {
        if (theme === 'dark' || (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            htmlElement.setAttribute('data-bs-theme', 'dark');
            if (themeToggle) themeToggle.innerHTML = '<i class="bi bi-sun"></i>';
        } else {
            htmlElement.setAttribute('data-bs-theme', 'light');
            if (themeToggle) themeToggle.innerHTML = '<i class="bi bi-moon"></i>';
        }
    }
    
    // Initial theme application
    applyTheme(savedTheme);
    
    // Toggle theme when button is clicked
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = htmlElement.getAttribute('data-bs-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            localStorage.setItem('theme', newTheme);
            applyTheme(newTheme);
        });
    }
});
