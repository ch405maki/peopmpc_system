from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('create/', views.create_member, name='create_member'),
    path('detail/', views.member_detail, name='member_detail'),
    path('update/<int:pk>/', views.MemberUpdateView.as_view(), name='update_member'),
    path('delete/<int:pk>/', views.MemberDeleteView.as_view(), name='delete_member'),
    path('view/<int:pk>/', views.MemberDetailView.as_view(), name='view_member'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
