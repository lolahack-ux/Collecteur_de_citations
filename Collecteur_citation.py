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

    for i in range(len(citations)):
        f.write("  <div class='item'>\n")
        f.write(f"    <p>{citations[i]["texte"]}</p>\n")
        f.write(f"    <p>— {citations[i]["auteur"]}</p>\n")
        f.write("  </div>\n\n")
    f.write("</body>\n")
    f.write("</html>\n")


print("5 citationns ajoutées")
