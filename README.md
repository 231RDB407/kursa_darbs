# kursa_darbs

# Uzdevumu plānotājs

## Projekta uzdevuma apraksts

Šis projekts ir izstrādāts, lai automatizētu ikdienas uzdevumu plānošanu un pārvaldību. Mūsdienu straujajā dzīves ritmā cilvēkiem bieži ir grūti sekot līdzi visiem saviem uzdevumiem, termiņiem un prioritātēm. Uzdevumu plānotājs ir vienkārša, bet efektīva programmatūra, kas palīdz lietotājiem organizēt savus uzdevumus, noteikt to prioritātes un sekot līdzi izpildes termiņiem.

Programma ir izstrādāta kā konsoles aplikācija, kas ļauj lietotājam:
- Pievienot jaunus uzdevumus ar aprakstu, prioritāti un izpildes termiņu
- Apskatīt uzdevumu sarakstu, sakārtotu pēc prioritātes vai termiņa
- Atzīmēt uzdevumus kā pabeigtus
- Dzēst uzdevumus no saraksta
- Saglabāt uzdevumu sarakstu failā un ielādēt to no faila

Šī programmatūra ir īpaši noderīga studentiem, darbiniekiem un jebkuram, kam nepieciešams efektīvi pārvaldīt savus ikdienas pienākumus. Tā palīdz lietotājiem koncentrēties uz svarīgākajiem uzdevumiem, neaizmirst par termiņiem un sistemātiski sekot līdzi savu uzdevumu izpildei.

## Izmantotās Python bibliotēkas un to nozīme

Projekta izstrādē tiek izmantotas šādas Python standarta bibliotēkas:

1. **json** - Šī bibliotēka tiek izmantota, lai nodrošinātu uzdevumu saraksta saglabāšanu un ielādi JSON formātā. JSON (JavaScript Object Notation) ir viegli lasāms datu apmaiņas formāts, kas ir ideāli piemērots strukturētu datu, piemēram, uzdevumu saraksta, glabāšanai. Bibliotēka nodrošina funkcijas `json.dump()` un `json.load()`, kas attiecīgi ļauj saglabāt Python objektus JSON failā un ielādēt tos no faila.

2. **os** - Operētājsistēmas bibliotēka tiek izmantota, lai pārbaudītu, vai uzdevumu saglabāšanas fails eksistē pirms mēģinājuma to ielādēt. Funkcija `os.path.exists()` ļauj pārbaudīt, vai norādītais fails eksistē, kas palīdz izvairīties no kļūdām, mēģinot ielādēt neeksistējošu failu.

3. **datetime** - Šī bibliotēka nodrošina funkcionalitāti darbam ar datumiem un laiku. Projektā tā tiek izmantota, lai apstrādātu uzdevumu termiņus, pārveidotu teksta formāta datumus datuma objektos un formatētu datumus attēlošanai lietotājam. Klase `datetime` un tās metodes ļauj veikt dažādas operācijas ar datumiem, piemēram, salīdzināt tos, formatēt un aprēķināt starpību.

4. **re** - Regulāro izteiksmju bibliotēka tiek izmantota, lai apstrādātu un normalizētu lietotāja ievadītos datuma formātus. Funkcija `re.sub()` ļauj aizstāt dažādus datuma atdalītājus (piemēram, atstarpes, domuzīmes, slīpsvītras) ar punktiem, tādējādi nodrošinot vienotu datuma formātu tālākai apstrādei.

Šīs bibliotēkas ir izvēlētas, jo tās ir daļa no Python standarta bibliotēkas, kas nozīmē, ka tās ir pieejamas bez papildu instalācijas, nodrošinot programmas vieglu pārnesamību un uzstādīšanu. Turklāt tās piedāvā visas nepieciešamās funkcijas, lai efektīvi implementētu uzdevumu plānotāja pamatfunkcionalitāti.

## Izmantotās datu struktūras

Projektā tiek izmantotas šādas pašdefinētas datu struktūras:

1. **Task klase** - Šī klase reprezentē vienu uzdevumu un satur šādus atribūtus:
   - `description` (apraksts) - uzdevuma teksta apraksts
   - `priority` (prioritāte) - skaitliska vērtība no 1 līdz 10, kas norāda uzdevuma svarīgumu
   - `deadline` (termiņš) - datuma objekts, kas norāda uzdevuma izpildes termiņu
   - `completed` (pabeigts) - būla vērtība, kas norāda, vai uzdevums ir pabeigts

   Task klase nodrošina arī metodes datu konvertēšanai starp objektu un vārdnīcas formātu, kas nepieciešams JSON serializācijai:
   - `to_dict()` - pārveido uzdevumu vārdnīcas formātā
   - `from_dict()` - izveido uzdevumu no vārdnīcas datu struktūras

2. **TaskPlanner klase** - Šī klase pārvalda uzdevumu kolekciju un nodrošina šādas funkcijas:
   - Uzdevumu pievienošana, atzīmēšana kā pabeigtu un dzēšana
   - Uzdevumu kārtošana pēc prioritātes vai termiņa
   - Uzdevumu saglabāšana failā un ielāde no faila
   - Uzdevumu attēlošana konsolē

   TaskPlanner klase izmanto sarakstu (list) kā galveno datu struktūru uzdevumu glabāšanai, kas ļauj viegli pievienot, dzēst un kārtot uzdevumus.

