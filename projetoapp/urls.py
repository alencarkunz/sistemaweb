from django.contrib import admin
from django.urls import path


from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # depois alterar para admin-django > produção
    path('sistema/', include('sistema.urls')), # urls do application principal - index
    path('', RedirectView.as_view(url='/sistema/')), #Add URL maps to redirect the base URL to our application    
]

# Use static() to add url mapping to serve static files during development (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# applications
urlpatterns += [
    path('usuario/', include('sys_usuario.urls')), 
    path('menu/', include('sys_menu.urls')),
    path('modulo/', include('sys_modulo.urls')),
] 

