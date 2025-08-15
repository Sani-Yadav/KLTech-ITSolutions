from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index),
    path('about.html', views.about, name='about'),
    path('service.html', views.service, name='service'),
    path('project.html', views.project, name='project'),
    path('contact.html', views.contact, name='contact'),
    path('blog.html', views.blog, name='blog'),
    path('team.html', views.team, name='team'),
    path('testimonial.html', views.testimonial, name='testimonial'),
    path('404.html', views.error_404, name='404'),
    path('debug/', TemplateView.as_view(template_name='debug.html'), name='debug'),
]

