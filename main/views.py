from socket import errorTab
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework import viewsets
from main.models import *
from main.serializer import *

class SliderView(viewsets.ModelViewSet):
    queryset = Sldier.objects.all()
    serializer_class = SliderSerializer

    def list(self, request):
        slider = Sldier.objects.last()
        sl = SliderSerializer(slider)
        return Response(sl.data)

class AboutProjectView(viewsets.ModelViewSet):
    queryset = AboutProject.objects.all()
    serializer_class = AboutProjectSerializer

    def list(self, request):
        about = AboutProject.objects.all().order_by("-id")[0:2]
        ab = AboutProjectSerializer(about, many=True)
        return Response(ab.data)

class DirectionView(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

    def list(self, request):
        direction = Direction.objects.all().order_by("-id")[0:6]
        dir = DirectionSerializer(direction, many=True)
        return Response(dir.data)

class AboutProject2View(viewsets.ModelViewSet):
    queryset = AboutProject2.objects.all()
    serializer_class = AboutProject2Serializer

    def list(self, request):
        about = AboutProject2.objects.all().order_by("-id")[0:2]
        ab = AboutProject2Serializer(about, many=True)
        return Response(ab.data)

class ZadachaView(viewsets.ModelViewSet):
    queryset = Zadacha.objects.all()
    serializer_class = ZadachaSerializer

    def list(self, request):
        zadacha = Zadacha.objects.all().order_by("-id")[0:10]
        ab = ZadachaSerializer(zadacha, many=True)
        return Response(ab.data)

class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    

    def create(self, request):
        try:
            name = request.data["name"]
            surname = request.data["surname"]
            born = request.data["born"]
            email = request.data["email"]
            address = request.data["address"]
            phone = request.data["phone"]
            answer = request.data['answer']
            ans = Answer.objects.filter(answer=answer, tick=True)
            a = Registration.objects.create(ans=ans, name=name, surname=surname, born=born, email=email, address=address, phone=phone)
            b = RegistrationSerializer(a, many=False)

            return Response(b.data)
        
        except Exception as arr:
            dat = {
                "error": f"{arr}"
            }
            return Response(dat)


class ResultView(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def list(self, request):
        result = Result.objects.all().order_by("-id")[0:5]
        dir = ResultSerializer(result, many=True)
        return Response(dir.data)

class AboutUsView(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    http_method_names = ['get']

    def list(self, request):
        aboutus = AboutUs.objects.last()
        sl = AboutUsSerializer(aboutus)
        return Response(sl.data)

class LinkView(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    http_method_names = ['get']


    def list(self, request):
        link = Link.objects.last()
        sl = LinkSerializer(link)
        return Response(sl.data)

class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ['get']


class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    http_method_names = ['post']




class PismoView(viewsets.ModelViewSet):
    queryset = Pismo.objects.all()
    serializer_class = PismoSerializer
    http_method_names = ['post']


    def list(self, request):
        pismo = Pismo.objects.all()
        ps = PismoSerializer(pismo, many=True)
        return Response(ps.data)
    
 