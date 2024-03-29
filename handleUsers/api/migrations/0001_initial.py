# Generated by Django 4.1 on 2022-11-17 08:30

from django.db import migrations, models
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorId', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='Nome')),
                ('surname', models.CharField(blank=True, default='', max_length=100, verbose_name='Cognome')),
                ('cf', models.CharField(blank=True, default='', max_length=100, verbose_name='Codice fiscale')),
                ('office', models.CharField(choices=[('o0', '--'), ('o1', 'Informatica'), ('o2', 'Ragioneria'), ('o3', 'Tributi'), ('o4', 'Segreteria'), ('o5', 'Urp'), ('o6', 'Protocollo'), ('o7', 'Messo'), ('o8', 'Polizia locale'), ('o9', 'Anagrafe'), ('o10', 'Magazzino'), ('o11', 'LLPP'), ('o12', 'Ambiente'), ('o13', 'Commercio'), ('o14', 'Edilizia'), ('o15', 'Biblioteca'), ('o16', 'Informagiovani'), ('o17', 'CDR'), ('o18', 'Politico')], default='o0', max_length=4, verbose_name='Ufficio principale')),
                ('mail', models.CharField(default='@comune.aviano.pn.it', max_length=120, verbose_name='Mail personale')),
                ('mailOffice', multiselectfield.db.fields.MultiSelectField(choices=[('mo0', '--'), ('mo1', 'magazzino@'), ('mo2', 'patrimonio@'), ('mo3', 'tecnico@'), ('mo4', 'manutenzione@'), ('mo5', 'tributi@'), ('mo6', 'ragioneria@'), ('mo7', 'informatica@'), ('mo8', 'segreteria@'), ('mo9', 'sindaco@'), ('mo10', 'polizia.locale@'), ('mo11', 'serviziscolastici@'), ('mo12', 'urbanistica@'), ('mo13', 'edilizia.privata@'), ('mo14', 'sportellounico.edilizia@'), ('mo15', 'gestione.territorio@'), ('mo16', 'ambiente@'), ('mo17', 'commercio@'), ('mo18', 'urp@'), ('mo19', '@'), ('mo20', 'vicesindaco@')], default='mo0', max_length=100)),
                ('lan', models.CharField(default='A516-', max_length=120, verbose_name='ID personale')),
                ('lanOffice', multiselectfield.db.fields.MultiSelectField(choices=[('l0', '--'), ('l1', 'Affari Generali'), ('l2', 'Ambiente'), ('l3', 'Anagrafe'), ('l4', 'Associazioni'), ('l5', 'Biblioteca'), ('l6', 'Casa di riposo'), ('l7', 'Commercio'), ('l8', 'Contratti'), ('l9', 'Informagiovani'), ('l10', 'Lavori pubblici'), ('l11', 'Manutenzione'), ('l12', 'Patrimonio'), ('l13', 'Personale'), ('l14', 'Polizia municipale'), ('l15', 'Protocollo'), ('l16', 'Ragioneria'), ('l17', 'Segreteria'), ('l18', 'Segreteria sindaco'), ('l19', 'Servizi educativi'), ('l20', 'Sistemi informatici'), ('l21', 'Tributi'), ('l22', 'Urbanistica')], default='mo0', max_length=100)),
                ('lanRole', models.CharField(choices=[('l0', '--'), ('l1', 'Utente'), ('l2', 'Amministratore'), ('l3', 'Solo internet')], default='l1', max_length=2, verbose_name='Ruolo in LAN')),
                ('lanNote', models.CharField(blank=True, default='', max_length=150, verbose_name='Note per lan')),
                ('adwebOffice', multiselectfield.db.fields.MultiSelectField(choices=[('ao0', '--'), ('ao23', '2015 Attività segreteria'), ('ao1', 'Servizi alla persona e alla comunità'), ('ao2', 'Servizi demografici'), ('ao3', 'Servizi educativi e culturali'), ('ao4', 'Servizio affari generali urp protocollo'), ('ao5', 'Servizio appalti e contratti'), ('ao6', 'Servizio turismo sport e associazioni'), ('ao7', 'Servizio casa di soggiorno anziani'), ('ao8', 'Servizi informatici'), ('ao9', 'Servizio contabilità e bilancio'), ('ao10', 'Servizio tributi'), ('ao11', 'Servizio ambiente ed energie rinnovabili'), ('ao12', 'Servizio SUAP e commercio'), ('ao13', 'Servizio urbanistica ed edilizia privata'), ('ao14', 'Servizio gestione rifiuti'), ('ao15', 'Servizio lavori pubblici ed espropri'), ('ao16', 'Servizio manutenzione'), ('ao17', 'Servizio patrimonio'), ('ao18', 'Servizio Polizia locale'), ('ao19', 'Servizio Segreteria particolare e rappresentanza'), ('ao20', 'Segretario generale'), ('ao21', 'Ufficio gestione delle risorse umane - MCM'), ('ao22', 'Nominativo per consigli e giunte')], default='mo0', max_length=100)),
                ('adwebRole', models.CharField(choices=[('a0', '--'), ('a1', 'Istruttore'), ('a2', 'Istruttore ragioneria'), ('a3', 'Istruttore segreteria'), ('a5', 'Politico'), ('a6', 'Potere di firma')], default='a0', max_length=4, verbose_name='Ruolo in adweb')),
                ('adwebNote', models.CharField(blank=True, default='', max_length=150, verbose_name='Note per adweb')),
                ('ascotOffice', multiselectfield.db.fields.MultiSelectField(choices=[('a0', '--'), ('a1', 'Servizi alla persona e alla comunità'), ('a2', 'Servizi demografici'), ('a3', 'Servizi educativi e culturali'), ('a4', 'Servizio affari generali urp protocollo'), ('a5', 'Servizio appalti e contratti'), ('a6', 'Servizio turismo sport e associazioni'), ('a7', 'Servizio casa di soggiorno anziani'), ('a8', 'Servizi informatici'), ('a9', 'Servizio contabilità e bilancio'), ('a10', 'Servizio tributi'), ('a11', 'Servizio ambiente ed energie rinnovabili'), ('a12', 'Servizio SUAP e commercio'), ('a13', 'Servizio urbanistica ed edilizia privata'), ('a14', 'Servizio gestione rifiuti'), ('a15', 'Servizio lavori pubblici ed espropri'), ('a16', 'Servizio manutenzione'), ('a17', 'Servizio patrimonio'), ('a18', 'Servizio Polizia locale'), ('a19', 'Servizio Segreteria particolare e rappresentanza'), ('a20', 'Segretario generale'), ('a21', 'Ufficio gestione delle risorse umane - MCM')], default='a0', max_length=100, verbose_name='Uffici ascot')),
                ('ascotRole', models.CharField(choices=[('a0', '--'), ('a1', 'Utente'), ('a2', 'Amministratore')], default='a0', max_length=4, verbose_name='Ruolo ascot')),
                ('ascotNote', models.CharField(blank=True, default='', max_length=150, verbose_name='Note per ascot')),
                ('sdiOffice', multiselectfield.db.fields.MultiSelectField(choices=[('sdi0', '--'), ('sdi1', 'Casa di soggiorno anziani'), ('sdi2', 'Affari generali, URP, protocollo'), ('sdi3', 'Segreteria generale'), ('sdi4', 'Gestione risorse umane'), ('sdi5', 'Polizia locale'), ('sdi6', 'Servizio contabilità'), ('sdi7', 'Servizio contratti'), ('sdi8', 'Servizio cultura biblioteca'), ('sdi9', 'Servizio manutenzione'), ('sdi10', 'Servizio personale'), ('sdi11', 'Servizio tributi'), ('sdi12', 'Settore urbanistica, ambiente, commercio')], default='sdi0', max_length=100, verbose_name='Uffici SDI')),
                ('sdiRole', models.CharField(choices=[('sdi0', '--'), ('sdi1', 'Utente'), ('sdi2', 'Amministratore')], default='sdi0', max_length=4, verbose_name='Ruolo in SDI')),
                ('sdiNote', models.CharField(blank=True, default='', max_length=150, verbose_name='Note per SDI')),
                ('iteratti', models.CharField(blank=True, default='', max_length=120, verbose_name='ID iteratti')),
                ('iterattiOffice', multiselectfield.db.fields.MultiSelectField(choices=[('i0', '--'), ('i1', 'AAG - Area affari generali'), ('i2', 'PROT - Protocollo'), ('i3', 'DEL - Delibere'), ('i4', 'BIBLIO - Biblioteca'), ('i5', 'PG - Progetto giovani'), ('i6', 'AANA - Area anagrafe'), ('i7', 'AN - Anagrafe'), ('i8', 'ATTIAN - Atti anagrafe'), ('i9', 'ACA\t- Area contratti e assicurazioni'), ('i10', 'URP - Urp'), ('i11', 'UFFASS - Ufficio assicurazioni'), ('i12', 'UFFCONT - Ufficio contratti'), ('i13', 'AAGG - Affari generali'), ('i14', 'AEF - Area economico finanziaria'), ('i15', 'RAG - Ragioneria'), ('i16', 'ECON\t- Economo'), ('i17', 'REVISORI\t- Revisori'), ('i18', 'TRIB\t- Tributi'), ('i19', 'INF - Informatica'), ('i20', 'ALPP - Area lavori pubblici e patrimonio'), ('i21', 'LP - Lavori pubblici'), ('i22', 'PATRIMONIO  - Patrimonio'), ('i23', 'MAN - Manutenzione'), ('i24', 'AUAP - Area urbanistica e attività produttive'), ('i25', 'URB - Urbanistica'), ('i26', 'SUAP - Suap'), ('i27', 'SUE - Sue'), ('i28', 'AMB - Ambiente'), ('i29', 'UFFCOM  - Ufficio commercio'), ('i30', 'AMA - Area messo e albo'), ('i31', 'MESSO - Messo'), ('i32', 'ALBO - Albo'), ('i33', 'ATALBO - Atti albo'), ('i33', 'VIG - Polizia locale'), ('i34', 'CR - Casa di riposo'), ('i35', 'UFFSEG - Ufficio segreteria'), ('i36', 'SEG - Segretario'), ('i37', 'SIND - Sindaco'), ('i38', 'GEN  - Protocollo generale'), ('i39', 'BASS\t- Basso Daniele - assessore'), ('i40', 'CREM\t- Cremon Martina - assessore'), ('i41', 'RAGZ - Ragozzino Giuseppe - assessore'), ('i42', 'MEN  - Menegoz Andrea - assessore'), ('i43', 'MUN  - Mungo Giorgia - assessore')], default='i0', max_length=100, verbose_name='Uffici iteratti')),
                ('iterattiRole', models.CharField(choices=[('i0', '--'), ('i1', 'Utente'), ('i2', 'Amministratore')], default='i0', max_length=2)),
                ('iterattiNote', models.CharField(blank=True, default='', max_length=150, verbose_name='Note per iteratti')),
                ('boxAppsRole', models.CharField(choices=[('b0', '--'), ('b1', 'Utente'), ('b2', 'Amministratore')], default='b1', max_length=4)),
                ('masterDataRole', models.CharField(choices=[('m0', '--'), ('m1', 'Voce inserita'), ('m2', 'Amministratore')], default='m1', max_length=4)),
                ('websiteRole', models.CharField(choices=[('w0', '--'), ('w1', 'Editor'), ('w2', 'Amministratore'), ('w3', 'Utente area privata')], default='w0', max_length=2)),
                ('crmRole', models.CharField(choices=[('c0', '--'), ('c1', 'Utente'), ('c2', 'Amministratore')], default='c0', max_length=2)),
                ('avcpRole', models.CharField(choices=[('a0', '--'), ('a1', 'Utente'), ('a2', 'Amministratore')], default='a0', max_length=2)),
                ('fvgPayRole', models.CharField(choices=[('f0', '--'), ('f1', 'Utente'), ('f2', 'Amministratore')], default='s0', max_length=2)),
                ('mepaRole', models.CharField(choices=[('m0', '--'), ('m1', 'Istruttore'), ('m2', 'Punto ordinante')], default='m0', max_length=4)),
                ('agEntrRole', models.CharField(choices=[('a0', '--'), ('a1', 'Istruttore'), ('a2', 'PO')], default='a0', max_length=4)),
                ('sueRole', models.CharField(choices=[('s0', '--'), ('s1', 'Utente'), ('s2', 'Amministratore')], default='s0', max_length=2)),
                ('suapRole', models.CharField(choices=[('s0', '--'), ('s1', 'Utente'), ('s2', 'Amministratore')], default='s0', max_length=2)),
                ('servScolRole', models.CharField(choices=[('ss0', '--'), ('ss1', 'Utente'), ('ss2', 'Amministratore')], default='ss0', max_length=4)),
                ('alboPretRole', models.CharField(choices=[('ap0', '--'), ('ap1', 'Visualizzatore'), ('ap2', 'Editor'), ('ap3', 'Amministratore')], default='ap0', max_length=4)),
                ('note', models.TextField(blank=True, default='')),
                ('active', models.BooleanField(default=True)),
                ('mailDeleted', models.BooleanField(default=False, verbose_name='Mail disattivata')),
                ('lanDeleted', models.BooleanField(default=False, verbose_name='Lan disattivata')),
                ('adwebDeleted', models.BooleanField(default=False, verbose_name='Adweb disattivato')),
                ('ascotDeleted', models.BooleanField(default=False, verbose_name='Ascot disattivato')),
                ('sdiDeleted', models.BooleanField(default=False, verbose_name='SDI disattivato')),
                ('iterattiDeleted', models.BooleanField(default=False, verbose_name='SDI disattivato')),
                ('boxAppsDeleted', models.BooleanField(default=False, verbose_name='SDI disattivato')),
                ('websiteDeleted', models.BooleanField(default=False, verbose_name='Sito disattivato')),
                ('crmDeleted', models.BooleanField(default=False, verbose_name='CRM disattivato')),
                ('avcpDeleted', models.BooleanField(default=False, verbose_name='AVCP disattivato')),
                ('servScuolDeleted', models.BooleanField(default=False, verbose_name='Servizi scolastici disattivato')),
                ('alboPretDeleted', models.BooleanField(default=False, verbose_name='Albo pretorio disattivato')),
                ('masterdataDeleted', models.BooleanField(default=False, verbose_name='Masterdata eliminato')),
            ],
            options={
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='officeMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(choices=[('mo0', '--'), ('mo1', 'magazzino@'), ('mo2', 'patrimonio@'), ('mo3', 'tecnico@'), ('mo4', 'manutenzione@'), ('mo5', 'tributi@'), ('mo6', 'ragioneria@'), ('mo7', 'informatica@'), ('mo8', 'segreteria@'), ('mo9', 'sindaco@'), ('mo10', 'polizia.locale@'), ('mo11', 'serviziscolastici@'), ('mo12', 'urbanistica@'), ('mo13', 'edilizia.privata@'), ('mo14', 'sportellounico.edilizia@'), ('mo15', 'gestione.territorio@'), ('mo16', 'ambiente@'), ('mo17', 'commercio@'), ('mo18', 'urp@'), ('mo19', '@'), ('mo20', 'vicesindaco@')], default='mo0', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='officeSDI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offices', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userSDI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdiId', models.CharField(blank=True, default='', max_length=100, verbose_name='LOGIN FVG')),
                ('sdiOffices', models.ManyToManyField(to='api.officesdi')),
            ],
        ),
        migrations.CreateModel(
            name='userLan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lanId', models.CharField(blank=True, default='A516-', max_length=100, verbose_name='Nome utente rete locale')),
                ('lanFolders', models.ManyToManyField(to='api.officemail')),
            ],
        ),
    ]
