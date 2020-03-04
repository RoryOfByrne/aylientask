"""Paint URLs

The old API is accessible via /v1/, while the new API (including history 
and authentication) is at /v2/.abspath
"""
from django.contrib import admin
from django.urls import include, path

from paint.apps.authentication.urls import v2 as auth_v2
from paint.apps.batch.urls import v1 as batch_v1
from paint.apps.batch.urls import v2 as batch_v2
from paint.apps.history.urls import v2 as history_v2

# For backwards compatibility
v1 = [
    path('batch/', include(batch_v1))
]

v2 = [
    path('auth/', include(auth_v2)),
    path('batch/', include(batch_v2)),
    path('history/', include(history_v2)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(v1)),
    path('v2/', include(v2))
]
