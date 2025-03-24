document.addEventListener('DOMContentLoaded', function() {
    // Check for saved dark mode preference
    const darkModeEnabled = localStorage.getItem('darkMode') === 'enabled';
    
    // Apply dark mode if it was enabled previously
    if (darkModeEnabled) {
        document.body.classList.add('dark-mode');
        document.documentElement.setAttribute('data-bs-theme', 'dark');
        if (document.getElementById('darkModeToggle')) {
            document.getElementById('darkModeToggle').checked = true;
        }
    }
    
    // Set up event listener for dark mode toggle
    const darkModeToggle = document.getElementById('darkModeToggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('change', function() {
            if (this.checked) {
                document.body.classList.add('dark-mode');
                document.documentElement.setAttribute('data-bs-theme', 'dark');
                localStorage.setItem('darkMode', 'enabled');
            } else {
                document.body.classList.remove('dark-mode');
                document.documentElement.setAttribute('data-bs-theme', 'light');
                localStorage.setItem('darkMode', null);
            }
        });
    }

    // Handle the theme-toggle button as well
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', function() {
            const isDarkMode = document.body.classList.contains('dark-mode');
            if (isDarkMode) {
                document.body.classList.remove('dark-mode');
                document.documentElement.setAttribute('data-bs-theme', 'light');
                localStorage.setItem('darkMode', null);
                if (darkModeToggle) {
                    darkModeToggle.checked = false;
                }
            } else {
                document.body.classList.add('dark-mode');
                document.documentElement.setAttribute('data-bs-theme', 'dark');
                localStorage.setItem('darkMode', 'enabled');
                if (darkModeToggle) {
                    darkModeToggle.checked = true;
                }
            }
            
            // Update the icon
            const icon = this.querySelector('i');
            if (icon) {
                if (document.body.classList.contains('dark-mode')) {
                    icon.classList.replace('bi-moon', 'bi-sun');
                } else {
                    icon.classList.replace('bi-sun', 'bi-moon');
                }
            }
        });
        
        // Set initial icon state
        const icon = themeToggleBtn.querySelector('i');
        if (icon && darkModeEnabled) {
            icon.classList.replace('bi-moon', 'bi-sun');
        }
    }
});
