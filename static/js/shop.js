document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('#category-filter input[type="checkbox"]');
    const grid = document.getElementById('product-grid');
    let pagination = document.querySelector('.pagination');

    const orderConfirmedOverlay = document.getElementById('order-confirmed-overlay');
    const orderConfirmedClose = document.getElementById('order-confirmed-close');
    if (orderConfirmedOverlay && orderConfirmedClose) {
        orderConfirmedClose.addEventListener('click', () => orderConfirmedOverlay.remove());
    }

    checkboxes.forEach(cb => {
        cb.addEventListener('change', function () {
            if (cb.checked) {
                // Only one category can be active server-side at a time,
                // so checking one box unchecks the other before fetching.
                checkboxes.forEach(other => {
                    if (other !== cb) other.checked = false;
                });
            }
            const category = cb.checked ? cb.value : null;
            loadProducts(buildUrl(category, 1));
        });
    });

    // Pagination links point at plain shop URLs, so intercept clicks on them
    // and route through the same fetch-based loader instead of reloading.
    document.addEventListener('click', function (event) {
        const link = event.target.closest('.pagination a');
        if (!link) return;

        event.preventDefault();
        loadProducts(link.href);
    });

    function buildUrl(category, page) {
        const url = new URL(window.location.pathname, window.location.origin);
        if (category) url.searchParams.set('category', category);
        if (page) url.searchParams.set('page', page);
        return url.toString();
    }

    function loadProducts(url) {
        fetch(url)
            .then(response => response.text())
            .then(html => {
                // Parse the fetched page and pull out just the pieces that changed.
                const parsed = new DOMParser().parseFromString(html, 'text/html');
                const newGrid = parsed.getElementById('product-grid');
                const newPagination = parsed.querySelector('.pagination');

                if (newGrid) grid.innerHTML = newGrid.innerHTML;
                if (newPagination) {
                    pagination.innerHTML = newPagination.innerHTML;
                }

                // Update the address bar without a full page reload.
                window.history.pushState({}, '', url);
            });
    }
});