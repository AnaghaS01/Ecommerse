import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from shop.models import Category, Product

cat = Category.objects.get(name='Bags')
prod, created = Product.objects.get_or_create(
    name='Crossbody Sling Bag',
    category=cat,
    defaults={
        'description': 'A stylish and versatile crossbody sling bag featuring an adjustable strap, gold accents, and compact compartments for everyday convenience.',
        'price': 699.00,
        'stock': 12,
        'available': True,
        'image': 'products/sling_crossbody.jpg',
    }
)

if not created:
    prod.price = 699.00
    prod.stock = 12
    prod.image = 'products/sling_crossbody.jpg'
    prod.save()

print(f"Product '{prod.name}' added to category '{cat.name}' at Rs. {prod.price}.")
