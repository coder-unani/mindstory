from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Page
from .forms import PageForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "diary/index.html"

class InfoView(TemplateView):
    template_name = "diary/info.html"
    
class PageListView(ListView):
    model = Page
    template_name = "diary/page_list.html"
    # context_object_name = "page"
    ordering = "-dt_created"
    paginate_by = 8
    # page_kwarg = "page"

class PageCreateView(CreateView):
    model = Page
    template_name = "diary/page_form.html"
    form_class = PageForm

    def get_success_url(self):
        return reverse("page-detail", kwargs={"pk": self.object.id})

class PageDetailView(DetailView):
    model = Page
    template_name = "diary/page_detail.html"
    # context_object_name = "page"

class PageUpdateView(UpdateView):
    model = Page
    template_name = "diary/page_form.html"
    form_class = PageForm

    def get_success_url(self):
        return reverse("page-detail", kwargs={"pk": self.object.id})
    
class PageDeleteView(DeleteView):
    model = Page
    template_name = "diary/page_confirm_delete.html"
    # context_object_name = "page"
    
    def get_success_url(self):
        return reverse("page-list")
    
# def index(request):
#     return render(request, "diary/index.html")                   
# def page_list(request):
#     pages = Page.objects.all()
#     paginator = Paginator(pages, 8)
#     curr_page_num = request.GET.get("page", 1)
#     page = paginator.page(curr_page_num)
#     return render(request, "diary/page_list.html", { "page": page})
# def page_create(request):
#     if request.method == "POST":
#         form_data = PageForm(request.POST)
#         if form_data.is_valid():
#             new_page = form_data.save()
#             return redirect("page-detail", page_id = new_page.id)
#     else:
#         form_data = PageForm()
#     return render(request, "diary/page_form.html", { "form": form_data })
# def page_detail(request, page_id):
#     page = Page.objects.get(id=page_id)
#     context = {
#         "page": page,
#     }
#     return render(request, "diary/page_detail.html", context)
# def page_update(request, page_id):
#     page = Page.objects.get(id=page_id)
#     if request.method == "POST":
#         form_data = PageForm(request.POST, instance=page)
#         if form_data.is_valid():
#             form_data.save()
#             return redirect("page-detail", page_id = page.id)
#     else:
#         form_data = PageForm(instance=page)
#     return render(request, "diary/page_form.html", { "form": form_data })
# def page_delete(request, page_id):
#     page = Page.objects.get(id=page_id)
#     if request.method == "POST":
#         page.delete()
#         return redirect("page-list")
#     else:
#         return render(request, "diary/page_confirm_delete.html", { "page": page})

