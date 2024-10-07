from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from WORKERS.models import Worker



def worker_signup(request):
    if request.method == 'POST':
        worker_name = request.POST.get('worker_name')
        email_id = request.POST.get('email_id')
        phone_number = request.POST.get('phone_number', '')
        address = request.POST.get('address', '')
        skills = request.POST.get('skills')
        experience = request.POST.get('experience', 0)
        password = request.POST.get('password')


        # Validate the fields before proceeding
        if not (worker_name and email_id and password and skills):
            messages.error(request, 'Please fill in all the required fields.')
            return redirect('worker_reg')

        # Check if email_id is already in use
        if Worker.objects.filter(email_id=email_id).exists():

            messages.error(request, 'A worker with that email already exists.')
            return redirect('worker_reg')

        try:
            # Create the worker account
            worker = Worker.objects.create_user(
                username=email_id,
                email_id=email_id,
                password=password
            )
            worker.worker_name = worker_name
            worker.phone_number = phone_number
            worker.address = address
            worker.skills = skills
            worker.experience = int(experience)  # Convert to integer
            worker.is_approved = False  # Set is_approved to False by default (admin approval needed)
            worker.save()

            # Success message
            # If registration is successful
            messages.success(request, 'Registration successful! Please wait for admin approval.')
            return redirect('worker_login')  # Should redirect here after POST


        except Exception as e:
            # Handle the error and provide feedback to the user
            messages.error(request, f'Error occurred: {str(e)}')
            return redirect('worker_reg')

    return render(request, 'workersignup.html')




# Worker Login View
def worker_login(request):
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')

        # Authenticate the worker
        worker = authenticate(request, username=email_id, password=password)
        if worker is not None:
            if hasattr(worker, 'is_approved') and worker.is_approved:  # Ensure 'is_approved' is checked safely
                login(request, worker)
                messages.success(request, 'Login successful!')
                return redirect('worker_home')  # Redirect to worker dashboard or homepage
            else:
                messages.error(request, 'Your account is not approved yet.')
                return redirect('worker_login')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('worker_login')

    return render(request, 'workerlogin.html')






# Worker Home View
def worker_home(request):
    return render(request, 'workerhome.html')
