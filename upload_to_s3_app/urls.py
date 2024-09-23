from django.urls import path

from upload_to_s3_app.views import FileUploadView

urlpatterns = [
    path('upload_file/', FileUploadView.as_view(), name='upload_file'),
]