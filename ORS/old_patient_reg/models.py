from django.db import models
import datetime


# Data models here to build database.

class Old_Patient(models.Model):
    class Meta:
        verbose_name             = 'Patient Registration & Status'
        ordering                  =['-pub_date']
        verbose_name_plural      = 'Patients' 
    # id                          = models.IntegerField(primary_key=True)
    pub_date                    = models.DateField('date added',blank=True,null=True)
    #pub_date                    = models.CharField(max_length= 50,blank=True,null=True)
    order_taken_by              = models.CharField(max_length= 50,blank=True,)
    store                       = models.CharField(max_length= 200,blank=True)
    patient_first_name          = models.CharField(max_length= 50,verbose_name='First Name')
    patient_last_name           = models.CharField(max_length=50,verbose_name='Last Name')
    address1                    = models.CharField(max_length=300,blank=True)
    address2                    = models.CharField(max_length=300,blank=True,)
    city                        = models.CharField(max_length=100,blank=True,)
    state                       = models.CharField(max_length=40,blank=True,)
    zip_code                    = models.CharField(max_length=50,blank=True,)
    home_phone                  = models.CharField(max_length=50,blank=True,)
    back_up_phone               = models.CharField(max_length=90,blank=True,)
    sex                         = models.CharField(max_length=20,blank=True,)
    relationship                = models.CharField(max_length=100,blank=True,)
    primary_insurance           = models.CharField(max_length=200,blank=True,)
    claim_id                    = models.CharField(max_length=200,blank=True,)
    insurance_address           = models.CharField(max_length=300,blank=True,)
    insurance_phone             = models.CharField(max_length=200,blank=True,)
    secondary_insurance         = models.CharField(max_length=200,blank=True,)
    secondary_insurance_claim_id= models.CharField(max_length=200,blank=True,)
    secondary_insurance_address = models.CharField(max_length=200,blank=True,)
    secondary_insurance_phone   = models.CharField(max_length=200,blank=True,)
    referal_name                = models.CharField(max_length=200,blank=True,)
    resp_party_name             = models.CharField(max_length=200,blank=True,)
    md_name                     = models.CharField(max_length=200,blank=True,)
    md_id                       = models.CharField(max_length=200,blank=True,)
    md_address                  = models.CharField(max_length=300,blank=True,)
    md_phone                    = models.CharField(max_length=200,blank=True,)
    hips                        = models.CharField(max_length=200,blank=True,)
    trunk                       = models.CharField(max_length=200,blank=True,)
    shoulder                    = models.CharField(max_length=200,blank=True,)
    head_width                  = models.CharField(max_length=200,blank=True,)
    foot_length                 = models.CharField(max_length=200,blank=True,)
    weight                      = models.CharField(max_length=200,blank=True,)
    height                      = models.CharField(max_length=200,blank=True,)
    seat_elbow                  = models.CharField(max_length=200,blank=True,)
    seat_lateral_top            = models.CharField(max_length=200,blank=True,)
    seat_shoulder_top           = models.CharField(max_length=200,blank=True,)
    seat_head_top               = models.CharField(max_length=200,blank=True,)
    back_knee                   = models.CharField(max_length=200,blank=True,)
    knee_heel                   = models.CharField(max_length=200,blank=True,)
    axilla_floor                = models.CharField(max_length=200,blank=True,)
    elbow_floor                 = models.CharField(max_length=200,blank=True,)
    wrist_floor                 = models.CharField(max_length=200,blank=True,)
    buttock_crease_floor        = models.CharField(max_length=200,blank=True,)
    comments                    = models.TextField(blank=True,)
    orders                      = models.TextField(blank=True,)
    #dob                        = models.CharField(max_length=20,blank=True,null=True)
    dob                         = models.DateField('DOB',blank=True, null=True)
    codes_prices                = models.TextField(blank=True,)
    faxed_reg_date              = models.DateField('date', null=True,blank=True,)
    faxed_reg_status            = models.NullBooleanField(default=False,blank=True,verbose_name='Faxed Reg')
    faxed_script                = models.NullBooleanField(default=False,blank=True,verbose_name='Faxed RX')
    faxed_script_date           = models.DateField('date',null=True,blank=True)
    faxed_justification         = models.NullBooleanField(blank=True,verbose_name='Faxed Just')
    faxed_justification_date    = models.DateField('date',blank=True,null=True)
    faxed_MD_notes              = models.NullBooleanField(blank=True, verbose_name='Faxed MD')
    faxed_price_quotes          = models.NullBooleanField(blank=True,verbose_name='Faxed Quotes')
    faxed_MD_notes_date         = models.DateField('date',blank=True,null=True)
    faxed_price_quotes_date     = models.DateField('date',blank=True,null=True)
    quickbooks_estimate         = models.NullBooleanField(default=False,blank=True,verbose_name='QB Est')
    quickbooks_estimate_date    =  models.DateField('date',blank=True,null=True)
    quickbooks_eval_estimate    = models.NullBooleanField(blank=True,verbose_name='QB Eval')
    quickbooks_eval_estimate_date = models.DateField('date',blank=True,null=True)
    item_ordered                = models.NullBooleanField(default=False,blank=True,verbose_name='Ordered')
    item_ordered_date           = models.DateField('Date:',blank=True,null=True)
    item_set_up                 = models.NullBooleanField(default=False,blank=True,verbose_name='Set Up/Fit')
    item_set_up_date            = models.DateField('Date:',blank=True,null=True)
    billed                      = models.NullBooleanField(default=False,blank=True)
    billed_date                 = models.DateField('Date:',blank=True,null=True)
    paid                        = models.NullBooleanField(default=False,blank=True)
    paid_date                   = models.DateField('Date:',blank=True,null=True)
    item_approved               = models.NullBooleanField(default=False,blank=True,verbose_name='Approved')
    item_approved_date          = models.DateField('Date:',blank=True,null=True)
    status_notes                = models.TextField(blank=True,null=True)
    pending_date                = models.DateField('Follow-Up Next',blank=True,null=True)



    def __unicode__(self):
        return u' %s %s %s' % (self.pub_date, self.patient_first_name, self.patient_last_name)
        #return self.patient_last_name

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Added today?'

