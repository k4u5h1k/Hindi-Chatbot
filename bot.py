import string
import re
import random
from data import patterns, reflections

class chat:
  def __init__(self):
    self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),patterns))
    self.values = list(map(lambda x:x[1],patterns))

  def translate(self,str,dict):
    words = str.lower().split()
    keys = dict.keys();
    for i in range(0,len(words)):
      if words[i] in keys:
        words[i] = dict[words[i]]
    return ' '.join(words)

  def respond(self,str):
    for i in range(0, len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        resp = random.choice(self.values[i])
        pos = resp.find('%')
        while pos > -1:
          num = int(resp[pos+1:pos+2])
          resp = resp[:pos] + \
            self.translate(match.group(num),reflections) + \
            resp[pos+2:]
          pos = resp.find('%')
        if resp[-2:] == '?.': resp = resp[:-2] + '.'
        if resp[-2:] == '??': resp = resp[:-2] + '?'
        return resp


def command_interface():
    '''
        Enter "अलविदा" when done.
    '''
    print('आपका स्वागत है। आज आप कैसे है? ?')

    s = ''
    bot = chat()
    while s != 'अलविदा':
        try:
            s = input('You: ')
        except EOFError:
            s = 'अलविदा'
        print(s)
        while s[-1] in '!.':
            s = s[:-1]
        print("Bot : " + bot.respond(s))

if __name__ == "__main__":
    command_interface()