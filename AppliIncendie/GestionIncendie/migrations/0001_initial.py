# Generated by Django 4.2.2 on 2024-02-18 14:08

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ccdrf',
            fields=[
                ('nom_ccdrf', models.CharField(choices=[('ASSILAH', 'ASSILAH'), ('BAB BERRED', 'BAB BERRED'), ('BEN KARRICH', 'BEN KARRICH'), ('BENI AAROUSS', 'BENI AAROUSS'), ('CHECHAOUEN NORD', 'CHECHAOUEN NORD'), ('CHECHAOUEN SUD', 'CHECHAOUEN SUD'), ('FAHS-ANJRA', 'FAHS-ANJRA'), ('JEBHA', 'JEBHA'), ('LARACHE', 'LARACHE'), ('MDIQ-TETOUAN', 'MDIQ-TETOUAN'), ('MOKRISSET', 'MOKRISSET'), ('TATTOFT', 'TATTOFT')], max_length=80, primary_key=True, serialize=False, verbose_name='Nom du CCDRF')),
                ('comment_ccdrf', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('geometry_ccdrf', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='DirectionProvinciale',
            fields=[
                ('nom_dp', models.CharField(choices=[('CHEFCHAOUEN', 'CHEFCHAOUEN'), ('LARACHE', 'LARACHE'), ('TANGER', 'TANGER'), ('TETOUAN', 'TETOUAN')], max_length=80, primary_key=True, serialize=False, verbose_name='Nom de la DPEFLCD')),
                ('comment_dp', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('geometry_dp', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='TracheeParFeu',
            fields=[
                ('id_tpf', models.BigAutoField(primary_key=True, serialize=False)),
                ('etat_tpf', models.CharField(choices=[('BON', 'BON'), ('MOYEN', 'MOYEN'), ('MAUVAIS', 'MAUVAIS')], max_length=80, verbose_name='Etat')),
                ('largeur_tpf', models.IntegerField(blank=True, null=True, verbose_name='Largeur')),
                ('geometrie_tpf', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
                ('dp_tpf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tpf', to='GestionIncendie.directionprovinciale', verbose_name='Nom de la DPEFLCD')),
            ],
        ),
        migrations.CreateModel(
            name='SecteurForestier',
            fields=[
                ('nom_sf', models.CharField(choices=[('AIN JDIDA', 'AIN JDIDA'), ('BEN KARRICH', 'BEN KARRICH'), ('Bni Hassane', 'Bni Hassane'), ('CAP SPARTEL', 'CAP SPARTEL'), ('OUED LAOU', 'OUED LAOU'), ('TORRETA', 'TORRETA'), ('Tamrabta', 'Tamrabta'), ('MELLOUSSA', 'MELLOUSSA'), ('BGHAGHZA', 'BGHAGHZA'), ('DAR CHAOUI', 'DAR CHAOUI'), ('HARCHA', 'HARCHA'), ('Oued Raouze', 'Oued Raouze'), ('GHABA LARACHE', 'GHABA LARACHE'), ('Koudiat Tayfor', 'Koudiat Tayfor'), ('Machrah', 'Machrah'), ('Rouaousa', 'Rouaousa'), ('GHABA KHALIFA', 'GHABA KHALIFA'), ('TATTOFT', 'TATTOFT'), ('El Ghorraf', 'El Ghorraf'), ('BOUHACHEM', 'BOUHACHEM'), ('TAZIA', 'TAZIA'), ('TAGHRAMT', 'TAGHRAMT'), ('RESTINGA', 'RESTINGA'), ('KRIMDA', 'KRIMDA'), ('ASSILAH', 'ASSILAH'), ('NOUADER', 'NOUADER')], max_length=80, primary_key=True, serialize=False, verbose_name='Nom du Secteur forestier')),
                ('comment_sf', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('geometrie_sf', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('ccdrf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secteurs', to='GestionIncendie.ccdrf', verbose_name='Nom du CCDRF')),
            ],
        ),
        migrations.CreateModel(
            name='PosteVigie',
            fields=[
                ('id_pv', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom_pv', models.CharField(blank=True, max_length=50, null=True, verbose_name='Lieu')),
                ('date_creation_pv', models.DateField(blank=True, null=True, verbose_name='Date de création')),
                ('altitude_pv', models.FloatField(blank=True, null=True, verbose_name='Altitude')),
                ('etat_pe', models.CharField(choices=[('FONCTIONNEL', 'FONCTIONNEL'), ('NON FONCTIONNEL', 'NON FONCTIONNEL')], max_length=80, verbose_name='Etat')),
                ('geometrie_pv', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('dp_pv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postes_vigies', to='GestionIncendie.directionprovinciale', verbose_name='Nom de la DPEFLCD')),
            ],
        ),
        migrations.CreateModel(
            name='PointEau',
            fields=[
                ('id_pe', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom_pe', models.CharField(blank=True, max_length=50, null=True, verbose_name='Lieu')),
                ('date_creation_pe', models.DateField(blank=True, null=True, verbose_name='Date de création')),
                ('altitude_pe', models.FloatField(blank=True, null=True, verbose_name='Altitude')),
                ('capacite_eau', models.FloatField(blank=True, null=True, verbose_name='Capacité en eau')),
                ('etat_pe', models.CharField(choices=[('FONCTIONNEL', 'FONCTIONNEL'), ('NON FONCTIONNEL', 'NON FONCTIONNEL')], max_length=80, verbose_name='Etat')),
                ('geometrie_pe', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('dp_pe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points_eaux', to='GestionIncendie.directionprovinciale', verbose_name='Nom de la DPEFLCD')),
            ],
        ),
        migrations.CreateModel(
            name='Incendie',
            fields=[
                ('id_incendie', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_eclosion', models.DateField(blank=True, null=True, verbose_name="Date d'éclosion")),
                ('date_arret', models.DateField(blank=True, null=True, verbose_name="Date d'arrêt")),
                ('cause_incendie', models.CharField(choices=[('INCONNUE', 'INCONNUE'), ('HUMAINE', 'HUMAINE'), ('NATURELLE', 'NATURELLE')], max_length=80, verbose_name='Cause')),
                ('surface_brulee', models.FloatField(blank=True, null=True, verbose_name='Surface brûlée')),
                ('cout_financier', models.FloatField(blank=True, null=True, verbose_name='Coût financier (Dhs)')),
                ('comment_incendie', models.TextField(blank=True, max_length=500, null=True, verbose_name='Commentaire')),
                ('geometrie_incendie', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('dp_icd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incendies', to='GestionIncendie.directionprovinciale', verbose_name='Nom de la DPEFLCD')),
            ],
        ),
        migrations.AddField(
            model_name='ccdrf',
            name='dp_ccdrf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ccdrf', to='GestionIncendie.directionprovinciale', verbose_name='Nom de la DPEFLCD'),
        ),
    ]
