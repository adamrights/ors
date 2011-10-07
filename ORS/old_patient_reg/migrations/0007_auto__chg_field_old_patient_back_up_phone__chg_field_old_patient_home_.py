# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Old_Patient.back_up_phone'
        db.alter_column('old_patient_reg_old_patient', 'back_up_phone', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Old_Patient.home_phone'
        db.alter_column('old_patient_reg_old_patient', 'home_phone', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Old_Patient.zip_code'
        db.alter_column('old_patient_reg_old_patient', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=50))


    def backwards(self, orm):
        
        # Changing field 'Old_Patient.back_up_phone'
        db.alter_column('old_patient_reg_old_patient', 'back_up_phone', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Old_Patient.home_phone'
        db.alter_column('old_patient_reg_old_patient', 'home_phone', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Old_Patient.zip_code'
        db.alter_column('old_patient_reg_old_patient', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=30))


    models = {
        'old_patient_reg.old_patient': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Old_Patient'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'axilla_floor': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'back_knee': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'back_up_phone': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'billed': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'billed_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'buttock_crease_floor': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'claim_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'codes_prices': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'elbow_floor': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'faxed_MD_notes': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'faxed_MD_notes_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'faxed_justification': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'faxed_justification_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'faxed_price_quotes': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'faxed_price_quotes_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'faxed_reg_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'faxed_reg_status': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'faxed_script': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'faxed_script_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'foot_length': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'head_width': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'hips': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'insurance_phone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'item_approved': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'item_approved_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'item_ordered': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'item_ordered_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'item_set_up': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'item_set_up_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'knee_heel': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'md_address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'md_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'md_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'md_phone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order_taken_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'orders': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'paid': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'paid_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'patient_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'patient_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'primary_insurance': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'quickbooks_estimate': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'quickbooks_estimate_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'quickbooks_eval_estimate': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'quickbooks_eval_estimate_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'referal_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'resp_party_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'seat_elbow': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'seat_head_top': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'seat_lateral_top': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'seat_shoulder_top': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'secondary_insurance': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'secondary_insurance_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'secondary_insurance_claim_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'secondary_insurance_phone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'shoulder': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'status_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'store': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'trunk': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'wrist_floor': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['old_patient_reg']
