import django_filters
from .models import Wishes


class WishFilter(django_filters.FilterSet):
    class Meta:
        model = Wishes
        fields = ['status']