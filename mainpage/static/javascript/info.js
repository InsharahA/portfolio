document.addEventListener('DOMContentLoaded', () => {
    const slidingBackground =document.querySelector('.right');
    if (!slidingBackground) {
        console.error('Element with id "right" not found');
        return;
    }

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                console.log('Animation triggered!');
                slidingBackground.style.animation = 'none'; // Reset animation
                void slidingBackground.offsetWidth; // Trigger reflow
                slidingBackground.style.animation = 'slideBackground 2s ease-out forwards';
            }
        });
    }, {
        threshold: 0.3
    });

    observer.observe(slidingBackground);
});
