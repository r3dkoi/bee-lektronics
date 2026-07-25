/* Minicart Overlay */
document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('cart-toggle');
    const overlay = document.getElementById('minicart-overlay');
    if (!toggleButton || !overlay) return;

    const closeButton = document.getElementById('minicart-close');
    const itemsContainer = document.getElementById('minicart-items');
    const itemTemplate = document.getElementById('minicart-item-template');
    const emptyMessage = itemsContainer.querySelector('.minicart-empty');
    const footer = document.getElementById('minicart-footer');
    const subtotalAmount = document.getElementById('minicart-subtotal-amount');

    /* Open / Close */
    const open = () => {
        overlay.hidden = false;
    };

    const close = () => {
        overlay.hidden = true;
    };

    const formatCurrency = (amount) => `$${amount.toFixed(2)}`;

    /* Rendering — takes the JSON shape returned by every /cart/* endpoint
       ({ items: [...], subtotal }) and redraws the item list from scratch.
       The "empty" message is the same <p> that's already in base.html — it's
       only ever shown/hidden, never removed, so there's nothing to recreate. */
    const renderCart = (data) => {
        itemsContainer.querySelectorAll('.minicart-item').forEach((node) => node.remove());
        emptyMessage.hidden = data.items.length > 0;

        if (!data.items.length) {
            footer.hidden = true;
            return;
        }

        data.items.forEach((item) => {
            const node = itemTemplate.content.cloneNode(true);

            node.querySelector('.minicart-item').dataset.productId = item.id;

            const image = node.querySelector('.minicart-item-image');
            image.src = item.image;
            image.alt = item.name;

            node.querySelector('.item-name').textContent = item.name;
            node.querySelector('.item-price').textContent = formatCurrency(item.price);
            node.querySelector('.quantity-value').textContent = item.quantity;

            // +/- re-fetch and re-render on every click rather than mutating the
            // DOM locally, so the session cart stays the single source of truth.
            node.querySelector('.quantity-decrease').addEventListener('click', () => updateQuantity(item.id, item.quantity - 1));
            node.querySelector('.quantity-increase').addEventListener('click', () => updateQuantity(item.id, item.quantity + 1));

            itemsContainer.appendChild(node);
        });

        subtotalAmount.textContent = formatCurrency(data.subtotal);
        footer.hidden = false;
    };

    /* Cart actions — thin wrappers around routes/cart.py, all returning the
       full { items, subtotal } payload so the caller can just renderCart(). */
    const refreshCart = async () => {
        const response = await fetch('/cart/data');
        renderCart(await response.json());
    };

    const updateQuantity = async (productId, quantity) => {
        // quantity <= 0 means "remove"; /cart/update only ever sets positive quantities.
        const endpoint = quantity > 0
            ? `/cart/update/${productId}`
            : `/cart/remove/${productId}`;

        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: quantity > 0 ? JSON.stringify({ quantity }) : undefined,
        });
        renderCart(await response.json());
    };

    // No need to refetch here — every add/update/remove call already
    // re-renders from its own response, so state is kept in sync as it
    // happens rather than re-pulled (and risking a stale response racing
    // an in-flight mutation) each time the panel is opened.
    toggleButton.addEventListener('click', open);
    closeButton.addEventListener('click', close);

    /* Add-to-cart delegation — "Add to Cart" forms live on shop.html and
       product_detail.html, not here, so listen on document and match by
       action instead of binding per-form on pages this file never sees. */
    document.addEventListener('submit', async (event) => {
        const form = event.target.closest('form[action*="/cart/add/"]');
        if (!form) return;

        event.preventDefault();

        // shop.html's grid form has no quantity input, so this is undefined
        // there and /cart/add falls back to its own default of 1.
        const quantityInput = form.querySelector('.quantity-value');
        const options = quantityInput
            ? {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ quantity: Number(quantityInput.value) }),
            }
            : { method: 'POST' };

        const response = await fetch(form.action, options);
        renderCart(await response.json());
        open();
    });

    // Keep the subtotal accurate even before the user opens the overlay.
    refreshCart();
});
