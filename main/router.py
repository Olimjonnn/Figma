from rest_framework import routers
from main.views import *

router = routers.DefaultRouter()

router.register("slider",SliderView)
router.register("aboutproject", AboutProjectView)
router.register("direction", DirectionView)
router.register("aboutproject2", AboutProject2View)
router.register("zadacha", ZadachaView)
router.register("registration", RegistrationView)
router.register("result", ResultView)
router.register("aboutus", AboutUsView)
router.register("link", LinkView)
router.register("question", QuestionView)
router.register("answer", AnswerView)
router.register("pismo", PismoView)
router.register("logo", LogoView)