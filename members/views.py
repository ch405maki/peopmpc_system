
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberForm
from .models import Member
from django.views.generic import UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

class MemberDetailView(DetailView):
    model = Member
    template_name = 'members/member_detail_individual.html'
    context_object_name = 'member'

def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member_detail')
        else:
            print(form.errors)
    else:
        form = MemberForm()
    if request.user.is_authenticated:
        # User is logged in, redirect to the create_member.html template
        return render(request, 'members/create_member.html', {'form': form})
    else:
        # User is not logged in, show the register_member.html template
        return render(request, 'members/register_member.html', {'form': form})


def member_detail(request):
    # Get the search query from the URL parameter 'q'
    search_query = request.GET.get('q', '')
    # Initialize a queryset with all members
    members = Member.objects.all()
    
    if search_query:
        # If there's a search query, filter the members based on the name field
        members = members.filter(name__icontains=search_query)

    return render(request, 'members/member_detail.html', {'members': members, 'search_text': search_query})

class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'members/update_member.html'
    success_url = reverse_lazy('member_detail')

class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'members/delete_member.html'
    success_url = reverse_lazy('member_detail')
