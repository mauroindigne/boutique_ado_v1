from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key' : 'pk_test_51HA9qfHlDvQ76wYUpIH7qW0wTZaA67L9gLs0AOVGmLNfTGiev8Xw0w9juSfNCYrEcC8WiJ1OPl7sWFBcWWRpgVjO00jxrilbeS',
    }

    return render(request, template, context)