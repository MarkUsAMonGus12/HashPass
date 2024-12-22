import os 
import hashlib
print('''
      
 __    __                      __        _______                              
/  |  /  |                    /  |      /       \                             
$$ |  $$ |  ______    _______ $$ |____  $$$$$$$  | ______    _______  _______ 
$$ |__$$ | /      \  /       |$$      \ $$ |__$$ |/      \  /       |/       |
$$    $$ | $$$$$$  |/$$$$$$$/ $$$$$$$  |$$    $$/ $$$$$$  |/$$$$$$$//$$$$$$$/ 
$$$$$$$$ | /    $$ |$$      \ $$ |  $$ |$$$$$$$/  /    $$ |$$      \$$      \ 
$$ |  $$ |/$$$$$$$ | $$$$$$  |$$ |  $$ |$$ |     /$$$$$$$ | $$$$$$  |$$$$$$  |
$$ |  $$ |$$    $$ |/     $$/ $$ |  $$ |$$ |     $$    $$ |/     $$//     $$/ 
$$/   $$/  $$$$$$$/ $$$$$$$/  $$/   $$/ $$/       $$$$$$$/ $$$$$$$/ $$$$$$$/  
                                                                              
                    
      ''')
print('Hi, this app will allow you to encode your password!')
if not os.path.exists('hashed_password'):
    os.makedirs('hashed_password')

question = int(input('What you want to use? \n1. md5\n \n2. Sha256 \n \n3.Sha 224\n \n4.Sha512\n'))
if question == 1:
    text = input('Type your password: ').encode('utf-8')
    hash = hashlib.md5(text)
    hasdxt = hash.hexdigest()
    print(hasdxt)
    os.chdir('hashed_password')
    with open('md5.txt', 'a') as md5:
        md5.write(f'{text.decode('utf-8')} = {hasdxt} \n')
    
elif question == 2:
    text = input('Type your password: ').encode('utf-8')
    hash = hashlib.sha256(text)
    hasdxt = hash.hexdigest()
    print(hasdxt)
    os.chdir('hashed_password')
    with open('sha256.txt', 'a') as sha256:
        sha256.write(f'{text.decode('utf-8')} = {hasdxt} \n')
elif question == 3:
    text = input('Type your password: ').encode('utf-8')
    hash = hashlib.sha224(text)
    hasdxt = hash.hexdigest()
    print(hasdxt)
    os.chdir('hashed_password')
    with open('sha225.txt', 'a') as sha224:
        sha224.write(f'{text.decode("utf-8")} = {hasdxt} \n')
elif question == 4:
    text = input('Type your password: ').encode('utf-8')
    hash = hashlib.sha512(text)
    hasdxt = hash.hexdigest()
    print(hasdxt)
    os.chdir('hashed_password')
    with open('sha512.txt', 'a') as sha512:
        sha512.write(f'{text.decode('utf-8')} = {hasdxt} \n')
else:
    print('Error')
    
