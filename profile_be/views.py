from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.views import *
from rest_framework.response import Response
from rest_framework.renderers import *
from .models import *
from .serializer import *


# Create your views here.

class TransactionsTemplateHTMLRender(TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        data = super().get_template_context(data, renderer_context)
        if not data:
            return {}
        else:
            return data


class ContactViewset(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = ContactView.objects.all()
    renderer_classes = (TransactionsTemplateHTMLRender,)
    template_name = "index.html"

    @action(detail=True, methods=['GET'])
    def get_contact(self, request):
        assert isinstance(request, HttpRequest)
        detail = [{"name": detail.name, "email": detail.email, "message": detail.message}
                  for detail in ContactView.objects.all()]
        serializer = ContactSerializer(detail, context={'request': request}, many=True)
        #   return Response({'serializer': serializer, 'detail': detail})
        return render(template_name, {'serializer': serializer})

    @action(detail=True, methods=['POST'])
    def post_contact(self, request):
        assert isinstance(request, HttpRequest)
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
@csrf_exempt
def my(request):
    assert isinstance(request, HttpRequest)
    queryset = ContactView.objects.all()
    serializer_class = ContactSerializer(queryset, many=True)
    if request.method == 'GET':
        detail = [{"name": detail.name, "email": detail.email, "message": detail.message}
                  for detail in ContactView.objects.all()]
        serializer = ContactSerializer(detail, context={'request': request}, many=True)
        return Response(detail)

    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'index.html',
                  {
                      'data': serializer_class.data,
                  }
                  )
"""
