# -*- coding: utf-8 -*-
# sexo 0 indefinido, 1 hombre y 2 mujer
# Sentimiento 0 pesimo 1 malo 2 regular 3 bueno 4 excelente
import requests


class User:

    def __init__(self, name=""):
        self.name = name
        self.comments = []
        self.gender = "undefined"
        self.formated_name = ""

    def getFormatedName(self):
        formated_name = self.name.strip()
        list_formated_name = formated_name.split()
        self.formated_name = list_formated_name[0]
        return self.formated_name

    def getSentiment(self):
        positive = 0
        negative = 0
        neutral = 0

        for comment in self.comments:
            if comment['sentiment'] == 'pos':
                positive += 1
            elif comment['sentiment'] == 'neg':
                negative += 1
            else:
                neutral += 1

        if positive == negative or (neutral > positive and neutral > negative):
            return 'neutral'

        if positive > negative:
            return 'positive'
        if negative > positive:
            return 'negative'

    def getGender(self):
        name = self.name
        payload = {'name': name}
        response = requests.get('https://api.genderize.io', params=payload)
        gender_dictionary = response.json()

        if not gender_dictionary["gender"]:
            self.gender = 'undefined'
        else:
            self.gender = gender_dictionary["gender"]

        return self.gender
