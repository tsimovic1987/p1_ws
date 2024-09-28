from django.contrib import admin
from django.urls import path, include, re_path
from api.resources import NoteResource

note_resource = NoteResource()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    re_path(r'^api/', include(note_resource.urls)),
]