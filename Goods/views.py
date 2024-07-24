from django.shortcuts import render, get_object_or_404
from . import models
from django.contrib.auth.models import User

def main(request):
    guest = request.user
    if guest.is_authenticated:
        user_id = guest.id
    else:
        user_id = None
        

    banners = models.Banner.objects.filter(is_active = True)[:5]
    user = get_object_or_404(User, pk=user_id)
    navbar = models.NavbarTop.objects.all()
    footer = models.Footer.objects.all()
    footer_images = models.FooterImages.objects.all()
    categories = models.Category.objects.all()

    context = {}
    context['banners'] = banners
    context['user'] = user
    context['nav_top'] = navbar
    context['categories'] = categories
    context['footer'] = footer
    context['footer_images'] = footer_images

    return render(request, 'index.html', context)
