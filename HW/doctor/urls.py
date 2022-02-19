from django.contrib import admin
from django.urls import path
from doctor import views

#app_name='doctor'
urlpatterns=[
    #path('admin/',admin.site.urls),
    path('docdab',views.docdab,name="docdab"),
    path('doclogin/',views.doclogin,name="doclogin"),
    path('docregister/',views.doc, name="docregister"),
    path('doconduty/',views.show, name="docshow"),
    path('patshow/',views.patshow,name="patshow"),
    path('docedit/<int:id>/',views.docedit,name="docedit"),
    path('docupdate/',views.docupdate,name="docupdate"),
    path('docdelete/<int:id>/',views.docdestroy,name="docdelete"),
]