from django.shortcuts import render, get_object_or_404
from .models import Testimonial, Profession


# Create your views here.
def testimonial(request):
    testimonials= Testimonial.objects.all()
    return render(request ,"testimonial/testimonial.html", {'listTestimonial':testimonials})
