#!/usr/bin/env python3
import os
import json
import random
import pickle
import requests
import pandas as pd
import tensorflow as tf
from inltk.inltk import get_sentence_encoding
from inltk.inltk import setup
import pyttsx3

class Bot:
    def __init__(self):
        print('Setting up hindi support')
        setup('hi')
        self.subscription_key = '1352efe917df4167b7e990696200e04a'
        self.endpoint =  'https://api.cognitive.microsofttranslator.com/'

        path = '/translate?api-version=3.0'
        params = '&from=en&to=hi'
        self.constructed_url = self.endpoint + path + params

        self.headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
            'Content-type': 'application/json',
            'Ocp-Apim-Subscription-Region': 'centralindia',
        }

        self.hdf = pd.read_json('hindi_intent.json')
        self.model = tf.keras.models.load_model('model', compile=False)

        with open('pickles/ohe', 'rb') as handle:
            self.ohe = pickle.load(handle)

        with open('pickles/le', 'rb') as handle:
            self.le = pickle.load(handle)

        self.reader = pyttsx3.init()

    def _translate(self, text):
        body = []
        count = 0
        if isinstance(text, list):
            for sent in text:
                body.append({'text': sent})
                count += len(sent)
                if count>10000:
                    body.pop(-1)
                    break
        else:
            body.append({'text': text})
        
        request = requests.post(self.constructed_url, headers=self.headers, json=body)
        response = request.json()
        
        if isinstance(text, list):
            return [result['translations'][0]['text'] for result in response]
        else:
            return response[0]['translations'][0]['text']

    def say(self, text):
        for voice in self.reader.getProperty('voices'):
            if voice.languages[0]=='hi_IN' and voice.gender=='VoiceGenderFemale':
                self.reader.setProperty('voice', voice.id)
                self.reader.say(text)
                self.reader.runAndWait()
                self.reader.stop()

    def reply(self, message):
        message = self._translate(message)

        encoding = get_sentence_encoding(message,'hi').reshape(1,1,400)

        if tf.reduce_max(self.model(encoding))>0.3:
            result = self.ohe.inverse_transform(self.model(encoding))
            result = self.le.inverse_transform(result)[0]
            choices = self.hdf[self.hdf['intent']==result]['responses'].to_list()[0]

            return random.choice(choices)

        else:
            return self.translate("I don't understand what you mean")

if __name__ == '__main__':
    myBot = Bot()
    myBot.say(myBot.reply('hello'))
