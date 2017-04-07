from django.contrib import admin
from wedding.models import Rsvp, GiftOrder, Gift, GiftOrderItem, Cart, CartItem

# Register your models here.
admin.site.register(Rsvp)
admin.site.register(Gift)
admin.site.register(GiftOrder)
admin.site.register(GiftOrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)

