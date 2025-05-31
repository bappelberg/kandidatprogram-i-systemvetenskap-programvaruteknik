# AutoMailSender & Survey Data Processor
Ett komplett Python-system för automatiserad e-postutskick till svenska gymnasieskolor och avancerad bearbetning av enkätdata för forskningsstudier om AI och språkmodeller i utbildning.

## Systemöversikt
### Detta repository innehåller två huvudsystem:

📧 AutoMailSender - Massutskick av forskningsenkäter
Automatiserat e-postsystem för att nå ut till svenska gymnasieskolor med forskningsförfrågningar.

📊 Survey Data Processor - ML-baserad databehandling
Avancerat system för bearbetning av enkätdata med maskininlärning för imputering av saknade värden.

🚀 AutoMailSender System
Komponenter
email_clean_and_batcher.py - Rensar data och tar bort dubletter
batchify.py - Delar upp i batch-filer (100 skolor per batch)
auto_mail_sender.py - Skickar e-post från batch-filerna (HUVUDFIL)
Snabbstart
Steg 1: Förberedelse
```bash
cd AutoMailSender
pip install pandas openpyxl matplotlib scikit-learn

eller 

pip install -r requirements.txt vid projektroten
```
```
Steg 2: Konfigurera e-post
Skapa config.ini:

```ini
[DEFAULT]
EMAIL_SENDER = din.email@gmail.com
EMAIL_PASSWORD = ditt_app_password
```
Steg 3: Testa med dry-run
```bash

./auto_mail_sender.py batches/batch_01.xlsx --dry-run
```
Steg 4: Kör på riktigt
```bash
./auto_mail_sender.py batches/batch_01.xlsx
```

Filtstruktur
```bash
projekt/
├── autosender-survey-system/
│   ├── auto_mail_sender.py              # Huvudfil för e-postutskick
│   ├── email_clean_and_batcher.py       # Datarensning
│   ├── batchify.py                      # Batch-skapare
│   ├── config.ini                       # E-postkonfiguration
│   ├── skolenhetsadresser_*.xlsx        # Originaldata (gymnasieskolor)
│   ├── gymnasieskolor_unika_email.xlsx  # Rensad data
│   └── batches/
│       ├── batch_01.xlsx                # 100 skolor per batch
│       ├── batch_02.xlsx
│       └── ...
├── DataPreprocessor/
│   ├── survey_processor.py              # Huvudklassen för databehandling
│   ├── enkätdata.xlsx                   # Rådata från Google Forms
│   ├── survey-teacher-data-*.xlsx       # Bearbetad data
│   └── *.png                           # Konfusionsmatriser
└── README.md
```
# 🔧 Konfiguration
Gmail-inställningar
Aktivera 2-faktor autentisering
Generera App Password:
Google-konto → Säkerhet → App-lösenord
Välj "E-post" som app-typ
Använd genererat lösenord i config.ini

# 📈 Forskningskontext
## Syfte
Undersöka svenska gymnasielärares attityder och användning av stora språkmodeller (LLM) i undervisning.

# Målgrupp
Gymnasielärare i Sverige
Alla ämnesområden
Fokus på AI-adoption i utbildning
Teoretisk grund
UTAUT-modellen (Unified Theory of Acceptance and Use of Technology)
Technology Acceptance Model för utbildningskontext
ML-baserad dataanalys för robust forskningsdata
Etiska överväganden
Anonymitet: Ingen personidentifierbar information sparas
Frivillighet: Tydlig information om forskningens syfte
GDPR-compliance: Säker datahantering
🤝 Bidrag och utveckling
# Utvecklingsmiljö
bash 
```
git clone https://github.com/bappelberg/c-uppsats.git
pip install -r requirements.txt
````


# Kodstruktur
* Modulär design: Separata system för e-post och dataanalys
* Felhantering: Robust error handling i alla komponenter
* Loggning: Detaljerad spårning av alla processer
* Testbarhet: Dry-run lägen för säker utveckling
# Framtida förbättringar
* GUI för icke-tekniska användare
* Automatisk rapportgenerering
* Fler ML-algoritmer för imputering
* Integrering med LimeSurvey/Qualtrics
* Real-time dashboard för enkätrespons

# 📄 Licens
Detta projekt är utvecklat för forskningsändamål vid Uppsala universitet Inst. för informatik och media. Kontakta författarna för användning utanför forskningskontext.

# Kontakt
* Huvudutvecklare: Benjamin Appelberg
* Forskningsprojekt: AI i gymnasieskolan
* Institution: Uppsala universitet Inst. för informatik och media
* E-post: benjamin.w.appelberg@gmail.com
# 📚 Referenser
* Venkatesh, V., et al. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425-478.
* Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319-340.

Notera att de slutgiltiga data som användes för SmartPLS analysen är: 2025-05-14_invert_vol1and2_from_tvang_till_frivillighet_survey-teacher-data-cleaned-imputed.xlsx
Se resultat: SmartPLSProgram/2025-05-18_09-22.html

Senast uppdaterad: 31 maj 2025

