"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from .models import Product
from  .models import Cart
@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(10), 'Enough'

        assert not product.check_quantity(1001), 'Not Enough'

        assert product.check_quantity(0), 'Enough'

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900, 'Took'

        product.buy(product.quantity)
        assert product.quantity == 0, 'Took'


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001), 'Not Took'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_cart_add_product(self, product):
        cart().add_product(product)
        print( cart().products.items())
