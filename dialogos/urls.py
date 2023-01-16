from django.urls import path

from . import views

urlpatterns = [
    path('comment/<int:content_type_id>/<int:object_id>/',
        views.post_comment, name='post_comment'),
    path('comment/<int:comment_id>)/delete/', views.delete_comment,
        name='delete_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment,
        name='edit_comment')
]
