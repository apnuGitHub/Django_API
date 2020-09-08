from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime  
from rest_framework.views import APIView
from django.http import HttpResponse  
from .summarisation import summarise




class ParagraphViewAPI(APIView):

    def post(self, request, *args, **kwargs):
        response = {}
        response["status"] = 500
        try:
            data = request.data
            title = data['title']
            para = data['para']

            print("Title:" + title)
            print("Paragraph:"+para)

            summary = summarise(para)
            print("summary:"+summary)
            response['status'] = 200
            response['summary_txt'] = summary
        except Exception as e:
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            #logger.error("ParagraphViewAPI: %s %s", str(e), str(exc_tb.tb_lineno))
        return Response(data=response)


ParaView = ParagraphViewAPI.as_view()

def index(request):  
    #text = Hero.Objects.para
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" %now
    return HttpResponse(html)    # rendering the template in HttpResponse  

class HeroViewSet(viewsets.ModelViewSet):
 #   queryset = Hero.objects.all().order_by('title')
    serializer_class = HeroSerializer

