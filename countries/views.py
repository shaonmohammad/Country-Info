from rest_framework import viewsets, filters
from .models import Country
from .serializers import CountrySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def same_region(self, request, pk=None):
        country = self.get_object()
        countries = Country.objects.filter(region=country.region).exclude(pk=country.pk)
        serializer = self.get_serializer(countries, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='by-language/(?P<lang_code>[^/.]+)')
    def by_language(self, request, lang_code=None):
        countries = Country.objects.filter(languages__icontains=lang_code)
        serializer = self.get_serializer(countries, many=True)
        return Response(serializer.data)

@login_required
def country_list_view(request):
    search = request.GET.get('search',"")
    countries = Country.objects.filter(name__icontains = search)
    return render(request,'country_list.html',{'countries':countries,'search':search})

def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    same_region = Country.objects.filter(region=country.region).exclude(pk=country.pk)
    return render(request, 'country_details.html', {
        'country': country,
        'same_region': same_region,
    })