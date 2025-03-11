// اسکریپت برای کاهش و افزایش تعداد محصولات
document.querySelectorAll('.quantity-btn').forEach(button => {
    button.addEventListener('click', () => {
        const quantityElement = button.parentElement.querySelector('.quantity');
        let quantity = parseInt(quantityElement.textContent);

        if (button.classList.contains('decrease')) {
            if (quantity > 1) {
                quantity--;
            }
        } else if (button.classList.contains('increase')) {
            quantity++;
        }

        quantityElement.textContent = quantity;
    });
});