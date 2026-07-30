document.addEventListener('DOMContentLoaded', () => {
    // Scroll header effect
    const header = document.querySelector('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Close toast notifications
    const toasts = document.querySelectorAll('.message-toast');
    toasts.forEach(toast => {
        // Auto-close after 5 seconds
        const timeout = setTimeout(() => {
            closeToast(toast);
        }, 5000);

        const closeBtn = toast.querySelector('.message-close-btn');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                clearTimeout(timeout);
                closeToast(toast);
            });
        }
    });

    function closeToast(toast) {
        toast.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(100px)';
        setTimeout(() => {
            toast.remove();
        }, 400);
    }
});
