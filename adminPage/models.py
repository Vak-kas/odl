from django.db import models

# Create your models here.
class Slider(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    sliderName = models.CharField(max_length=50, verbose_name="슬라이더 이름")
    assignToPage = models.CharField(max_length=50, blank = True, null = True, verbose_name="할당된 페이지")
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜")
    updatedDate = models.DateTimeField(blank=True, null=True, verbose_name="업데이트 날짜")

    def __str__(self):
        return self.sliderName




class Slide(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, verbose_name="소속 슬라이더")
    image = models.ImageField(upload_to='slides/', verbose_name="이미지")
    sloganHeading = models.CharField(max_length=100, verbose_name="올릴 내용")
    caption = models.CharField(max_length=100, verbose_name="올릴 내용")
    description = models.TextField(blank=True, verbose_name="설명")
    link = models.URLField(blank=True, verbose_name="링크")
    order = models.IntegerField(default=0, verbose_name="순서")
    isActive = models.BooleanField(default=True, verbose_name="활성 상태")
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜")
    updatedDate = models.DateTimeField(blank=True, null=True, verbose_name="업데이트 날짜")

    def __str__(self):
        return f"{self.slider.slideName} - {self.title}"


from django.db import models

class SlideDetail(models.Model):
    slide = models.OneToOneField(Slide, on_delete=models.CASCADE, related_name='detail')
    textAlign = models.CharField(max_length=50, default='center', verbose_name="텍스트 정렬")
    textSize = models.IntegerField(default=11, verbose_name="텍스트 크기")  # int 형으로 변경
    textColor = models.CharField(max_length=20, default='black', verbose_name="텍스트 색상")
    imageHeight = models.IntegerField(default=500, verbose_name="이미지 높이")

    def __str__(self):
        return f"Detail for {self.slide.sloganHeading}"

