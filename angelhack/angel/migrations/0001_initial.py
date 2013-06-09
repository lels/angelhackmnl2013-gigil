# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gender'
        db.create_table(u'angel_gender', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
        ))
        db.send_create_signal(u'angel', ['Gender'])

        # Adding model 'YesNo'
        db.create_table(u'angel_yesno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yes_no', self.gf('django.db.models.fields.CharField')(default='Y', max_length=1)),
        ))
        db.send_create_signal(u'angel', ['YesNo'])

        # Adding model 'NeedItem'
        db.create_table(u'angel_needitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('need', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
        ))
        db.send_create_signal(u'angel', ['NeedItem'])

        # Adding model 'YearLevel'
        db.create_table(u'angel_yearlevel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year_in_school', self.gf('django.db.models.fields.CharField')(default=0, max_length=2)),
        ))
        db.send_create_signal(u'angel', ['YearLevel'])

        # Adding model 'Story'
        db.create_table(u'angel_story', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pitch', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('need_statement', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('create_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_upd_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'angel', ['Story'])

        # Adding model 'Student'
        db.create_table(u'angel_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['angel.Gender'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=255, null=True)),
            ('amount_needed', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=9, decimal_places=2)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['angel.Story'])),
            ('c_year_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['angel.YearLevel'])),
            ('need_items', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['angel.NeedItem'])),
            ('last_upd_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'angel', ['Student'])

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

        # Adding model 'Donation'
        db.create_table(u'angel_donation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['angel.Student'])),
            ('donator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['angel.Donator'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal(u'angel', ['Donation'])


    def backwards(self, orm):
        # Deleting model 'Gender'
        db.delete_table(u'angel_gender')

        # Deleting model 'YesNo'
        db.delete_table(u'angel_yesno')

        # Deleting model 'NeedItem'
        db.delete_table(u'angel_needitem')

        # Deleting model 'YearLevel'
        db.delete_table(u'angel_yearlevel')

        # Deleting model 'Story'
        db.delete_table(u'angel_story')

        # Deleting model 'Student'
        db.delete_table(u'angel_student')

        # Deleting model 'Donator'
        db.delete_table(u'angel_donator')

        # Deleting model 'Donation'
        db.delete_table(u'angel_donation')


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
        u'angel.needitem': {
            'Meta': {'object_name': 'NeedItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'need': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'})
        },
        u'angel.story': {
            'Meta': {'object_name': 'Story'},
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_upd_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'need_statement': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'pitch': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
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
            'need_items': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['angel.NeedItem']"}),
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