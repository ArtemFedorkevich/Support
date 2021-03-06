from rest_framework.routers import DefaultRouter

from authentication import views
app_name = 'authentication'
router = DefaultRouter()
router.register(r'users', views.RegistrationView, basename="user_creation")
router.register(r'login', views.LoginView, basename="user_login")
urlpatterns = router.urls
