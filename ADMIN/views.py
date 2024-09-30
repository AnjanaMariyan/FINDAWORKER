
from django.shortcuts import render, redirect
from WORKERS.models import Worker
from django.contrib import messages

# Create your views here.
def hai(request):
    return render(request,'home.html')


# Admin Dashboard to view unapproved workers
def admin_dashboard(request):
    unapproved_workers = Worker.objects.filter(is_approved=False)
    return render(request, 'admin_dashboard.html', {'workers': unapproved_workers})

# Approve Worker
def approve_worker(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    worker.is_approved = True
    worker.save()
    messages.success(request, f'Worker {worker.worker_name} has been approved.')
    return redirect('admin_dashboard')

# Reject Worker (Optional, you may choose to delete or reject)
def reject_worker(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    worker.delete()  # Optionally you could mark it as rejected instead of deleting
    messages.success(request, f'Worker {worker.worker_name} has been rejected.')
    return redirect('admin_dashboard')
