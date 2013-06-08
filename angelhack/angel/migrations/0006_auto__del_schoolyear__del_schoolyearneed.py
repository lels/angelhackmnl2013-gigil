# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SchoolYear'
        db.delete_table(u'angel_schoolyear')

        # Deleting model 'SchoolYearNeed'
        db.delete_table(u'angel_schoolyearneed')


    def backwards(self, orm):
        # Adding model 'SchoolYear'
        db.create_table(u'angel_schoolyear', (
            ('year_from', self.gf('django.db.models.fields.IntegerField')()),
            ('year_to', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'angel', ['SchoolYear'])

        # Adding model 'SchoolYearNeed'
        db.create_table(u'angel_schoolyearneed', (
            ('school_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['angel.SchoolYear'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=9, decimal_places=2)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['angel.Student'])),
        ))
        db.send_create_signal(u'angel', ['SchoolYearNeed'])


    models = {
        u'angel.donation': {
            'Meta': {'object_name': 'Donation'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '9', 'decimal_places': '2'}),
            'donator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.Donator']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.Student']"})
        },
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
            'amount_needed': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '9', 'decimal_places': '2'}),
            'c_year_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.YearLevel']"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.Gender']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_upd_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'story': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True'})
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