from django.urls import path, include
from rest_framework_nested import routers
from .views import SliderViewSet, SlideViewSet, SlideDetailViewSet, LatestCourseViewSet


router = routers.SimpleRouter()
router.register(r'sliders', SliderViewSet)

slides_router = routers.NestedSimpleRouter(router, r'sliders', lookup='slider')
slides_router.register(r'slides', SlideViewSet, basename='slider-slides')


details_router = routers.NestedSimpleRouter(slides_router, r'slides', lookup='slide')
details_router.register(r'detail', SlideDetailViewSet, basename='slide-details')

latest_router = routers.SimpleRouter()
latest_router.register(r'latest', LatestCourseViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(slides_router.urls)),
    path('', include(details_router.urls)),
    path('', include(latest_router.urls)),
]

