from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class HelloWorld(APIView):
    def get(self, request):
        return Response(data="Hello World!", status=200)

    def patch(self, request):
        return Response(data="Estoy en el Patch", status = 200)

    def delete(self,request):
        return Response(data = "Estoy en el Delete", status = 200)

    def post(self, request):
        return Response(data = "Estoy en el Post", status = 200)

class PetView(APIView):
    def get(self, request):
        return Response(data="Hello World!", status=200)

    def patch(self, request):
        return Response(data="Estoy en el Patch", status = 200)

    def delete(self,request):
        return Response(data = "Estoy en el Delete", status = 200)

    def post(self, request):
        return Response(data = "Estoy en el Post", status = 200)
    

class PersonView(APIView):
    def get(self, request):
        return Response(data="Hello World!", status=200)

    def patch(self, request):
        return Response(data="Estoy en el Patch", status = 200)

    def delete(self,request):
        return Response(data = "Estoy en el Delete", status = 200)

    def post(self, request):
        return Response(data = "Estoy en el Post", status = 200)
