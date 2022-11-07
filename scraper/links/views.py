from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Link, CustomUser
from .froms import AddLinkForm
from django.views.generic import TemplateView, DeleteView
from django.contrib import messages

@login_required
def price_tracker(request):
    form = AddLinkForm()
    discounted_items = 0


    if request.method == 'POST':
        form = AddLinkForm(request.POST)
        try:
            if form.is_valid():
                # check if the user already submitted this link
                link_submitted = form.cleaned_data.get('url')
            if Link.objects.filter(user=request.user, url=link_submitted).exists():
                messages.error(request, 'Link already exists! Try with another link.')
            else:
                form.instance.user = request.user
                form.save()
                messages.success(request, 'Link Added Successfully!')
        except:
            messages.error(request, 'Something went wrong! please try with another link.')

    form = AddLinkForm()
    links = Link.objects.filter(user=request.user)
    num_items = links.count()

    if num_items < 0:
        discounted = []
        for item in links:
            discounted.append(item)
            discounted_items = len(discounted)

    context = {
        'form':form,
        'link':links,
        'num_items':num_items,
        'discounted_items':discounted_items
    }

    return render(request, 'links/main.html', context)
    
@login_required
def update_prices(request):
    # refresh prices data
    links = Link.objects.filter(user=request.user)
    for link in links:
        try:
            link.save()
        except:
            messages.error(request, 'Something went wrong! please try again!')
            
    messages.info(request, 'Prices were updated!')
    return redirect('links:tracker')


class DeleteItem(LoginRequiredMixin, DeleteView):
    queryset = Link.objects.all()
    template_name = 'links/delete.html'
    context_object_name = 'item'

    def get_success_url(self):
        messages.success(self.request, 'Item deleted successfully!')
        return reverse('links:tracker')

