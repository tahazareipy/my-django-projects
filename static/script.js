document.addEventListener('DOMContentLoaded', function() {
    var toggleButton = document.getElementById('toggleUsers');
    var userListContainer = document.getElementById('userListContainer');
    
    toggleButton.addEventListener('click', function() {
        if (userListContainer.classList.contains('hidden')) {
            userListContainer.classList.remove('hidden');
        } else {
            userListContainer.classList.add('hidden');
        }
    });
});
