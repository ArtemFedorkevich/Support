from authentication.urls import router


# This routher add paths to routher form authentication.urls
from useractions import views
router.register(r'problems', views.PostList)
router.register(r'problemindetail', views.PostDetailList)
urlpatterns = router.urls
app_name = 'useractions'