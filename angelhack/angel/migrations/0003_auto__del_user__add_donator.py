# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'angel_user')

        # Adding model 'Donator'
        db.create_table(u'angel_donator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_login_dt', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_upd_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'angel', ['Donator'])


    def backwards(self, orm):
        # Adding model 'User'
        db.create_table(u'angel_user', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_upd_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_login_dt', self.gf('django.db.models.fields.DateTimeField')()),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=32)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'angel', ['User'])

        # Deleting model 'Donator'
        db.delete_table(u'angel_donator')


    models = {
        u'angel.donator': {
            'Meta': {'object_name': 'Donator'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_upd_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'angel.gender': {
            'Meta': {'object_name': 'Gender'},
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'angel.student': {
            'Meta': {'object_name': 'Student'},
            'amount_needed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'amount_received': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'c_year_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.YearLevel']"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.Gender']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ind_success': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_upd_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'angel.successstory': {
            'Meta': {'object_name': 'SuccessStory'},
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_upd_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.Student']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'angel.yearlevel': {
            'Meta': {'object_name': 'YearLevel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year_in_school': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '2'})
        },
        u'angel.yesno': {
            'Meta': {'object_name': 'YesNo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yes_no': ('django.db.models.fields.CharField', [], {'default': "'Y'", 'max_length': '1'})
        }
    }

    complete_apps = ['angel']