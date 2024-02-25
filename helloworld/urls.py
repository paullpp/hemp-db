from django.urls import path
from . import views
from .views import CompanyCreateView


urlpatterns = [
    path("", views.index, name="index"),

    # List view for all companies
    path('companies/', views.companies, name="companies"),

    # Create view for a new company
    path('companies/create/', CompanyCreateView.as_view(), name='company-create'),

    path('companies/<int:id>', views.view_company, name='company-view'),

    # Delete view for a specific company
    path('remove_companies/<int:id>', views.remove_companies),
]