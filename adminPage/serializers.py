from rest_framework import serializers
from .models import Slider, Slide, SlideDetail, LatestCourse

class SlideDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideDetail
        fields = '__all__'
        read_only_fields = ('slide',)  # 'slide' 필드를 읽기 전용으로 설정

class SlideSerializer(serializers.ModelSerializer):
    detail = SlideDetailSerializer(read_only=True)  # SlideDetail 정보를 포함

    class Meta:
        model = Slide
        fields = '__all__'
        extra_kwargs = {'slider': {'read_only': True}}

class SliderSerializer(serializers.ModelSerializer):
    slides = SlideSerializer(many=True, read_only=True, source='slide_set')  # 'slide_set'는 Slider 모델과 연결된 Slide 객체들을 나타냅니다.

    class Meta:
        model = Slider
        fields = ['id', 'sliderName', 'assignToPage', 'createdDate', 'updatedDate', 'slides']


class LatestCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestCourse
        fields = '__all__'
