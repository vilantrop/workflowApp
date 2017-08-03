from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Shoe

# Create your views here.

def index(request):
    all_shoes = Shoe.objects.all()
#    template = loader.get_template('shoes/index.html')
    context = {
        'all_shoes' : all_shoes,
    }

    return render(request, 'shoes/index.html', context)
#    html = ''
#    for shoes in all_shoes:
#        url = '/main/' + str(shoes.id) +'/'
#        html += '<a href ="' + url +'">' + shoes.name + '</a><br>'

#    return HttpResponse(template.render(context,request))

def detail(request, shoe_id):
    return HttpResponse("<h2>Details for shoe : " + str(shoe_id) + "</h2>")
