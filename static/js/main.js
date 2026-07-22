/* Carousel Feature */
document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.querySelector('.carousel-featured');
    if (!carousel) return;

    const intervalMs = 4000;
    let timer = null;

    const advance = () => {
        const items = carousel.querySelectorAll('.carousel-item');
        const itemWidth = items[0]?.getBoundingClientRect().width + 24; // 24 = the CSS gap value
        const atEnd = carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 1;

        carousel.scrollTo({
            left: atEnd ? 0 : carousel.scrollLeft + itemWidth, // loop back to the start at the end
            behavior: 'smooth',
        });
    };

    const start = () => {
        // don't auto-animate for users who've asked the OS to reduce motion
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
        stop();
        timer = setInterval(advance, intervalMs);
    };

    const stop = () => {
        if (timer) clearInterval(timer);
        timer = null;
    };

    // pause auto-advance whenever the user is actively engaging with the carousel
    carousel.addEventListener('mouseenter', stop);
    carousel.addEventListener('mouseleave', start);
    carousel.addEventListener('focusin', stop);
    carousel.addEventListener('focusout', start);
    carousel.addEventListener('touchstart', stop, { passive: true });

    start();
});