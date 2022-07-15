from .views import *
urlpatterns = [
        ('cars/', cars_listing),
        ('cars-create/', cars_create),
        ('cars-retrieve/id', cars_retrieve),
        ('cars-update/id', cars_update),
        ('delete-delete/id', cars_delete),
]