import pytest
from classes.product import Product


@pytest.mark.parametrize('search,sort_field', [('alcatel', 'name')])
def test_name_alcatel(products_api, search, sort_field):
    r = products_api.get(
        path='js-test-task',
        params={
            'search': search,
            'sort_field': sort_field
        }
    )
    data = r.json()
    products = list(map(lambda x: Product(**x), data['products']))
    assert all(
        list(
            map(
                lambda x: search in x.name.lower(),
                products
            )
        )
    ) is True


@pytest.mark.parametrize('search,sort_field', [('alcatel', 'name')])
def test_sort_name(products_api, search, sort_field):
    r = products_api.get(
        path='js-test-task',
        params={
            'search': search,
            'sort_field': sort_field
        }
    )
    data = r.json()
    products = list(map(lambda x: Product(**x), data['products']))
    sorted_products = sorted(products, key=lambda x: x.name)
    assert sorted_products == products
