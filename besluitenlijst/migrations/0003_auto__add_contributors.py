# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contributors'
        db.create_table(u'besluitenlijst_contributors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contributor', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'besluitenlijst', ['Contributors'])


    def backwards(self, orm):
        # Deleting model 'Contributors'
        db.delete_table(u'besluitenlijst_contributors')


    models = {
        u'besluitenlijst.alv': {
            'Meta': {'object_name': 'Alv'},
            'datum': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'besluitenlijst.besluit': {
            'Meta': {'ordering': "['volgnummer']", 'object_name': 'Besluit'},
            'alv': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['besluitenlijst.Alv']"}),
            'besluit': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'volgnummer': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'besluitenlijst.contributors': {
            'Meta': {'object_name': 'Contributors'},
            'contributor': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['besluitenlijst']