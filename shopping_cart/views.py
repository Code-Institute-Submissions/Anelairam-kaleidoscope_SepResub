from django.shortcuts import render, redirect

# Create your views here.

def cart(request):
    """The view returns the index page"""
    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})


    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
