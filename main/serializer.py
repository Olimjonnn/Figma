from rest_framework import serializers
from main.models import *

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sldier
        fields = "__all__"

class AboutProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutProject
        fields = "__all__"

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"

class AboutProject2Serializer(serializers.ModelSerializer):
    class Meta:
        model = AboutProject2
        fields = "__all__"

class ZadachaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zadacha
        fields = "__all__"

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

class PismoSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Pismo
        fields = "__all__"
