import os
from selenium import webdriver
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.conf import settings
from .serializers import GoogleResultModelSerializer, GoogleResultReqSerializer
from .models import GoogleResult
from .page import GooglePage
from .scraper import DocumentScraper

geckodriver_path = os.path.join(settings.BASE_DIR, 'demo', 'geckodriver', 'geckodriver.exe')

class GoogleResultApi(mixins.CreateModelMixin, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    Returns the list of query objects objects that have been searched.
    create:
    Searches for a queryset then returns the result.
    """
    queryset = GoogleResult.objects.all().order_by('-created_at')
    serializer_class = GoogleResultModelSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return GoogleResultModelSerializer
        elif self.action == 'create':
            return GoogleResultReqSerializer
        else:
            return self.serializer_class

    def get_queryset(self):
        if self.action == 'list':
            try:
                return self.queryset[0:30]
            except:
                return self.queryset
        else:
            return self.queryset

    def create(self, request, *args, **kwargs):
        driver = webdriver.Firefox(executable_path=geckodriver_path)
        page_instance = GooglePage(driver)
        query_param = request.data.get('query_param', '')
        page_instance.make_search_query(query_param)
        scraper_instance = DocumentScraper(page_instance.get_page_source())
        text_url_list = scraper_instance.get_url_and_text_list()
        try: 
            driver.quit()
        except: 
            pass
        serializer = GoogleResultModelSerializer(data=[{'query_param': query_param, 'text': obj.get('text'), 'url': obj.get('url')} for obj in text_url_list], many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
