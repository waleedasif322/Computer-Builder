# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BuildsTable'
        db.create_table(u'builds_buildstable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('moboListing', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal(u'builds', ['BuildsTable'])


    def backwards(self, orm):
        # Deleting model 'BuildsTable'
        db.delete_table(u'builds_buildstable')


    models = {
        u'builds.buildstable': {
            'Meta': {'object_name': 'BuildsTable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moboListing': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['builds']