import wikipedia
import os
print('hi! how can i help you?')
while True:
    prompt = str(input('you:'))
    if prompt == '/help':
        print('/recall - to recall last chat.')
        print('/crazy - turns on crazy mode(do not do it!)')
        print('/big brain mode - gives more detailed answers but takes a bit more time to load.')
        print('type disable in front of any of these features to disable them.ex-/recall disable')
        print('/search-search about a topic related page')
        continue
    elif prompt == '/crazy':
        while True:
            while True:
                while True:
                    print('i warned you!')
    elif prompt == '/big brain mode':
        with open('data/bigbrain.NGPTdat','w') as f:
            f.write('delete this file to disable big brain mode!')
        print('big brain mode eneabled!')
        continue
    elif prompt.startswith('/search'):
        search = wikipedia.search(prompt[7:])
        print('--searching--')
        for i in search:
            print(i)
        continue
    elif prompt == '/big brain mode disable':
        if os.path.exists('data/bigbrain.NGPTdat'):
            os.remove('data/bigbrain.NGPTdat')
            print('big brain mode disabled!')
            continue
        else:
            print('big brain mode is already disabled!')
            continue
    elif prompt == '/recall disable':
        if os.path.exists('data/recall.NGPTdat'):
            with open('data/recall.NGPTdat','w',encoding='utf-8') as f:
                f.write(' ')
            print('last chat removed')
            continue
        else:
            print('first search anything to use the recall feature(cuz you deleted it did you?)')
            continue
    print('--wait for answer--')
    if wikipedia.exceptions.DisambiguationError or wikipedia.exceptions.PageError:
        with open('crashlog.txt','w') as f:
            f.write("this ai is not capable of giving answers to complex questions.\n")
            f.write('if your prompt does not have a wiki page,it will give a error.\n')
            f.write('it can give answers to wiki pages like las vegas,among us,or anything like that')
    if prompt == '/recall':
        with open('data/recall.NGPTdat','r') as f:
            answer = f.read()
        print(answer)
        continue
    if os.path.exists('data/bigbrain.NGPTdat'):
        answer = wikipedia.page(prompt)
        print('----NGPT----')
        with open('data/recall.NGPTdat','w',encoding='utf-8') as f:
            f.write(answer.content)
        print(answer.content)
    else:
        answer = wikipedia.summary(prompt)
        with open('data/recall.NGPTdat','w',encoding='utf-8') as f:
            f.write(answer)
        print('----NGPT----')
        print(answer)