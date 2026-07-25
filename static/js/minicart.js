/* Minicart Overlay */
document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('cart-toggle');
    const overlay = document.getElementById('minicart-overlay');
    if (!toggleButton || !overlay) return;

    const closeButton = document.getElementById('minicart-close');
    const itemsContainer = document.getElementById('minicart-items');
    const itemTemplate = document.getElementById('minicart-item-template');
    const footer = document.getElementById('minicart-footer');
    const subtotalAmount = document.getElementById('minicart-subtotal-amount');

    const open = () => {
        overlay.hidden = false;
    };

    const close = () => {
        overlay.hidden = true;
    };

    toggleButton.addEventListener('click', open);
    closeButton.addEventListener('click', close);

    // TODO: fetch cart contents and populate itemsContainer via itemTemplate
    // TODO: wire quantity-increase / quantity-decrease per item
    // TODO: update subtotalAmount and toggle footer visibility based on cart state
});
