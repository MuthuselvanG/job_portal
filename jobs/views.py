from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Job, Application
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, Application

def home(request):
    jobs = Job.objects.all().order_by('-created_at')
    title = request.GET.get('title')
    location = request.GET.get('location')

    if title:
        jobs = jobs.filter(title__icontains=title)

    if location:
        jobs = jobs.filter(location__icontains=location)

    context = {
        'jobs': jobs
    }
    return render(request, 'home.html', context)

@login_required
def post_job(request):
    if request.method == 'POST':
        Job.objects.create(
            employer=request.user,
            title=request.POST['title'],
            company=request.POST['company'],
            location=request.POST['location'],
            description=request.POST['description']
        )
        return redirect('dashboard')
    return render(request, 'job_post.html')

@login_required
def dashboard(request):
   
    jobs = Job.objects.filter(employer=request.user).order_by('-created_at')
    return render(request, 'employer_dashboard.html', {'jobs': jobs})

def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        app = Application.objects.create(
            job=job,
            name=request.POST['name'],
            email=request.POST['email'],
            resume=request.FILES['resume']
        )

        send_mail(
            'Job Application Submitted',
            f'You have applied for {job.title}',
            'admin@jobportal.com',
            [app.email],
        )
        return redirect('home')
    return render(request, 'job_detail.html', {'job': job})

@login_required
def applications(request, job_id):
    apps = Application.objects.filter(job_id=job_id)
    return render(request, 'applications.html', {'apps': apps})

@login_required
def update_status(request, app_id, status):
    app = Application.objects.get(id=app_id)
    app.status = status
    app.save()

    if status == 'Rejected':
        send_mail(
            'Application Rejected',
            'Sorry, your application was rejected.',
            'admin@jobportal.com',
            [app.email],
        )
    if status == 'Selected':
        send_mail(
            'Application Selected',
            'Happy To Share, your application was Selected Next Level.',
            'admin@jobportal.com',
            [app.email],
        )
    return redirect('dashboard')
@login_required
def dashboard(request):
    jobs = Job.objects.filter(employer=request.user).order_by('-created_at')
    return render(request, 'employer_dashboard.html', {'jobs': jobs})

@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user)

    if request.method == 'POST':
        job.title = request.POST['title']
        job.company = request.POST['company']
        job.location = request.POST['location']
        job.description = request.POST['description']
        job.save()
        return redirect('dashboard')

    return render(request, 'edit_job.html', {'job': job})

@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user)
    job.delete()
    return redirect('dashboard')