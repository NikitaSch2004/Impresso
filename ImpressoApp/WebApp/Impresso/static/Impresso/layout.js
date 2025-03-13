document.addEventListener('DOMContentLoaded', function() {
    const dropdownButton = document.querySelector('.dropdown-button');
    const menu = document.querySelector('.menu');
    const menuItems = menu.querySelectorAll('li');

    dropdownButton.addEventListener('click', function() {
        if (menu.classList.contains('show')) {
            // Close the menu with an animation
            menu.animate([
                { opacity: 1, maxHeight: '500px' },
                { opacity: 0, maxHeight: '0' }
            ], {
                duration: 1000,
                easing: 'ease'
            }).onfinish = function() {
                menu.classList.remove('show');
                menu.style.opacity = 0;
                menu.style.maxHeight = '0';
                menuItems.forEach((item) => {
                    item.style.opacity = 0; // Reset opacity when menu closes
                });
            };
        } else {
            // Show the menu with an animation
            menu.classList.add('show');
            menu.style.opacity = 0;
            menu.style.maxHeight = '0';
            menu.animate([
                { opacity: 0, maxHeight: '0' },
                { opacity: 1, maxHeight: '500px' }
            ], {
                duration: 1000,
                easing: 'ease'
            }).onfinish = function() {
                menu.style.opacity = 1;
                menu.style.maxHeight = '500px';

                // After menu appears, animate each item one by one
                menuItems.forEach((item, index) => {
                    item.style.opacity = 0; // Start with hidden items
                    item.style.transition = `opacity 0.5s ease ${index * 100}ms`; // Delay each item
                    item.style.opacity = 1; // Fade in items one by one
                });
            };
        }
    });
});
