from django.urls import path

from paint.apps.batch.views import BatchV1

v1 = [
    path('', BatchV1.as_view(), name='v1-batch')
]

v2 = [

]