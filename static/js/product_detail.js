/* Product Detail — Quantity Selector */
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.add-to-cart-form');
    if (!form) return;

    const quantityInput = form.querySelector('.quantity-value');
    const decreaseButton = form.querySelector('.quantity-decrease');
    const increaseButton = form.querySelector('.quantity-increase');

    const step = (delta) => {
        const min = Number(quantityInput.min) || 1;
        const next = Number(quantityInput.value) + delta;
        quantityInput.value = Math.max(min, next);
    };

    decreaseButton.addEventListener('click', () => step(-1));
    increaseButton.addEventListener('click', () => step(1));
});
