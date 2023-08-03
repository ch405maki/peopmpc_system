
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberForm
from .models import Member
from django.views.generic import UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator

class MemberDetailView(DetailView):
    model = Member
    template_name = 'members/member_detail_individual.html'
    context_object_name = 'member'

@login_required
def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member_detail')
    else:
        form = MemberForm()

    return render(request, 'members/create_member.html', {'form': form})

# Not Authenticated
from django.urls import reverse

def register_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save()
            return redirect('account_number', account_number=member.account_number, name=member.name, mname=member.mname, lname=member.lname)
    else:
        form = MemberForm()
    return render(request, 'members/register_member.html', {'form': form})


# Not Authenticated
def account_number(request, account_number, name, mname, lname):
    # Retrieve other details based on the account number and the additional parameters
    # Then pass them to the template as context variables

    return render(request, 'members/account_number.html', {
        'account_number': account_number,
        'name': name,
        'mname': mname,
        'lname': lname,
    })

def member_detail(request):
    # Get the search query from the URL parameter 'q'
    search_query = request.GET.get('q', '')
    print("Search Query:", search_query) 
    # Initialize a queryset with all members
    members = Member.objects.all()
    
    if search_query:
        # If there's a search query, filter the members based on multiple fields using Q objects
        members = members.filter(
            Q(account_number__icontains=search_query) |
            Q(name__icontains=search_query) |
            Q(mname__icontains=search_query) |
            Q(lname__icontains=search_query) |
            Q(sname__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(contact_number__icontains=search_query)
        )
    
        # Paginate the queryset
    paginator = Paginator(members, per_page=5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'members/member_detail.html', {'members': page_obj,  'search_text': search_query})

class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'members/update_member.html'
    success_url = reverse_lazy('member_detail')

class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'members/delete_member.html'
    success_url = reverse_lazy('member_detail')
