/* Admin Sales Summary — click a column header to sort the table by it */
document.addEventListener('DOMContentLoaded', () => {
    const table = document.getElementById('sales-table');
    if (!table) return;

    const tbody = table.querySelector('tbody');
    const headers = table.querySelectorAll('th[data-sort]');

    headers.forEach((header, columnIndex) => {
        header.addEventListener('click', () => {
            const direction = header.dataset.sortDir === 'asc' ? 'desc' : 'asc';
            headers.forEach((h) => delete h.dataset.sortDir);
            header.dataset.sortDir = direction;

            const rows = Array.from(tbody.querySelectorAll('tr'))
                .filter((row) => !row.classList.contains('sales-empty-row'));

            rows.sort((rowA, rowB) => {
                const valueA = rowA.children[columnIndex].dataset.value;
                const valueB = rowB.children[columnIndex].dataset.value;
                const numberA = Number(valueA);
                const numberB = Number(valueB);
                const comparison = (valueA !== '' && valueB !== '' && !isNaN(numberA) && !isNaN(numberB))
                    ? numberA - numberB
                    : valueA.localeCompare(valueB);
                return direction === 'asc' ? comparison : -comparison;
            });

            rows.forEach((row) => tbody.appendChild(row));
        });
    });
});