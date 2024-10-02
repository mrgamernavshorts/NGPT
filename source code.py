import wikipedia
import os
import github

loop = True

username = 'username'
token = 'tokwn'

g = github.Github(token)
repo = g.get_repo('username/reponame')

if os.path.exists('data/username.txt'):
    with open('data/username.txt','r') as f:
        user = f.read()
    print(f'hello {user}! how can i help you?')
else:
    init = input('/login or /signup to continue:')
    if init == '/login':
        usern = input('username :')
        passw = input('password :')
        try:
            upassword = repo.get_contents(usern+'/userpass.txt')
            upassword = upassword.decoded_content.decode('utf-8')
            if upassword and upassword == passw:
                with open('data/username.txt','w') as f:
                    f.write(usern)
            else:
                input('username or password is wrong!')
        except github.UnknownObjectException:
            input('username was not found!')

    elif init == '/signup':
        usern = input('username :')
        passw = input('password :')
        try:
            upassword = repo.get_contents(usern+'/userpass.txt')
            print('username taken!')
            input('restart application to retry!')
        except github.UnknownObjectException:
            repo.create_file(usern+'/userpass.txt','user login',passw)
            with open('data/username.txt','w') as f:
                    f.write(usern)


while os.path.exists('data/username.txt'):
    if loop:
        upassword = input('please renter the password to continue :')
        if upassword.startswith('{[!accterminated]}'):
            print('ahha very clever huh?')
            repo.update_file(usern+'/userpass.txt','terminated account','{[!accterminated]} trying to become too much clever!')
            break
        else:
            pass
        with open('data/username.txt','r') as f:
            usern = f.read()
        try:
            passw = repo.get_contents(usern+'/userpass.txt')
            passw = passw.decoded_content.decode('utf-8')
            if not passw.startswith('{[!accterminated]}'):
                if upassword == passw:
                    pass
                else:
                    print('password is incorrect!')
                    input('restart the application to continue!')
                    break
            else:
                teres = passw
                print(f'your account is terminated for {teres[19:]}')
                input('')
                break
        except github.UnknownObjectException:
            input('username change detected in data/username.txt.delete the file and re-login.')
            break
        loop = False
    prompt = str(input('you:'))
    if prompt.startswith('/'):
        if prompt == '/help':
            print('/login-for logging in.')
            print('/signup-for sign up.')
            print('/recall - to recall last chat.')
            print('/crazy - turns on crazy mode(do not do it!)')
            print('/big brain mode - gives more detailed answers but takes a bit more time to load.')
            print('type disable in front of any of these features to disable them.ex-/recall disable')
            print('/search-search about a topic related page')
            continue
        elif prompt == '/recall':
            try:
                recall = repo.get_contents(usern+'/recall.txt')
                recall = recall.decoded_content.decode('utf-8')
                print("--recalled answer---")
                print(recall)
                continue
            except github.UnknownObjectException:
                print('first search for something to be recalled!')
                continue
        elif prompt.startswith('/search'):
            search = wikipedia.search(prompt[8:])
            for i in search:
                print(i)
            continue
        elif prompt == '/big brain mode':
            try:
                sha = repo.get_contents(usern+'/big brain.txt')
                print('big brain mode is already eneabled!')
                continue
            except github.UnknownObjectException:
                repo.create_file(usern+'/big brain.txt','recall update',' ')
                print('big brain mode enealed!')
                continue
        elif prompt == '/crazy':
            print('warned you!')
            print('deleting your account....')
            contents = repo.get_contents(usern)
            for content in contents:
                if content.type == "file":
                    repo.delete_file(content.path, "Delete file", content.sha)
            os.remove('data/username.txt')
            input('account deleted')
            break
        elif prompt ==  '/login' or '/signup':
            print('you can only do this on the start of the application!')
            input('delete the `username.txt` file in the `data` folder to re-login!')
            break
    try:
        repo.get_contents(usern+'/big brain.txt')
        answer = wikipedia.page(prompt)
        answer = answer.content
        print(answer)
        try:
            sha = repo.get_contents(usern+'/recall.txt')
            repo.update_file(usern+'/recall.txt','recall update',answer,sha.sha)
        except github.UnknownObjectException:
            repo.create_file(usern+'/recall.txt','recall update',answer)
    except github.UnknownObjectException:
        answer = wikipedia.summary(prompt)
        print(answer)
        try:
            sha = repo.get_contents(usern+'/recall.txt')
            repo.update_file(usern+'/recall.txt','recall update',answer,sha.sha)
        except github.UnknownObjectException:
            repo.create_file(usern+'/recall.txt','recall update',answer)