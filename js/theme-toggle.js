// Theme Toggle Functionality - Immediate Execution
(function() {
    'use strict';
    
    // Apply theme immediately to prevent flash
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    document.body.classList.add(savedTheme === 'dark' ? 'dark-mode' : 'light-mode');
    
    class ThemeToggle {
        constructor() {
            this.currentTheme = savedTheme;
            this.init();
        }

        init() {
            // Wait for DOM to be ready
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', () => this.setup());
            } else {
                this.setup();
            }
        }

        setup() {
            // Create theme toggle button
            this.createToggleButton();
            
            // Attach event listeners
            this.attachEventListeners();
            
            console.log('Theme toggle initialized. Current theme:', this.currentTheme);
        }

        createToggleButton() {
            // Check if button already exists
            if (document.getElementById('theme-toggle')) {
                console.log('Theme toggle button already exists');
                return;
            }

            // Create toggle button HTML
            const toggleBtn = document.createElement('button');
            toggleBtn.id = 'theme-toggle';
            toggleBtn.className = 'theme-toggle-btn';
            toggleBtn.setAttribute('aria-label', 'Toggle theme');
            
            toggleBtn.innerHTML = `
                <i class="bi bi-sun-fill" id="theme-icon-light"></i>
                <i class="bi bi-moon-fill" id="theme-icon-dark"></i>
            `;

            // Add button to body
            document.body.appendChild(toggleBtn);
            
            // Update icon based on current theme
            this.updateToggleIcon(this.currentTheme);
            
            console.log('Theme toggle button created');
        }

        attachEventListeners() {
            const toggleBtn = document.getElementById('theme-toggle');
            if (toggleBtn) {
                toggleBtn.addEventListener('click', () => {
                    console.log('Theme toggle clicked');
                    this.toggleTheme();
                });
            } else {
                console.error('Theme toggle button not found');
            }
        }

        toggleTheme() {
            this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
            console.log('Switching to theme:', this.currentTheme);
            this.applyTheme(this.currentTheme);
            localStorage.setItem('theme', this.currentTheme);
        }

        applyTheme(theme) {
            const html = document.documentElement;
            const body = document.body;
            
            // Set data attribute
            html.setAttribute('data-theme', theme);
            
            // Update body classes
            if (theme === 'dark') {
                body.classList.remove('light-mode');
                body.classList.add('dark-mode');
            } else {
                body.classList.remove('dark-mode');
                body.classList.add('light-mode');
            }

            // Update toggle button icon
            this.updateToggleIcon(theme);
            
            console.log('Theme applied:', theme);
        }

        updateToggleIcon(theme) {
            const lightIcon = document.getElementById('theme-icon-light');
            const darkIcon = document.getElementById('theme-icon-dark');
            
            if (lightIcon && darkIcon) {
                if (theme === 'dark') {
                    lightIcon.style.display = 'none';
                    darkIcon.style.display = 'block';
                } else {
                    lightIcon.style.display = 'block';
                    darkIcon.style.display = 'none';
                }
            }
        }
    }

    // Initialize theme toggle
    new ThemeToggle();
})();
