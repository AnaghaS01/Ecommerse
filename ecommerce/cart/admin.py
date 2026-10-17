from django.contrib import admin
from cart.models import Cart,Payment,Order_details,Wishlist
# Register your models here.

admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Order_details)
admin.site.register(Wishlist)