from django.shortcuts import render,HttpResponse, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Slider, Slide, SlideDetail
from .serializers import SliderSerializer, SlideSerializer, SlideDetailSerializer
from django.utils import timezone
from rest_framework import viewsets



# Create your views here.
def index(request):
    return HttpResponse("안녕하세요 로그인에 오신것을 환영합니다.")





class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

    def create(self, request, *args, **kwargs):
        # 요청 데이터로부터 시리얼라이저 인스턴스 생성
        serializer = self.get_serializer(data=request.data)
        # 데이터 유효성 검증
        serializer.is_valid(raise_exception=True)
        # 유효한 데이터의 경우, 저장
        self.perform_create(serializer)
        # HTTP 201 Created 상태 코드와 함께 생성된 객체의 데이터 반환
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        # 객체 저장. 'perform_create'를 오버라이드하여 커스텀 저장 로직을 적용할 수 있음
        serializer.save()


    def update(self, request, *args, **kwargs):
        slider_instance = self.get_object()

        # 클라이언트로부터 받은 데이터로 객체 업데이트
        serializer = self.get_serializer(slider_instance, data=request.data, partial=kwargs.pop('partial', False))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # updatedDate 필드를 현재 시간으로 업데이트
        slider_instance.updatedDate = timezone.now()
        slider_instance.save()

        # 업데이트된 객체 정보 반환
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Slider가 성공적으로 삭제되었습니다.'}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        slider = self.get_object()  # 요청받은 ID에 해당하는 Slider 인스턴스를 가져옵니다.
        serializer = self.get_serializer(slider)  # Slider 인스턴스를 직렬화합니다.

        # 연결된 Slide 인스턴스들을 가져오고 직렬화합니다.
        slides = Slide.objects.filter(slider=slider)
        slide_serializer = SlideSerializer(slides, many=True)

        # Slider 데이터와 연결된 Slide 데이터를 함께 반환합니다.
        response_data = serializer.data
        response_data['slides'] = slide_serializer.data  # 'slides' 키에 Slide 데이터를 추가합니다.
        return Response(response_data)



class SlideViewSet(viewsets.ModelViewSet):
    serializer_class = SlideSerializer

    def get_queryset(self):
        queryset = Slide.objects.filter(slider_id=self.kwargs['slider_pk'])
        queryset = queryset.order_by('order')
        return queryset

    def perform_create(self, serializer):
        # URL에서 slider_id를 가져옵니다.
        slider_id = self.kwargs.get('slider_pk')
        # 해당 ID를 가진 Slider 인스턴스를 가져옵니다.
        slider = get_object_or_404(Slider, pk=slider_id)
        # Slide 객체를 저장하며 Slider 인스턴스를 연결합니다.
        serializer.save(slider=slider)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.updatedDate = timezone.now()
        instance.save()

        return super(SlideViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        slide_instance = self.get_object()
        slider_id = slide_instance.slider.id
        order_to_update = slide_instance.order

        # 선택한 슬라이드를 삭제합니다.
        slide_instance.delete()

        # 삭제된 슬라이드의 order보다 큰 슬라이드들의 order를 갱신합니다.
        slides_to_update = Slide.objects.filter(slider_id=slider_id, order__gt=order_to_update)
        for slide in slides_to_update:
            slide.order -= 1
            slide.save()

        return Response({'message': 'Slide가 성공적으로 삭제되었습니다.'},status=status.HTTP_204_NO_CONTENT)



class SlideDetailViewSet(viewsets.ModelViewSet):
    queryset = SlideDetail.objects.all()
    serializer_class = SlideDetailSerializer

    def perform_create(self, serializer):
        # URL에서 slide_id를 가져옵니다. 'slide_pk'는 NestedSimpleRouter의 lookup 설정에 따라 결정됩니다.
        slide_id = self.kwargs.get('slide_pk')  # 'slide_pk'로 수정
        slide = get_object_or_404(Slide, pk=slide_id)
        serializer.save(slide=slide)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # 부분 업데이트(PATCH)를 지원할 지 결정합니다.
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # 인스턴스가 prefetch_related()를 사용하여 캐시된 경우, 이를 제거하여 업데이트된 인스턴스를 반영합니다.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)







