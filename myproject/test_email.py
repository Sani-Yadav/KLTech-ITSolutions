#!/usr/bin/env python
"""
Email Configuration Test Script
Run this to test if your email setup is working
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

def test_email_config():
    print("=" * 50)
    print("EMAIL CONFIGURATION TEST")
    print("=" * 50)
    
    try:
        # Test email settings
        print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
        print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
        print(f"EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
        print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
        print(f"DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")
        
        # Try to send test email
        print("\n Sending test email...")
        
        send_mail(
            subject='Test Email from KL Tech Website',
            message='This is a test email to verify email configuration.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['saniyadav7755@gmail.com'],
            fail_silently=False,
        )
        
        print("SUCCESS: Test email sent successfully!")
        print(" Check saniyadav7755@gmail.com for the test email")
        
    except Exception as e:
        print(f" ERROR: {str(e)}")
        
        if 'authentication' in str(e).lower():
            print("\n SOLUTION:")
            print("1. Go to https://myaccount.google.com/")
            print("2. Enable 2-Step Verification")
            print("3. Generate App Password for 'Mail'")
            print("4. Update email_config.py with the app password")
        elif 'connection' in str(e).lower():
            print("\n SOLUTION:")
            print("Check your internet connection")
        else:
            print(f"\n UNKNOWN ERROR: {str(e)}")
    
    print("=" * 50)

if __name__ == "__main__":
    test_email_config() 