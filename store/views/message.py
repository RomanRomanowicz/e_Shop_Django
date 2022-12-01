from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect

from store.forms import EmailPostForm
from store.models.products import Product


def post_message(request, id):
    """question to the store"""
    product = get_object_or_404(Product, id=id, available=True)
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(product.get_absolute_url())
            subject = '{} ({}) asks a question: "{}"'.format(cd['your_name'], cd['your_email'], product.name)
            message = 'question: "{}" at {}\n\n{}\'s contents: {}'.format(product.name, post_url, cd['your_name'], cd['question'])
            send_mail(subject, message, 'cop.testow@gmail.com', ['rr.romanowicz@gmail.com', cd['your_email']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'store/message.html', {'product': product, 'form': form, 'sent': sent})


# def contact_message(request):
#     send_mail('cześć', 'message', 'cop.testow@gmail.com', ['rr.romanowicz@gmail.com'], fail_silently=False)
#     return render(request, 'store/test.html')