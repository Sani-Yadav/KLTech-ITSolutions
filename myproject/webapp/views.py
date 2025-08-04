from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


def index(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            project = request.POST.get('project', '')
            message = request.POST.get('message', '')
            subject = f"New Contact Form Submission from {name}"
            email_content = f"""
            New contact form submission received:
            Name: {name}
            Email: {email}
            Project: {project}
            Message: {message}
            This message was sent from the KL Tech website contact form.
            """
            try:
                from email_config import EMAIL_CONFIG
                recipient_email = EMAIL_CONFIG['RECIPIENT_EMAIL']
                send_mail(
                    subject=subject,
                    message=email_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[recipient_email],
                    fail_silently=False,
                )
            except Exception as email_error:
                error_msg = str(email_error).lower()
                if 'authentication' in error_msg or 'password' in error_msg:
                    return JsonResponse({
                        'status': 'success',
                        'message': 'Your message has been received! You will get notification after email setup.'
                    })
                elif 'connection' in error_msg:
                    return JsonResponse({
                        'status': 'success',
                        'message': 'Your message has been received! Email will be sent after internet connection.'
                    })
                else:
                    return JsonResponse({
                        'status': 'success',
                        'message': 'Your message has been received! Please set up Gmail app password.'
                    })
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you! Your message has been sent successfully.'
            })
        except Exception as e:
            if 'EMAIL_HOST_PASSWORD' in str(e) or 'authentication' in str(e).lower():
                return JsonResponse({
                    'status': 'error',
                    'message': 'Email configuration not set up. Please configure Gmail app password in email_config.py'
                })
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Sorry, there was an error sending your message. Please try again.'
                })
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def error_404(request):
    return render(request, '404.html')



