import requests
url="http://api.quotable.io/random"


#LOOP
i = 0
citations = [] 

for i in range (0, 5):
    connexion = requests.get(url)
    donnees = connexion.json()
    citation = {
    "texte" : donnees['content'],
    "auteur" : donnees['author']
    } 
    citations.append(citation)

with open("citations.html", "w", encoding="utf-8") as f:

    f.write("<!DOCTYPE html>\n")
    f.write("<html lang='fr'>\n")

    f.write("<head>\n")
    f.write("<meta charset='UTF-8'>\n")
    f.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    f.write("<title>Citations</title>\n")
    f.write("<link rel='stylesheet' href='style.css'>")
    f.write("</head>\n")


    f.write("<body>\n")
    f.write("  <div class='header-quote'>“</div>\n")
    f.write("  <div class='header-line'></div>\n")
    f.write("  <main class='container'>\n")

    for i in range(len(citations)):
        f.write("  <div class='card'>\n")
        f.write("    <div class='quote-icon'>“</div>\n")
        f.write(f"    <p class='quote'>{citations[i]['texte']}</p>\n")
        f.write("    <div class='line'></div>\n")
        f.write(f"    <p class='author'>{citations[i]['auteur']}</p>\n")
        f.write("  </div>\n\n")

    f.write("  </main>\n")
    f.write("</body>\n")

print("5 citations ajoutées")
