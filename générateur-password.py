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
while True:
    if len(passwd) >=8:
        if passwd.isupper()==False:
            if passwd.islower()==False:
                if passwd.isalpha()==False:
                    if passwd.isdigit()==False:
                        caractère_speciaux(passwd)
                        hash_pass=hashlib.sha256(passwd.encode('utf-8')).hexdigest()
                        ajout_data=input('voulez-vous ajouter votre mot de passe haché o/n :')
                        if ajout_data == "o":
                            utilite=input('Pour quel utilité aura votre mot de passe en un mot ')
                            donnee_a_ajouter = {"user1" :{'utilite': utilite, 'password':hash_pass}}
                            with open("data_mot-de-passe.json","w") as f:                
                                json.dump(donnee_a_ajouter, f) 
                                break                     
                        elif ajout_data=='n':
                            print('ok')
                            break
                    
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

