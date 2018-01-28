from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='person_changelist'), name='home'),
    path('hr/', include('hr.urls')),
]
