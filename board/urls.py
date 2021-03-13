from django.conf.urls import include, url
from board import views

urlpatterns = [
    url(r'^$', views.index, name = "main"),
    url('^login/$', views.sign_in, name="sign-in"),
    url('^signup/$', views.signup, name="sign-up"),
    url('^new_topic/$', views.new_topic, name="new-topic"),
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic_detail, name = "topic-detail"),
    url(r'^add_post/$', views.add_post, name = "add-post"),
    url(r'^delete_post/$', views.delete_post, name = "delete-post"),
    url(r'^logout/$', views.logout_view, name = "logout"),
    
]
