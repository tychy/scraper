from django.urls import path
from django.views.generic import TemplateView

app_name = 'FB'
urlpatterns = [
    # 一覧
    path('', TemplateView.as_view(template_name='FB/home.html'), name='home'),
    ]
