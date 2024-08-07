from django.db import models

from django.urls import reverse

# Create your models here.

# Username: bananasitapp_admin
# Password: whitebanana

# Table for AboutUs
class AboutU(models.Model):
    # Index Page Content
    about_text_first = models.CharField(max_length=100)
    about_text_second = models.CharField(max_length=100)
    about_text_third = models.CharField(max_length=150)

    # Read More Content
    about_our_mission = models.CharField(max_length=500)
    about_what_we_do = models.CharField(max_length=500)
    about_our_team = models.CharField(max_length=500)
    about_why_choose_us = models.CharField(max_length=500)
    about_contact_us = models.CharField(max_length=500)

    def __str__(self):
        return 'About Us'
    
# Table for Services
class Service(models.Model):
    service_title = models.CharField(max_length=100)
    service_description = models.CharField(max_length=500)

    def __str__(self):
        return self.service_title
    
# Table for Portfolios
class Portfolio(models.Model):
    portfolio_title = models.CharField(max_length=100)
    portfolio_description = models.CharField(max_length=500)
    prortfolio_link = models.CharField(max_length=500)
    portfolio_image = models.FileField(upload_to='portfolio_images/')

    def __str__(self):
        return self.portfolio_title
    
# Table for Contact Text
class ContactText(models.Model):
    contact_text_first = models.CharField(max_length=100)
    contact_text_second = models.CharField(max_length=100)

    def __str__(self):
        return 'Contact Text'

# Table for Testimonials
class Testimonial(models.Model):
    testimonial_name = models.CharField(max_length=100)
    testimonial_designation = models.CharField(max_length=500)
    testimonial_description = models.CharField(max_length=500)
    testimonial_image = models.FileField(upload_to='testimonial_images/')

    def __str__(self):
        return self.testimonial_name
        
# Table for Clients
class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_website_link = models.CharField(max_length=500, default='')
    client_image = models.FileField(upload_to='client_images/')

    def __str__(self):
        return self.client_name
    
# Table for Team Members
class TeamMember(models.Model):
    # Details of Team Member
    member_name = models.CharField(max_length=100)
    member_designation = models.CharField(max_length=500)
    member_qualification = models.CharField(max_length=500)
    member_image = models.FileField(upload_to='team_member_images/')

    # Social Links of Team Member
    member_instagram = models.CharField(max_length=500)
    member_facebook = models.CharField(max_length=500)
    member_twitter = models.CharField(max_length=500)
    member_linkedin = models.CharField(max_length=500)

    def __str__(self):
        return self.member_name
    
# Table for Contact Details
class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_mobile = models.CharField(max_length=20)
    contact_email = models.EmailField(max_length=250)
    contact_message = models.CharField(max_length=500)

    def __str__(self):
        return self.contact_name
    
# Table for FAQ
class Faq(models.Model):
    faq_question = models.CharField(max_length=500)
    faq_answer = models.CharField(max_length=500)

    def __str__(self):
        return 'faq_' + str(self.id)
    
# Table for Subscription ID
class SubscriptionId(models.Model):
    subscription_id = models.CharField(max_length=500)

    def __str__(self):
        return self.subscription_id
    
# Table for Resume Submission
class Resume(models.Model):
    seeker_name = models.CharField(max_length=100)
    seeker_contact = models.CharField(max_length=20)
    seeker_email = models.CharField(max_length=500)
    seeker_job_post = models.CharField(max_length=500)
    seeker_experience = models.IntegerField(default=0)
    seeker_other_details = models.CharField(max_length=500)
    seeker_resume = models.FileField(upload_to='resume_documents/')
    seeker_submission_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.seeker_name
    
    def get_view_url(self):
        return reverse('admin:view_document', args=[self.id])
    
    def get_download_url(self):
        return reverse('admin:download_document', args=[self.id])
    
# Table for Job Posts
class JobPost(models.Model):
    job_post = models.CharField(max_length=100)

    def __str__(self):
        return self.job_post
    
# Table for Slider
class Slider(models.Model):
    slider_title = models.CharField(max_length=100)
    slider_description = models.CharField(max_length=500)
    slider_image = models.FileField(upload_to='slider_images/')

    def __str__(self):
        return self.slider_title