# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'YearLevel'
        db.create_table(u'angel_yearlevel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year_in_school', self.gf('django.db.models.fields.CharField')(default=0, max_length=2)),
        ))
        db.send_create_signal(u'angel', ['YearLevel'])

        # Adding model 'Student'
        db.create_table(u'angel_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_of_birth', self.gf('django.db.models.fields.DateTimeField')()),
            ('amount_needed', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('amount_received', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ind_success', self.gf('django.db.models.fields.CharField')(default='N', max_length=1)),
            ('c_year_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['angel.YearLevel'])),
            ('last_upd_dt', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'angel', ['Student'])

        # Adding model 'SuccessStory'
        db.create_table(u'angel_successstory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('create_dt', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'angel', ['SuccessStory'])


    def backwards(self, orm):
        # Deleting model 'YearLevel'
        db.delete_table(u'angel_yearlevel')

        # Deleting model 'Student'
        db.delete_table(u'angel_student')

        # Deleting model 'SuccessStory'
        db.delete_table(u'angel_successstory')


    models = {
        u'angel.student': {
            'Meta': {'object_name': 'Student'},
            'amount_needed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'amount_received': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'c_year_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.YearLevel']"}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ind_success': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_upd_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'angel.successstory': {
            'Meta': {'object_name': 'SuccessStory'},
            'create_dt': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'angel.yearlevel': {
            'Meta': {'object_name': 'YearLevel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year_in_school': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '2'})
        }
    }

    complete_apps = ['angel']