# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Besluit.valid'
        db.add_column(u'besluitenlijst_besluit', 'valid',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Besluit.valid'
        db.delete_column(u'besluitenlijst_besluit', 'valid')


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
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'volgnummer': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['besluitenlijst']