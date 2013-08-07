# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Alv'
        db.create_table(u'besluitenlijst_alv', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datum', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'besluitenlijst', ['Alv'])

        # Adding model 'Besluit'
        db.create_table(u'besluitenlijst_besluit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('besluit', self.gf('django.db.models.fields.TextField')()),
            ('alv', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['besluitenlijst.Alv'])),
            ('volgnummer', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'besluitenlijst', ['Besluit'])


    def backwards(self, orm):
        # Deleting model 'Alv'
        db.delete_table(u'besluitenlijst_alv')

        # Deleting model 'Besluit'
        db.delete_table(u'besluitenlijst_besluit')


    models = {
        u'besluitenlijst.alv': {
            'Meta': {'object_name': 'Alv'},
            'datum': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'besluitenlijst.besluit': {
            'Meta': {'object_name': 'Besluit'},
            'alv': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['besluitenlijst.Alv']"}),
            'besluit': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'volgnummer': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['besluitenlijst']