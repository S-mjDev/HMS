from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from patient import views as patient_views
from doctor import views as doctor_views


admin.site.site_header = 'QPHN - Hospital Management System'
admin.site.site_title = 'My Site Admin Portal'
admin.site.index_title = 'QPHN Admin Dashboard'


router = routers.DefaultRouter()
router.register(r"users", patient_views.UserViewSet)
router.register(r"groups", patient_views.GroupViewSet)
router.register(r"patient", patient_views.PatientViewSet)
router.register(r"doctor", doctor_views.DoctorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('admin/', admin.site.urls),
]