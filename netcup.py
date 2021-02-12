from netcup_crawler import NetcupCrawler
from send_mail import SendMail

crawler = NetcupCrawler()
mail = SendMail()

entries = crawler.fetch()

if crawler.check(entries):
    crawler.save(entries)

    subject = "Netcup - Neues Sonderangebot"
    body = ""
    for entry in entries:
        body += "<br>Angebot: " + entry.title + "<br> Preis: " + entry.price + "<br>"

    recepients = {"info@bausecreative.de", "olebause@hotmail.de"}

    mail.send_mail(subject, body, recepients)
    print("Email gesendet.")
else:
    print("Keine Email gesendet.")


