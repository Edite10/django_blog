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
            themeToggle.setAttribute('aria-label', 'Switch to light mode');
            
            // Update TinyMCE if it exists
            if (typeof tinymce !== 'undefined' && tinymce.activeEditor) {
                tinymce.activeEditor.dom.addClass(tinymce.activeEditor.dom.getRoot(), 'dark-mode');
            }
        } else {
            htmlElement.setAttribute('data-bs-theme', 'light');
            if (themeToggle) themeToggle.innerHTML = '<i class="bi bi-moon"></i>';
            themeToggle.setAttribute('aria-label', 'Switch to dark mode');
            
            // Update TinyMCE if it exists
            if (typeof tinymce !== 'undefined' && tinymce.activeEditor) {
                tinymce.activeEditor.dom.removeClass(tinymce.activeEditor.dom.getRoot(), 'dark-mode');
            }
        }
    }
    
    // Initial theme application
    applyTheme(savedTheme);
    
    // Listen for OS theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function() {
        if (savedTheme === 'auto') {
            applyTheme('auto');
        }
    });
    
    // Toggle theme when button is clicked
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = htmlElement.getAttribute('data-bs-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            localStorage.setItem('theme', newTheme);
            applyTheme(newTheme);

            // Announce theme change for screen readers
            const announcement = document.createElement('div');
            announcement.setAttribute('aria-live', 'polite');
            announcement.classList.add('sr-only');
            announcement.textContent = `Changed to ${newTheme} mode`;
            document.body.appendChild(announcement);
            
            // Clean up announcement
            setTimeout(() => {
                document.body.removeChild(announcement);
            }, 3000);
        });
    }
    
    // Add focus visible utility to interactive elements
    document.querySelectorAll('a, button, input, textarea, select, [tabindex]:not([tabindex="-1"])').forEach(element => {
        element.classList.add('focus-visible');
    });
    
    // Add skip to content link for keyboard users
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.className = 'skip-link';
    skipLink.textContent = 'Skip to main content';
    document.body.prepend(skipLink);
    
    // Add ID to main content for skip link
    const mainContent = document.querySelector('main');
    if (mainContent) {
        mainContent.id = 'main-content';
        mainContent.setAttribute('tabindex', '-1');
    }
});
