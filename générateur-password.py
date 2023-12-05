import hashlib
import json

def caractère_speciaux(passwd):
    taille=len(passwd)-1
    for i in range(len(passwd)):
       
        if passwd[i] == '!' or passwd[i]=="%" or passwd[i]== '#' or passwd[i]=='@'  or passwd[i]=='$' or passwd[i]=='%' or passwd[i]=='^' or passwd[i]=='&': 
            print('mot de passe enregistré')
            
            break
        elif passwd[i] != '!' and passwd[i]!="%" and passwd[i]!= '#' and passwd[i]!='@' and  passwd[i]!='$' and passwd[i]!='%' and passwd[i]!='^' and passwd[i]!='&' and i == taille:
            print('il faut au moins un  caractère spécial: (!, @, #, $, %, ^, &, *).')
        
        


passwd=input('saisir un mot de passe: ')

if len(passwd) >=8:
    if passwd.isupper()==False:
        if passwd.islower()==False:
            if passwd.isalpha()==False:
                if passwd.isdigit()==False:
                    caractère_speciaux(passwd)
                    hash_pass=hashlib.sha256(passwd.encode('utf-8'))
                    print (hash_pass)
                    ajout_base_de_donnée=input('voulez-vous ajouter votre mot de passe haché o/n :')
                    if ajout_base_de_donnée == "o":
                        mot_de_passe = open('Base_de_donnee.txt','a')
                        son.dumps([1, 2, 3, {'4': 5, '6': 7}]
                        mot_de_passe.write(hash_pass)
                    elif ajout_base_de_donnée =="n" :
                        print(json.dumps("\"foo\bar")
                else:
                    print('il faut plus de lettre ')
            else:
                print('il faut au moins un caractère numérique')       
        else:
            print('il faut au moins un caractère majuscule')
    else:
        print('il faut au moins un caractère minuscule')  
else:
    print('le mot de passe doit contenir au moins 8 caractères' )

