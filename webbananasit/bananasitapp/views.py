from django.shortcuts import render, redirect

from .models import AboutU, Contact, Slider, Testimonial, TeamMember, Client, Service, Portfolio, Resume, JobPost, Faq, SubscriptionId, ContactText
from django.views import View

# Create your views here.

def index(request):
    about_details = AboutU.objects.all()
    service_details = Service.objects.all()
    porfolio_details = Portfolio.objects.all()
    client_details = Client.objects.all()
    contact_text_details = ContactText.objects.all()
    testimonial_details = Testimonial.objects.all()
    team_details = TeamMember.objects.all()
    faq_details = Faq.objects.all()

    context = {'about_details': about_details, 
               'service_details': service_details, 
               'portfolio_details': porfolio_details, 
               'client_details': client_details, 
               'contact_text_details': contact_text_details, 
               'testimonial_details': testimonial_details, 
               'team_details': team_details, 
               'faq_details': faq_details}
    
    if request.method == "POST":
        # Getting Subcription Id and saving it in database
        if 'subscription_email' in request.POST:
            subscription_id = request.POST.get('subscription_email')
            emails = SubscriptionId(subscription_id = subscription_id)
            emails.save()

        # Getting ContactForm Details and saving them in database
        else:
            contact_name = request.POST.get('name')
            contact_email = request.POST.get('email')
            contact_mobile = request.POST.get('contact')
            contact_message = request.POST.get('yourmessage')

            contact = Contact(contact_name = contact_name, 
                            contact_email = contact_email, 
                            contact_mobile = contact_mobile, 
                            contact_message = contact_message)
            
            contact.save()

    return render(request, 'index.html', context)

def about(request):
    about_details = AboutU.objects.all()
    return render(request, 'about.html', {'about_details': about_details})

class JobApplication(View):
    def get(self, request):
        job_post_details = JobPost.objects.all()
        return render(request, 'career.html', {'job_post_details': job_post_details})

    def post(self, request):
        seeker_name = request.POST.get('name')
        seeker_contact = request.POST.get('contact')
        seeker_email = request.POST.get('email')
        seeker_job_post = request.POST.get('jobpost')
        seeker_experience = request.POST.get('experience')
        seeker_other_details = request.POST.get('otherdetails')

        # Handling file upload
        if 'seeker_resume' in request.FILES:
            seeker_resume = request.FILES['seeker_resume']
        else:
            seeker_resume = None

        print(seeker_name, seeker_contact, seeker_email, seeker_job_post, seeker_experience, seeker_other_details)

        resume = Resume(seeker_name = seeker_name, 
                        seeker_contact = seeker_contact, 
                        seeker_email = seeker_email, 
                        seeker_job_post = seeker_job_post, 
                        seeker_experience = seeker_experience, 
                        seeker_other_details = seeker_other_details, 
                        seeker_resume = seeker_resume)
        
        resume.save()
        return redirect('IndexPage')
    
def course(request):
    return render(request, 'courses.html')

