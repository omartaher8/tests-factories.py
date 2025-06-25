from factory import Factory, Faker
from service.models import Product

class ProductFactory(Factory):
    """Factory class for creating fake Product instances"""
    class Meta:
        model = Product

    name = Faker("word")
    category = Faker("word")
    price = Faker("pyfloat", left_digits=3, right_digits=2, positive=True)
    available = Faker("boolean")
    stock = Faker("random_int", min=0, max=100)
    description = Faker("sentence")
