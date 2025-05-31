#!/usr/bin/env python3
# 3. finally auto_mail_sender.py
import os.path
import subprocess
import sys
import time
import datetime

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser


def create_custom_message(school_name):
    body = f'''
Hej {school_name}, jag är auto_mail_sender.py
'''
    return body


def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT']['EMAIL_SENDER'], config['DEFAULT']['EMAIL_PASSWORD']


def check_duplicates(df):
    dups = df[df.duplicated(subset=["EPOST"], keep=False)]
    if not dups.empty:
        print("\n⚠️ Dubletter hittade (baserat på EPOST):")
        print(dups[["SKOLENHETENS NAMN", "EPOST"]].sort_values(by="EPOST"))
        print('Avbryter programmet.')
        sys.exit(1)
    else:
        print("\n✅ Inga dubletter i e-postadresser.")


def send_emails_in_batches(df, sender_email, sender_password, batch_size=20, pause_seconds=60, dry_run=False):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    if not dry_run:
        server.login(sender_email, sender_password)

    total_emails = len(df)
    for start in range(0, total_emails, batch_size):
        end = min(start + batch_size, total_emails)
        batch = df.iloc[start:end]
        print(f"\n📤 Skickar batch {start // batch_size + 1} (Från rad {start} till rad {end - 1}) totalt ")

        for index, row in batch.iterrows():
            recipient_email = row["EPOST"]
            school_name = row["SKOLENHETENS NAMN"]

            if pd.notna(recipient_email):
                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = recipient_email
                msg["Subject"] = f'Viktig forskningsförfrågan till {school_name}: AI i gymnasieskolan, vänligen vidarebefordra till lärare'

                body = create_custom_message(school_name)
                msg.attach(MIMEText(body, "plain"))

                try:
                    if not dry_run:
                        server.sendmail(sender_email, recipient_email, msg.as_string())
                    print(f"{'🧪 [TEST] ' if dry_run else '✅ '}Skickad till: {school_name} ({recipient_email})")
                except Exception as e:
                    print(f"❌ Misslyckades att skicka till {recipient_email}: {e}")

        if end < total_emails:
            print(f"⏳ Väntar {pause_seconds} sekunder innan nästa batch...")
            next_batch_time = datetime.datetime.now() + datetime.timedelta(seconds=pause_seconds)
            print(f"\n⏳ Nästa batch skickas ut vid: {next_batch_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"⏳ Väntar {pause_seconds} sekunder innan nästa batch...")
            for remaining in range(pause_seconds, 0, -1):
                print(f'{remaining}')
                time.sleep(1)
            print()

    server.quit()
    print("\n🚀 Alla e-postmeddelanden har skickats!")


def main():
    if not os.path.isdir('batches'):
        print('Directory "batches" does not exist. Running batchify.py...')
        print('🔧Directory "batches" does not exist.  Kör email_clean_and_batcher.py &-> batchify.py...')
        subprocess.run(['python', 'email_clean_and_batcher.py'], check=True)
    dry_run = "--dry-run" in sys.argv
    file_args = [arg for arg in sys.argv if arg.endswith(".xlsx")]
    if not file_args:
        print("❌ Ingen Excel-fil angiven. cd AutoMailSender och kör: ./auto_mail_sender.py batches/batch_01.xlsx --dry-run")
        sys.exit(1)

    input_file = file_args[0]

    if not os.path.exists(input_file):
        print(f"❌ Filen {input_file} finns inte.")
        sys.exit(1)
    if not dry_run:
        i_am_sure = input('This is not a dry run. Are you sure you want to send for real? (Y/n): ')
        if i_am_sure.lower() == 'n':
            print('You are not sure, exiting')
            print('Testa köra auto auto_mail_sender.py batches/batch_01.xlsx  --dry-run')
            sys.exit(0)
    df = pd.read_excel(input_file)
    sender_email, sender_password = load_config()

    check_duplicates(df)
    send_emails_in_batches(df, sender_email, sender_password, batch_size=20, pause_seconds=60, dry_run=dry_run)


if __name__ == "__main__":
    main()
