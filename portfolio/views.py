from django.shortcuts import render, redirect
from .models import *
import mimetypes
import os
from wsgiref.util import FileWrapper
from django.http import StreamingHttpResponse
from .forms import *
from django.http import JsonResponse


# Create your views here.
def index(request):

    # if request.method == "POST":
    #     full_name = request.POST['full_name']
    #     email_address = request.POST['email_address']
    #     phone_number = request.POST['phone_number']
    #     message = request.POST['message']

    #     contact_us = ContactUs(full_name=full_name, email_address=email_address, phone_number=phone_number, message=message)
    #     contact_us.save()
    #     return redirect("/")

    print(request.POST)
    form = ContactUsForm()
    if request.method == "POST" and request.is_ajax():
        form = ContactUsForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            form.save()
            return JsonResponse({"full_name": full_name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)



    copyright = CopyRight.objects.first()
    contact_info = ContactInformation.objects.all()
    portfolios = Portfolio.objects.all()
    services = Service.objects.all()
    about = About.objects.first()
    banners = BannerPortion.objects.all()


    context = {
        'copyright': copyright,
        'contact_info': contact_info,
        'portfolios': portfolios,
        'services': services,
        'about': about,
        'banners': banners,
        'form': form,
    }
    return render(request, 'portfolio/index.html', context)

def download_resume(request):
  base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  filename = 'django developer.pdf'
  filepath = base_dir + '/resume/' + filename
  thefile = filepath
  filename = os.path.basename(thefile)
  chunk_size = 8192
  response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'),chunk_size), content_type=mimetypes.guess_type(thefile)[0])
  response['Content-Length'] = os.path.getsize(thefile)
  response['Content-Disposition'] = "attachment; filename=%s" % filename
  return response