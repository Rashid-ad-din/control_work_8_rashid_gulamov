from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Avg
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms.products import ProductForm
from webapp.forms.reviews import ReviewForm
from webapp.models import Product, Review


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('show_product', kwargs={'pk': self.object.pk})


class AddProductView(GroupPermission, SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    model = Product
    extra_context = ()
    groups = ['Модераторы']

    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)
        form.save()
        return super().form_valid(form)


class ProductsView(ListView):
    template_name = 'products/products.html'
    model = Product
    context_object_name = 'products'
    queryset = Product.objects.all()
    paginate_by = 4
    paginate_orphans = 0


class ProductView(DetailView):
    template_name = 'products/product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Product.objects.filter(pk=self.kwargs.get('pk'))[0].reviewed_products.aggregate(
            Avg('rating'))
        context['q'] = p.get('rating__avg')
        return context


class ProductUpdateView(GroupPermission, SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    template_name = 'products/edit_product.html'
    form_class = ProductForm
    model = Product
    groups = ['Модераторы']


class ProductDeleteView(GroupPermission, DeleteView, LoginRequiredMixin):
    template_name = 'products/delete_product.html'
    model = Product
    success_url = reverse_lazy('show_products')
    groups = ['Модераторы']


class ProductAddReviewView(GroupPermission, LoginRequiredMixin, CreateView):
    template_name = 'reviews/add_review.html'
    form_class = ReviewForm
    model = Product
    extra_context = ()
    groups = ['Модераторы']

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            product = self.get_object()
            print(product.title)
            review = form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
            return redirect('show_product', product.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)
