
from ORS.old_patient_reg.models import Old_Patient	
from django.contrib import admin
import csv
from django.http import HttpResponse


class Old_PatientAdmin(admin.ModelAdmin):
    fieldsets = [
                 
                ('Patient Information', {'fields' : ['pub_date',('patient_first_name','patient_last_name'),'dob',('address1','address2'),('city','state'),'zip_code',('home_phone','back_up_phone'),'sex',('relationship','order_taken_by','store')], 'classes':['collapse']}),
                ('Insurance Information', {'fields' : [('primary_insurance','claim_id'),('insurance_address','insurance_phone'),('secondary_insurance','secondary_insurance_claim_id'),('secondary_insurance_address','secondary_insurance_phone')],'classes':['collapse']}),
                ('Referal & Doctor Information', {'fields' : ['referal_name','resp_party_name','md_name','md_id','md_address','md_phone'],'classes': ['collapse']}),
                ('Patient Measurements', {'fields':[('hips','trunk','shoulder'),('head_width','foot_length'),('weight','height'),('seat_elbow','seat_lateral_top'),('seat_shoulder_top','seat_head_top'),('back_knee','knee_heel','axilla_floor'),('elbow_floor','wrist_floor','buttock_crease_floor')], 'classes' : ['collapse']}),
                ('Comments & Orders', {'fields' :['comments','orders','codes_prices',],'classes':['collapse']}),
                ('Patient Status',{'fields' :[('faxed_reg_status','faxed_reg_date'),('faxed_script','faxed_script_date'),('faxed_justification','faxed_justification_date'),('faxed_MD_notes','faxed_MD_notes_date'),('faxed_price_quotes','faxed_price_quotes_date'),('quickbooks_estimate','quickbooks_estimate_date'),('quickbooks_eval_estimate','quickbooks_eval_estimate_date'),('item_approved','item_approved_date'),('item_ordered','item_ordered_date'),('item_set_up','item_set_up_date'),('billed','billed_date'),('paid','paid_date'),('pending_date','status_notes')],'classes':['collapse']}),
                ]
    list_display = ('pub_date','pending_date','patient_first_name','patient_last_name','faxed_reg_status','faxed_script','faxed_price_quotes','quickbooks_estimate','item_approved','item_ordered','item_set_up','billed','paid')
    #list_editable = ('patient_first_name','faxed_reg_status')
    list_filter = ['pub_date','faxed_reg_status','faxed_script','faxed_justification','faxed_MD_notes','faxed_price_quotes','quickbooks_estimate','quickbooks_eval_estimate','item_approved','item_ordered','item_set_up','billed','paid']
    search_fields =('patient_last_name','patient_first_name','orders','referal_name','store','md_name')
    save_as = True
    date_hierarchy = 'pub_date'
    save_on_top=True
    actions =['exportdata']

    def exportdata(self, request, queryset):
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=orsdata.csv'

        writer = csv.writer(response)
        for row in queryset:
            writer.writerow(queryset)

        return response
    
admin.site.register(Old_Patient, Old_PatientAdmin)
