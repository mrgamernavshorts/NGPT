import wikipedia
import os
print('hi! how can i help you?')
while True:
    prompt = str(input('you:'))
    if prompt.startswith('/'):
        pass
    else:
        with open('data/recall.txt','w') as f:
            f.write(prompt)
    if prompt == '/help':
        print('/recall - to recall last chat.delete the file `recall.txt` in `data` folder to reset it.')
        print('/crazy - turns on crazy mode(do not do it!)')
        print('/big brain mode - gives more detailed answers but takes A LOT O TIME TO LOAD.')
        print('    (delete `data/bigbrain.txt` to disable).')
        continue
    elif prompt == '/recall':
        with open('data/recall.txt','r') as f:
            prompt = f.read()
    elif prompt == '/crazy':
        while True:
            while True:
                while True:
                    print('i warned you!')
    elif prompt == '/big brain mode':
        with open('data/bigbrain.txt','w') as f:
            f.write('delete this file to disable big brain mode!')
        input('big brain mode eneabled!')
        break
    print('--wait for answer--')
    if wikipedia.exceptions.DisambiguationError or wikipedia.exceptions.PageError or wikipedia.exceptions.DisambiguationError and wikipedia.exceptions.PageError:
        with open('crashlog.txt','w') as f:
            f.write("this ai is not capable of giving answers to complex questions.\n")
            f.write('if your prompt does not have a wiki page,it will give a error.\n')
            f.write('it can give answers to wiki pages like las vegas,among us,or anything like that')
    if os.path.exists('data/bigbrain.txt'):
        answer = wikipedia.page(prompt)
        print('----NGPT----')
        print(answer.content)
    else:
        answer = wikipedia.summary(prompt)
        print('----NGPT----')
        print(answer)