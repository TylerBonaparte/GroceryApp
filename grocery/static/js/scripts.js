// static/js/scripts.js
document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        var itemInput = document.getElementById('item_name');
        if (itemInput.value.trim() === '') {
            alert('Please enter an item name.');
            event.preventDefault();
        }
    });
});
