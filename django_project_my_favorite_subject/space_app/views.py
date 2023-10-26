from django.http import HttpResponse
from django.template import loader
from .models import Mission

def space_app(request):
  mission = Mission.objects.all().values()
  template = loader.get_template('all_mission.html')
  context = {
    'mission': mission,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mission = Mission.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mission': mission,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def image_collection(request):
  template = loader.get_template('image_collection.html')
  context = {
    'image_collection': image_collection,
  }
  return HttpResponse(template.render(context, request))  