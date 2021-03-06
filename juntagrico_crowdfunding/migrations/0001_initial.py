# Generated by Django 2.0.2 on 2018-11-18 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor', models.CharField(blank=True, max_length=100, verbose_name='Pate(n)')),
                ('contribution', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Beitrag')),
                ('date_ordered', models.DateField(auto_now_add=True, verbose_name='Bestellt am')),
                ('date_paid', models.DateField(blank=True, null=True, verbose_name='Bezahlt am')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Mitteilung')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Kommentar')),
            ],
            options={
                'verbose_name': 'Unterstützung',
                'verbose_name_plural': 'Unterstützungen',
            },
        ),
        migrations.CreateModel(
            name='Fundable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('quantity', models.PositiveIntegerField(verbose_name='Gesamtzahl')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preis/Einheit')),
            ],
            options={
                'verbose_name': 'Unterstützungsart',
                'verbose_name_plural': 'Unterstützungsarten',
            },
        ),
        migrations.CreateModel(
            name='Funder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Vorname')),
                ('last_name', models.CharField(max_length=30, verbose_name='Nachname')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('addr_street', models.CharField(max_length=100, verbose_name='Strasse')),
                ('addr_zipcode', models.CharField(max_length=10, verbose_name='PLZ')),
                ('addr_location', models.CharField(max_length=50, verbose_name='Ort')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefonnr')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='funder', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UnterstützerIn',
                'verbose_name_plural': 'UnterstützerInnen',
            },
        ),
        migrations.CreateModel(
            name='FundingProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titel')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Beschreibung')),
                ('image', models.URLField(blank=True, null=True, verbose_name='Bild-URL')),
                ('active', models.BooleanField(verbose_name='Aktiv')),
                ('vocabulary_fundable', models.CharField(default='Patenschaft', max_length=200, verbose_name='Bezeichnung: Unterstützungsart')),
                ('vocabulary_fundables', models.CharField(default='Patenschaften', max_length=200, verbose_name='Bezeichnung: Unterstützungsarten')),
                ('vocabulary_whoIsSponsor', models.TextField(default='Auf wen soll die Patenschaft lauten (Vorname(n))?', verbose_name='Formular: Patenschaftsnennung')),
                ('vocabulary_confirmOrder', models.TextField(default='Bei Bestätigung kaufe ich eine Patenschaft und mache damit eine Schenkung an die Genossenschaft MehalsGmües. Ich kriege eine Patenschaftsbestätigung (Karte - als Geschenk geeignet) per Post. Der Name, auf welchen die Patenschaft lautet, wird auf einer Tafel in der Gärtnerei verewigt.', verbose_name='Formular: Kauf bestätigen')),
                ('vocabulary_confirmOrderButton', models.CharField(default='Verbindlich bestätigen', max_length=200, verbose_name='Formular: Button Verbindlich bestätigen')),
                ('vocabulary_thankYouTitle', models.CharField(default='Vielen Dank', max_length=200, verbose_name='Titel: Dankeschön')),
                ('vocabulary_thankYouMessage', models.TextField(default='ladida', verbose_name='Text: Dankeschön')),
            ],
            options={
                'verbose_name': 'Unterstützungs-Projekt',
                'verbose_name_plural': 'Unterstützungs-Projekte',
            },
        ),
        migrations.AddField(
            model_name='fundable',
            name='funding_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juntagrico_crowdfunding.FundingProject'),
        ),
        migrations.AddField(
            model_name='fund',
            name='fundable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juntagrico_crowdfunding.Fundable'),
        ),
        migrations.AddField(
            model_name='fund',
            name='funder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juntagrico_crowdfunding.Funder'),
        ),
    ]
