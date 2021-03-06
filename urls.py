from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.detail, name="details"),
    path('addmovies/', views.add_movie, name="add_movie"),
    path('addreview/<int:id>/', views.addReview, name="add_review"),
    path('addreleasedate/<int:id>/', views.add_release_date, name="add_release_date"),
    path('addsoundtrack/<int:id>/', views.add_soundtrack, name="add_soundtrack"),
    path('addproduction/<int:id>/', views.add_production, name="add_production"),
    path('addawardandcategory/<int:id>/', views.add_award_and_category, name="add_award_and_category"),
    path('addmoviecast/<int:id>/', views.add_movie_cast, name="add_movie_cast"),
    path('addmoviecrew/<int:id>/', views.add_movie_crew, name="add_movie_crew"),
    path('editmovie/<int:id>/', views.edit_movie, name="edit_movie"),
    path('deletemovie/<int:id>/', views.delete_movie, name="delete_movie"),
    path('editreleasedate/<int:id>/', views.edit_release_date, name="edit_release_date"),
    path('editsoundtrack/<int:id>/', views.edit_soundtrack, name="edit_soundtrack"),
    path('addsoundtrack/<int:id>/', views.add_soundtrack, name="add_soundtrack"),
    path('addkeywords/<int:id>/', views.add_keywords, name="add_keywords"),
    path('addcountry/<int:id>/', views.add_country, name="add_country"),
    path('addrating/<int:id>/', views.addRating, name="add_rating"),
    path('editreview/<int:movie_id>/<int:review_id>/', views.edit_review, name="edit_review"),
    path('deletereview/<int:movie_id>/<int:review_id>/', views.delete_review, name="delete_review")
    # path('add_info/<int:id>/', views.addInfo, name="add_info")
]
