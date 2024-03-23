from django.http import HttpResponse


def welcome(request):
    return HttpResponse("This is how you customise Welcome page into plain boring one.")
