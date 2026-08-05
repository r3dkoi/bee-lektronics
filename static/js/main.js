/* Hamburger Nav */
document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.getElementById('nav-toggle');
    const navLinks = document.getElementById('navbar-links');
    if (!navToggle || !navLinks) return;

    const closeMenu = () => {
        navLinks.classList.remove('is-open');
        navToggle.classList.remove('is-active');
        navToggle.setAttribute('aria-expanded', 'false');
    };

    navToggle.addEventListener('click', () => {
        const isOpen = navLinks.classList.toggle('is-open');
        navToggle.classList.toggle('is-active', isOpen);
        navToggle.setAttribute('aria-expanded', String(isOpen));
    });

    // collapse the menu once a link inside it is used to navigate
    navLinks.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', closeMenu);
    });
});

/* Carousel Feature */
document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.querySelector('.carousel-featured');
    if (!carousel) return;

    const wrapper = carousel.closest('.carousel-wrapper');
    const items = carousel.querySelectorAll('.carousel-item');
    const prevButton = wrapper.querySelector('.carousel-prev');
    const nextButton = wrapper.querySelector('.carousel-next');
    const dotsContainer = wrapper.querySelector('.carousel-dots');

    const intervalMs = 4000;
    let timer = null;

    const scrollToIndex = (index) => {
        items[index].scrollIntoView({ behavior: 'smooth', inline: 'start', block: 'nearest' });
    };

    // Maps scroll position to a dot index by progress (0 at the very start, the
    // last index at the very end) rather than "which item leads the visible
    // window" — with several items visible at once, that would peg the active
    // dot to an early item even once the carousel is fully scrolled to the end.
    const currentIndex = () => {
        const maxScrollLeft = carousel.scrollWidth - carousel.clientWidth;
        if (maxScrollLeft <= 0) return 0;
        return Math.round((carousel.scrollLeft / maxScrollLeft) * (items.length - 1));
    };

    const advance = () => {
        const atEnd = carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 1;
        scrollToIndex(atEnd ? 0 : currentIndex() + 1); // loop back to the start at the end
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

    // dots: one per item, clicking jumps straight to that item
    const dots = Array.from(items).map((_, index) => {
        const dot = document.createElement('button');
        dot.type = 'button';
        dot.setAttribute('aria-label', `Go to product ${index + 1}`);
        dot.addEventListener('click', () => {
            stop();
            scrollToIndex(index);
        });
        dotsContainer.appendChild(dot);
        return dot;
    });

    const updateActiveDot = () => {
        const active = currentIndex();
        dots.forEach((dot, index) => dot.classList.toggle('is-active', index === active));
    };

    // buttons: always work, regardless of the reduced-motion / auto-advance setting above
    prevButton.addEventListener('click', () => {
        stop();
        scrollToIndex(Math.max(0, currentIndex() - 1));
    });

    nextButton.addEventListener('click', () => {
        stop();
        scrollToIndex(Math.min(items.length - 1, currentIndex() + 1));
    });

    carousel.addEventListener('scroll', updateActiveDot);

    // pause auto-advance whenever the user is actively engaging with the carousel
    carousel.addEventListener('mouseenter', stop);
    carousel.addEventListener('mouseleave', start);
    carousel.addEventListener('focusin', stop);
    carousel.addEventListener('focusout', start);
    carousel.addEventListener('touchstart', stop, { passive: true });

    updateActiveDot();
    start();
});
