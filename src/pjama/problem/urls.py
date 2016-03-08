from rest_framework import routers
from pjama.problem.views import ProblemViewSet,PartialPointViewSet

router = routers.DefaultRouter()
router.register(r'problem', ProblemViewSet)
router.register(r'partialpoint', PartialPointViewSet)
