from rest_framework import routers
from pjama.log.views import ResultViewSet,SubmitViewSet,PartialResultViewSet

router = routers.DefaultRouter()
router.register(r'result', ResultViewSet)
router.register(r'submit', SubmitViewSet)
router.register(r'partialresult', PartialResultViewSet)