Papildus tam, projektā tiek izmantotas arī šādas Python standarta datu struktūras:

1. **Saraksti (lists)** - Tiek izmantoti, lai glabātu Task objektu kolekciju un apstrādātu datuma daļas.
2. **Vārdnīcas (dictionaries)** - Tiek izmantotas uzdevumu serializācijai un deserializācijai JSON formātā.
3. **Datuma objekti (datetime.date)** - Tiek izmantoti, lai reprezentētu un apstrādātu uzdevumu termiņus.

Šīs datu struktūras ir izvēlētas, lai nodrošinātu efektīvu datu organizāciju, vieglu piekļuvi un manipulāciju ar uzdevumiem, kā arī vienkāršu datu saglabāšanu un ielādi.

## Programmatūras izmantošanas metodes

Uzdevumu plānotājs ir konsoles aplikācija, kas darbojas interaktīvā režīmā. Lai izmantotu programmatūru, lietotājam jāseko šiem soļiem:

### Programmas palaišana

1. Pārliecinieties, ka jūsu sistēmā ir instalēts Python 3.
2. Lejupielādējiet programmas failu (piemēram, `task_planner.py`).
3. Atveriet termināli vai komandrindu.
4. Navigējiet uz direktoriju, kurā atrodas programmas fails.
5. Palaidiet programmu ar komandu:
   ```
   python task_planner.py
   ```

### Galvenā izvēlne

Pēc programmas palaišanas tiks attēlota galvenā izvēlne ar šādām opcijām:
1. Pievienot uzdevumu
2. Parādīt uzdevumus (pēc prioritātes)
3. Parādīt uzdevumus (pēc termiņa)
4. Atzīmēt uzdevumu kā pabeigtu
5. Dzēst uzdevumu
6. Iziet

Lai izvēlētos darbību, ievadiet atbilstošo ciparu un nospiediet Enter.

### Uzdevuma pievienošana

Lai pievienotu jaunu uzdevumu:
1. Izvēlnē ievadiet "1" un nospiediet Enter.
2. Ievadiet uzdevuma aprakstu, kad tas tiek pieprasīts.
3. Ievadiet uzdevuma prioritāti (skaitli no 1 līdz 10), kur 1 ir zemākā prioritāte un 10 ir augstākā.
4. Ievadiet uzdevuma izpildes termiņu formātā D.M.GGGG (piemēram, 15.12.2023) vai D.M (piemēram, 1.1, kas automātiski pieņems pašreizējo gadu).

Programma pārbauda ievadīto datu pareizību un informē par kļūdām, ja tādas ir. Piemēram, tā pārbauda, vai prioritāte ir skaitlis no 1 līdz 10, vai datums ir derīgs (ņemot vērā mēneša dienu skaitu un garā gada aprēķinu).

### Uzdevumu saraksta aplūkošana

Lai aplūkotu uzdevumu sarakstu:
- Ievadiet "2", lai skatītu uzdevumus, sakārtotus pēc prioritātes (no augstākās līdz zemākajai).
- Ievadiet "3", lai skatītu uzdevumus, sakārtotus pēc termiņa (no tuvākā līdz tālākajam).

Uzdevumu saraksts tiks attēlots ar numuriem, statusu (pabeigts vai ne), aprakstu, prioritāti un termiņu.

### Uzdevuma atzīmēšana kā pabeigtu

Lai atzīmētu uzdevumu kā pabeigtu:
1. Izvēlnē ievadiet "4" un nospiediet Enter.
2. Tiks parādīts uzdevumu saraksts.
3. Ievadiet uzdevuma numuru, kuru vēlaties atzīmēt kā pabeigtu.

### Uzdevuma dzēšana

Lai dzēstu uzdevumu:
1. Izvēlnē ievadiet "5" un nospiediet Enter.
2. Tiks parādīts uzdevumu saraksts.
3. Ievadiet uzdevuma numuru, kuru vēlaties dzēst.

### Programmas aizvēršana

Lai aizvērtu programmu, izvēlnē ievadiet "6" un nospiediet Enter.

### Datu saglabāšana

Programma automātiski saglabā visas izmaiņas uzdevumu sarakstā failā "tasks.json", kas atrodas tajā pašā direktorijā, kur programmas fails. Tas nozīmē, ka lietotājam nav jāuztraucas par manuālu datu saglabāšanu - visi pievienotie, pabeigti vai dzēstie uzdevumi tiek automātiski saglabāti.

Nākamreiz palaižot programmu, visi iepriekš saglabātie uzdevumi tiks automātiski ielādēti.

## Secinājumi

Uzdevumu plānotājs ir vienkārša, bet efektīva programmatūra, kas palīdz lietotājiem organizēt savus ikdienas uzdevumus. Tā nodrošina visas nepieciešamās pamatfunkcijas uzdevumu pārvaldībai, izmantojot intuitīvu konsoles interfeisu.

Programma ir izstrādāta, izmantojot objektorientētās programmēšanas principus, kas padara kodu modulāru un viegli paplašināmu. Izmantotās Python standarta bibliotēkas nodrošina nepieciešamo funkcionalitāti bez ārēju atkarību nepieciešamības.

Nākotnē programmu varētu uzlabot, pievienojot papildu funkcijas, piemēram, atkārtotu uzdevumu plānošanu, atgādinājumus par tuvojošiem termiņiem vai grafisko lietotāja interfeisu.
