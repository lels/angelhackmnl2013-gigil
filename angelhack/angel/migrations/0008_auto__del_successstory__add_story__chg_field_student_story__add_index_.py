# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SuccessStory'
        db.delete_table(u'angel_successstory')

        # Adding model 'Story'
        db.create_table(u'angel_story', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('create_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_upd_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'angel', ['Story'])


        # Renaming column for 'Student.story' to match new field type.
        db.rename_column(u'angel_student', 'story', 'story_id')
        # Changing field 'Student.story'
        db.alter_column(u'angel_student', 'story_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['angel.Story']))
        # Adding index on 'Student', fields ['story']
        db.create_index(u'angel_student', ['story_id'])


    def backwards(self, orm):
        # Removing index on 'Student', fields ['story']
        db.delete_index(u'angel_student', ['story_id'])

        # Adding model 'SuccessStory'
        db.create_table(u'angel_successstory', (
            ('create_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('last_upd_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['angel.Student'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'angel', ['SuccessStory'])

        # Deleting model 'Story'
        db.delete_table(u'angel_story')


        # Renaming column for 'Student.story' to match new field type.
        db.rename_column(u'angel_student', 'story_id', 'story')
        # Changing field 'Student.story'
        db.alter_column(u'angel_student', 'story', self.gf('django.db.models.fields.CharField')(max_length=4000, null=True))

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
        u'angel.story': {
            'Meta': {'object_name': 'Story'},
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_upd_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'angel.student': {
            'Meta': {'object_name': 'Student'},
            'amount_needed': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '9', 'decimal_places': '2'}),
            'c_year_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.YearLevel']"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.Gender']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_upd_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.Story']"})
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