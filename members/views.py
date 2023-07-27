
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
        form = MemberForm()
    return render(request, 'members/create_member.html', {'form': form})


def member_detail(request):
    members = Member.objects.all()
    return render(request, 'members/member_detail.html', {'members': members})

class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'members/update_member.html'
    success_url = reverse_lazy('member_detail')

class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'members/delete_member.html'
    success_url = reverse_lazy('member_detail')
