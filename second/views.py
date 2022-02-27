from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views import View
from django.http import HttpResponse

from second.models import Tag, Descriptions
from second.forms import Descriptions_Form
# Create your views here.
class home_view(View):
	# template_name = 'home.html'
	def get(self, request):
		p = self.request.GET.get('p')
		tag = Tag.objects.all()
		descriptions = Descriptions.objects.all()
		# for d in descriptions:
				# print("tag: ", d.tag)
		# print(f"All desc: {descriptions}" )
		descriptions_Form = Descriptions_Form()
		context = {
			'tag':tag,
			"descriptions_Form": descriptions_Form,
			"descriptions" : descriptions,
		}
		return render(request, 'home.html', context)
	
	def post(self, request):
		descriptions_Form = Descriptions_Form(request.POST)
		if descriptions_Form.is_valid():
			descriptions_Form.save()
			print(f"Successfully saved")
			return redirect('/')
		print(f"Does not saved", descriptions_Form)
		return redirect('/')
		
		# return render(request, 'home.html')


# function based views
def home_view_fnc(request):
	tag = Tag.objects.all()
	descriptions = Descriptions.objects.all()
	descriptions_Form = Descriptions_Form()
	if request.method == 'POST':
		descriptions_Form = Descriptions_Form(request.POST)
	context = {
			'tag':tag,
			"descriptions_Form": descriptions_Form,
			"descriptions" : descriptions,
		}
	return render(request, 'home.html', context)