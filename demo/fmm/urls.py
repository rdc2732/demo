from django.conf.urls import url

from . import views
app_name = 'fmm'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^loadfmm', views.loadfmm, name='loadfmm'),

]
