from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from app.forms import *
# Create your views here.

# returning string as a response Function based view
def srting_viewFBV(request):
    return HttpResponse('Rendering the https response by Function based view')

# returning string as a response Class based view
class string_viewCBV(View):
    def get(self,request):
        return HttpResponse('Returning http response by using class based View')

# returning template by function Based view
def Template_FBV(request):
    return render(request,'Template_FBV.html')

# returning Template using class based views
class Template_CBV(View):
    def get(self,request):
        return render(request, 'Template_CBV.html')


# inserting data by Function based view
def InsertData_By_FBV(request):
    IFDO=StudentModelForm()
    d={'IFDO':IFDO}

    if request.method=='POST':
        SFDO=StudentModelForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Student created')
        else:
            return HttpResponse('Innvalid data')

    return render(request,'InsertData_By_FBV.html',d)

#inserting Data by using Class based view
class InsertData_By_CBV(View):
    def get(self,request):
        IFDO=StudentModelForm()
        d={'IFDO':IFDO}
        return render(request,'InsertData_By_CBV.html',d)

        def post(self,request):
            SFDO=StudentModelForm(request.POST)
            if SFDO.is_valid():
                SFDO.save()
                return HttpResponse('Studet will created')
            else:
                return HttpResponse('invalid data')
                
# rendering Template by Template View 
class Render_Template_By_TemplateView(TemplateView):
    template_name='Render_Template_By_TemplateView.html'

