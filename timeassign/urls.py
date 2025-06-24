from django.urls import re_path
from django.contrib import admin
from django.urls import path
from ta_app import views

urlpatterns = [
  re_path(r'^admin/', admin.site.urls),
  path("", views.Home.as_view()),
  path("menu/",views.MenuView.as_view()),
  path("addUser/", views.addUserView.as_view()),
  path("addCourse/", views.addCourseView.as_view()),
  path("viewCourse/", views.viewCourses.as_view()),
  path("editCourse/", views.editCourses.as_view()),
  path("viewUsers/", views.viewUsersView.as_view()),
  path("chair_assignToCourse/", views.chair_assignToCourseView.as_view()),
  path("instructor_assignToCourse/", views.instructor_assignToCourseView.as_view()),
  path("logout/", views.logoutView.as_view()),
  path("validate/", views.runValidate.as_view()),
  path("editSchedule/", views.editScheduleView.as_view()),
  path("addBreak/", views.addBreak.as_view()),
  path("editBreak/", views.editBreak.as_view())

]
