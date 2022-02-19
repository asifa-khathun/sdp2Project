from django.contrib import admin
from django.urls import path
from patient import views
from django.conf import settings
from django.conf.urls.static import static
from HW.settings import MEDIA_URL,MEDIA_ROOT

#app_name='patient'
urlpatterns=[
    #path('admin/',admin.site.urls),
    #path('',views.patdab,name="patdab"),
    path('patdab/',views.patdab,name="patdab"),
    path('patlogin/',views.patlogin,name="patlogin"),
    path('patregister/',views.pat,name="patregister"),
    path('patedit/<int:id>/',views.patedit,name="patedit"),
    path('patupdate/',views.patupdate,name="patupdate"),
    path('patdelete/<int:id>/',views.patdestroy,name="patdelete"),
    path('docconsult/',views.consult,name="docconsult"),
    path('uploadpres/',views.uploadpres,name="uploadpres"),
    path('viewppres/',views.viewppres,name="viewppres"),
    path('medicines/',views.medicines,name="medicines"),
    path('services/',views.services,name="services"),
    path('test/',views.test,name="test"),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
