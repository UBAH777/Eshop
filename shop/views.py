from django.shortcuts import render, redirect
from .models import Item, Category, Vendor
from django.db.models import Q
from .forms import ReviewForm, RatingForm
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


class VendorCategory:
    """"""
    def get_vendors(self):
        return Vendor.objects.all()
    
    def get_categories(self):
        return Category.objects.all()


class ItemsView(VendorCategory, ListView):
    """"""
    model = Item
    queryset = Item.objects.all()
    paginate_by = 3
    

class ItemDetailView(DetailView):
    """"""
    model = Item
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        context["star_form"] = RatingForm()
        return context


class AddReview(View):
    """"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        item = Item.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.item = item
            form.save()
        return redirect("/")
    

class VendorView(DetailView):
    """"""
    model = Vendor
    template_name = 'shop/vendor.html'
    slug_field = "title"
    context_object_name = "vendor"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_list"] = Item.objects.filter(vendor_id=1)
        return context
    

class FilterItemsView(VendorCategory, ListView):
    """"""
    paginate_by = 3

    def get_queryset(self):
        my_q = Q()
        if 'vendor' in self.request.GET:
            my_q = Q(vendor_id__in=self.request.GET.getlist("vendor"))
        if 'category' in self.request.GET:
            my_q &= Q(category_id__in=self.request.GET.getlist("category"))
        #queryset = Item.objects.filter(
        #    Q(vendor_id__in=self.request.GET.getlist("vendor")) |
        #    Q(category_id__in=self.request.GET.getlist("category"))
        #).distinct()
        queryset = Item.objects.filter(my_q).distinct()
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["vendor"] = ''.join([f"vendor={x}&" for x in self.request.GET.getlist("vendor")])
        context["category"] = ''.join([f"category={x}&" for x in self.request.GET.getlist("category")])
        return context


class Search(VendorCategory, ListView):
    paginate_by = 3

    def get_queryset(self):
        return Item.objects.filter(title__icontains=self.request.GET.get("q"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
