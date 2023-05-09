urlpatterns = [
    path("cat/", CatView.as_view()),
    path("dog/", DogView.as_view()),
]