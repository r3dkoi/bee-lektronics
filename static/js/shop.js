document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('#category-filter input[type="checkbox"]');
    const cards = document.querySelectorAll('#product-grid .product-card');

// Only shows applied filtered products (e.g if Phone is checked, only Phones show) //
function applyFilter() {
    const checked = Array.from(checkboxes)
        .filter(cb => cb.checked)
        .map(cb => cb.value.toLowerCase());

    cards.forEach(card => {
        const show = checked.length === 0 || checked.includes(card.dataset.category);
        card.style.display = show ? '' : 'none';
    });
    }

    checkboxes.forEach(cb => cb.addEventListener('change', applyFilter));
});

