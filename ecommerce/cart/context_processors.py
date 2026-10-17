from cart.models import Cart, Wishlist


def count_items(request):
    u = request.user
    count = 0
    w_count = 0
    if request.user.is_authenticated:
        try:
            c = Cart.objects.filter(user=u)
            for i in c:
                count += i.quantity
            w_count = Wishlist.objects.filter(user=u).count()
        except:
            count = 0
            w_count = 0
    else:
        session_wishlist = request.session.get('wishlist', None)
        if session_wishlist is None:
            w_count = 1  # Pre-loaded 1 handbag
        else:
            w_count = len(session_wishlist)
    return {'c': count, 'w_count': w_count}


