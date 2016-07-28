# -*- coding: utf-8 -*-
#sexo 0 indefinido, 1 hombre y 2 mujer
#Sentimiento 0 pesimo 1 malo 2 regular 3 bueno 4 excelente
import requests
class User:
    def __init__(self):
        self.name = ""
        self.comments = []
        
    def getSentiment(self):
        return 0
    
    def getGender(self):
        name = self.name
        payload = {'name': name}
        response = requests.get('https://api.genderize.io', params=payload)
        d = response.json()
        genero = ""
        genero = d['gender']
        return  genero
        



