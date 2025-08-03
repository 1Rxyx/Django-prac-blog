from django.contrib import admin
from django.urls import path
from blog.views import frontpage, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),  # 管理者site
    path("", frontpage),
    path("<slug:slug>/", post_detail, name="post_detail"),  # slugを使ったURLパターン
]
