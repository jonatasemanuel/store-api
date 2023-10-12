import pytest
from app.schemas.category import Category
from app.schemas.product import Product, ProductInput, ProductOutput


def test_product_schema():
    product = Product(
        name='Camisa Mike',
        slug='camisa-mike',
        price=23.99,
        stock=24
    )

    assert product.dict() == {
        'name': 'Camisa Mike',
        'slug': 'camisa-mike',
        'price': 23.99,
        'stock': 24
    }


def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='camisa mike',
            price=23.99,
            stock=24
        )

    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='cão',
            price=23.99,
            stock=24
        )

    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='Camisa-mike',
            price=23.99,
            stock=24
        )


def test_product_schema_invalid_price():
    with pytest.raises(ValueError):
        product = Product(
            name='Camisa Mike',
            slug='camisa-mike',
            price=0,
            stock=24
        )


def test_product_input_schema():
    product = Product(
        name='Camisa Mike',
        slug='camisa-mike',
        price=23.99,
        stock=21
    )

    product_input = ProductInput(
        category_slug='roupa',
        product=product
    )

    assert product_input.model_dump() == {
        "category_slug": "roupa",
        "product": {
            "name": "Camisa Mike",
            "slug": "camisa-mike",
            "price": 23.99,
            "stock": 21
        }
    }


def test_product_output_schema():
    category = Category(name='Roupa', slug='roupa')

    product_output = ProductOutput(
        id=1,
        name='Camisa',
        slug='camisa',
        price=23.99,
        stock=21,
        category=category
    )

    assert product_output.model_dump() == {
        'id': 1,
        'name': 'Camisa',
        'slug': 'camisa',
        'price': 23.99,
        'stock': 21,
        'category': {
            'name': 'Roupa',
            'slug': 'roupa'
        }
    }
