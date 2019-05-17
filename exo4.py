import requests

class Exercice_4:
    """Ecrire une classe qui renvoie des informations sur un lieu"""
    def __init__(self, location):
        # Appel API Wikipedia
        self.lieu = location
        url = "https://fr.wikipedia.org/w/api.php"
        par = {"search":self.lieu,"format":"json","action":"opensearch",}
        self.req = requests.get(url,params = par).json()

    def loc(self):
        """
        Ecrire une fonction qui renvoie le nom et la description du lieu
        """

        return f"voici ce que je connais de {self.lieu}:{self.req[2][:]}"

    def get_image(self):  #A definir
        url =  "https://fr.wikipedia.org/w/api.php"
         par2 = {"search":,"format":"json","action":""}
        self.req2 = requests.get(url, params=par).json()
        return f"voici une image d'un quartier de {self.lieu} :{self.req2[0][0]}"


if __name__ == "__main__":

    location = "lyon"
    #Definition de l'objet
    Ville = Exercice_4(location)
    #informations sur lyon
    print(Ville.loc())
    #retourne l'image
    print(Ville.get_image())