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
question = int(input('What you want to use? \n1. md5\n \n2. Sha256 \n \n3.Sha 225\n \n4.Sha512\n'))
if question == 1:
    text = input('Type your password: ').encode('utf-8')
    hash = hashlib.md5(text)
    hasdxt = hash.hexdigest()
    print(hasdxt)
elif question == 2:
    text = input('Type your password: ').encode('utf-8')
    hash = hashlib.sha256(text)
    hasdxt = hash.hexdigest()
    print(hasdxt)
elif question == 3:
    text = input('Type your password: ').encode('utf-8')
    hash = hashlib.sha225(text)
    hasdxt = hash.hexdigest()
    print(hasdxt)
elif question == 4:
    text = input('Type your password: ').encode('utf-8')
    hash = hashlib.sha512(text)
    hasdxt = hash.hexdigest()
    print(hasdxt)
else:
    print('Error')
    