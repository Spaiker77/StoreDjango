// Анимация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    // Плавное появление карточек
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });

    // Подтверждение при добавлении товара
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productName = this.getAttribute('data-product');
            alert(`Товар "${productName}" добавлен в корзину!`);
        });
    });
});