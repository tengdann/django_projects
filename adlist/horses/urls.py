from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.HorseListView.as_view()),
    path('horses', views.HorseListView.as_view(), name='horses'),
    path('horses/<int:pk>', views.HorseDetailView.as_view(), name='horse_detail'),
    path('horses/create',
        views.HorseFormView.as_view(success_url=reverse_lazy('horses')), name='horse_create'),
    path('horses/<int:pk>/update',
        views.HorseFormView.as_view(success_url=reverse_lazy('horses')), name='horse_update'),
    path('horses/<int:pk>/delete',
        views.HorseDeleteView.as_view(success_url=reverse_lazy('horses')), name='horse_delete'),
    path('horses/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('autos')), name='comment_delete'),
]