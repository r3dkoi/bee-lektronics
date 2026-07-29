document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('#category-filter input[type="checkbox"]');
    const cards = document.querySelectorAll('#product-grid .product-card');
    const STORAGE_KEY = 'shop-category-filter';

// Only shows applied filtered products (e.g if Phone is checked, only Phones show) //
function applyFilter() {
    const checked = Array.from(checkboxes)
        .filter(cb => cb.checked)
        .map(cb => cb.value.toLowerCase()); //case sensitivity//

    //Saves current selection so it can be restored after a page reload/next page//
    sessionStorage.setItem(STORAGE_KEY, JSON.stringify(checked));

    //goes through each card to decide if it needs to be shown or hidden depending on checked category//
    cards.forEach(card => {
        const show = checked.length === 0 || checked.includes(card.dataset.category);
        card.style.display = show ? '' : 'none';
    });
    }

    //On page load, restore any previously saved selection //
    const saved = JSON.parse(sessionStorage.getItem(STORAGE_KEY) || '[]');

    //re-checks whichever boxes match the saved selection, so UI matches what was previously checked
    checkboxes.forEach(cb => {
        cb.checked = saved.includes(cb.value.toLowerCase());
    });

    //Whenever checkbox is ticked, re-run the filter
    checkboxes.forEach(cb => cb.addEventListener('change', applyFilter));

    //Apply restored filter immediately on load
    applyFilter();
});

