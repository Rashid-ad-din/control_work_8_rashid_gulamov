from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms.reviews import ReviewForm
from webapp.models import Review, Product


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('show_product', kwargs={'pk': self.object.product.pk})


class ReviewsView(ListView):
    template_name = 'reviews/reviews.html'
    model = Review
    context_object_name = 'reviews'
    queryset = Review.objects.all()
    paginate_by = 4
    paginate_orphans = 0


class ReviewView(DetailView):
    template_name = 'reviews/review.html'
    model = Review


class ReviewUpdateView(GroupPermission, SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    template_name = 'reviews/edit_review.html'
    form_class = ReviewForm
    model = Review
    groups = ['admin', 'user']


class ReviewDeleteView(GroupPermission, DeleteView, LoginRequiredMixin):
    template_name = 'reviews/delete_review.html'
    model = Review
    success_url = reverse_lazy('show_products')
    groups = ['admin', 'user']
