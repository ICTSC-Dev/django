from rest_framework import routers
from pjama.account.views import TeamViewSet

router = routers.DefaultRouter()
router.register(r'team', TeamViewSet)
