import os, shutil, sys, fnmatch, re 
import datetime

# ret = []
# for root, directory, files in os.walk('../'):
#   for name in files:
#     if fnmatch.fnmatch(name, 'test.py'):
#       print name + ": fichier invalide!\n"

# Default variables

# Chemin du fichier AppVersion.h
MY_APPVERSION = "api\\AppVersion.h"

# Numero de version de lapplication
# Elle doit obligatoirement etre assignee
# Mais pour plus de commodite on la laisse 
# a la version courante
getcurver = open( MY_APPVERSION, 'r' )
cline = getcurver.readline()  
while( re.search(".*MAJEUR *([0-9]{1,2}).*", cline )== None ):
  cline = getcurver.readline()  
MAJEUR_VER = int(re.sub(".*MAJEUR *([0-9]{1,2}).*","\\1", cline))

cline = getcurver.readline()  
while( re.search(".*REVISION *([0-9]{1,2}).*", cline )== None ):
  cline = getcurver.readline()  
CUR_VER = int(re.sub(".*REVISION *([0-9]{1,2}).*","\\1", cline))

# Il y a des conditions au fonctionnement ci dessous :
# 1. que le fichier respecte son heritage => le nom de version
# est habituellement indique a la fin du fichier, avant la 
# revision en tout cas.
# 2. qu il n y ai pas un prefixe qui commence par le match

while ( re.search(".*INEO_k_NAME *(\".*\").*", cline )== None ):
  cline = getcurver.readline()  
APP_NAME = re.sub(".*INEO_k_NAME *(\".*\").*","\\1", cline)
getcurver.close()
# Variables pour la mise a jour de la datation
now   = datetime.datetime.now()
DAY   = now.day
MONTH = now.month
YEAR  = now.year
HOUR  = now.hour
MIN   = now.minute
# Buffer nouveau fichier
buf_out = []

# Fonction de recuperation du nom de l appli
def get_app_name():
  return APP_NAME

# Fonction de recuperation du num de version
def get_num_ver():
  return CUR_VER

# Fonction de recuperation du num de version
def get_maj_num_ver():
  return MAJEUR_VER
# Fonction de mise a jour du fichier Appversion
def appversion_update( APP_VER = CUR_VER ):

# Motifs a remplacer par les regex
  motifs = [[ "INEO_k_VERSION_REVISION" , str( APP_VER )      , "[0-9]{1,2}" ],
            [ "INEO_k_DATE_JOUR"        , str( DAY     )      , "[0-9]{1,2}" ],
            [ "INEO_k_DATE_MOIS"        , str( MONTH   )      , "[0-9]{1,2}" ],
            [ "INEO_k_DATE_ANNEE"       , str( YEAR    )      , "[0-9]{4}"   ],
            [ "INEO_k_DATE_HEURE"       , str( HOUR    )      , "[0-9]{1,2}" ],
            [ "INEO_k_DATE_MINUTE"      , str( MIN     )      , "[0-9]{1,2}" ]
            ]

  appversion = open( MY_APPVERSION, 'r+' )
  try:
    for i in range( len( motifs ) ):
      line = appversion.readline()
      while ( re.search(".*" + motifs[i][0] + ".*", line ) == None ):
        print line
        buf_out.append(line)
        line = appversion.readline()
      if ( re.match(".*" + motifs[i][0] + ".*", line ) ):
        result = re.sub("(.*"+ motifs[i][0] + " *) " + motifs[i][2],"\\1 " + motifs[i][1], line)
        #appversion.write( result + "\n" )
        buf_out.append(result  )
        print result
  finally:
# On lit le fichier jusqu a la fin...
    while( line != '' ):
      line = appversion.readline()
      buf_out.append(line)

# Adaptation Vindove, on est obliger
# de fermer le fd et le rouvrir en
# ecriture, sinon IO Error
    appversion.close()
    appversion = open( MY_APPVERSION, 'w' )
    for line in buf_out:
      appversion.write(line)
    appversion.flush()
    appversion.close()
    print buf_out
    print "File has been closed!\n"


if __name__ == '__main__':
  appversion_update()
