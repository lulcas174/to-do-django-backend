from rest_framework.routers import DefaultRouter
from core.views import tarefasViewSet
app_name ='core'


router = DefaultRouter(trailing_slash=False)

router.register(r'tarefas',tarefasViewSet)

urlpatterns = router.urls