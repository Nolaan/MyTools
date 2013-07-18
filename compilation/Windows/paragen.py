#!/usr/bin/python

import os, subprocess, multiprocessing, sys
from multiprocessing import Process, Value
# Gestion de l'update du fichier de version
from upd_version import appversion_update

# Fonction de mise a jour du fichier Appversion
# def appversion_update():
#   appversion = open( MY_APPVERSION, 'w+' )
#   lignes = appversion.readline()
#   while
# 

# liste : liste contenant le nom des librairies a compiler 
# running nombre de threads en cours d'execution

liste = ['UCINEO_NANCY_CE','lib_airlan','lib_com_pcc','lib_dataemb','lib_dataex','lib_emb_reprise','lib_maintenances','lib_manager','lib_newloc','lib_phonie','lib_rapporteur','lib_sae','lib_service','lib_smart','lib_transfic','lib_udpservice',"lib_ihm"]
running = Value('i',0)

# Module lancant la compilation d une librairie
# On creer un processus, on attend qu'il 

def nmake(lib,running,config):
    cfg = 'CFG='+lib+' - Win32 (WCE x86) '+config
    print "Config courante : "+cfg
    p = subprocess.Popen(['nmake', '/F',  lib+'.vcn', cfg ])
    p.wait()
    running.value = running.value - 1

# Corps de la tache, elle s'execute tant qu'il y a des donnees dans la pile

if __name__ == '__main__':
    # ihm = subprocess.Popen(['nmake', '/F'])
    # ihm.wait()
# Ajout : Il faut aussi pour les projets gerer le fichier AppVersion.h
    appversion_update()
# On doit continuer a attendre qu'il n'y ait plus de taches dans la pool
    conf = sys.argv[1]
    if(conf == '1'):
      config = 'Release'
    else:
      config = 'Debug'
    while( liste or ( running.value > 0 ) ):
      if( ( running.value < 5 ) and liste ):
        if(liste):
          cur = liste.pop()
        p = Process( target = nmake, args = (cur,running,config,) )
        p.start()
        running.value = running.value + 1
        # print "**Librairie en cours de fab :"
        # print cur
        # print "Il y a ",running.value," en cours"
        # raw_input()
    print "\nOn lance l edition des liens\n"
    cfg = 'CFG=\"UCINEO_NANCY_CE - Win32 (WCE x86) '+ config + '\"'
    os.system('nmake' + '/F' + 'UCINEO_NANCY_CE.vcn ' + cfg) # En appelant une commande systeme, on bloque l execution du script 



