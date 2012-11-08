import os, time, shutil, sys
# import de la fonction permettant la mise
# a jour du fichier Appversion
from upd_version import *        # import des informations a partir du fichier de version (Appversion.h)
from os.path import join, getsize
from shutil import ignore_patterns


# Script de livraison de version ( a placer dans le repertoire des fichiers vcw)
# Fonctions : a partir d'un repertoire donne, il cree
# le zip de gel de version ( optionnellement pourra editer la fiche de version)
#

# Etapes de la livraison de version : 
# Une fiche de version decrivant le gel, les modifications recentes, les FNC et DM livrees par cette version, les compatibilites, les informations CVS,
# les fichiers (et outils) de programmation des logiciels associes a cette version,
# une archive de sauvegarde de l'environnement de developpement,
# des outils. 
# Le tout est a placer dans : gel\saeiv\embarque\Ville de l'affaire
#

# Recup et clean du repertoire de developpement


# 
#
deliv_dir = "../../Gel_de_version/"           # Repertoire de gel
root_dir = "../"                              # Repertoire des sources du projet et des outils
squel_dir = "D:\Affaires\Repertoire_type"     # Repertoire des squelettes 
num_version= "0.00"                           # Valeur par defaut qui devrait interpeller sur un probleme latent  quand elle est mentionnee
IGNORE_PATTERNS = ignore_patterns( '.git',    # Liste de chemins et fichiers a ignorer
                                   '*.pyc',
                                   '.gitignore',
                                   'tags',
                                   'touch',
                                   '*.vcb',
                                   '*.vcp',
                                   '*.vcw',
                                   '*.vcn',
                                   '*.swp',
                                   "compil_v2.py",
                                   "gel_de_version.py",
                                   "paragen.py",
                                   "pool_para.py",
                                   "PyTidy.py",
                                   "script.sed",
                                   "res_compil*.log",
                                   "test.py",
                                   "FV.sed",
                                   "upd_version.py"
                                   )
NUM      = get_num_ver()
MAJEUR   = get_maj_num_ver()

# Utility to copy files os independent
# NOTE: Do not preserve ACLs on Linux
# so one of the tricks should be to tar or gzip the directory and 
# then unzip it...

def copytree(src, dst, symlinks=False, ignore=IGNORE_PATTERNS):
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

# Creation du repertoire de destination
    if not os.path.exists(dst):
      os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            print "Ignored : " + name + " !\n"
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks, ignore)
            else:
                shutil.copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error), why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except IOError as err:
            errors.extend(err.args[0])
    try:
        shutil.copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError, why:
        errors.extend((src, dst, str(why)))
    if errors:
        raise IOError(errors)



def check_req ():
# Verification des prerequis a la generation d'un gel de version
# check du repertoire de livraison
# s'il n'existe pas il faut le creer et recopier le squelette
  if not os.path.exists(deliv_dir):
    os.makedirs(deliv_dir)
    copytree(squel_dir,deliv_dir)
  # On copie les sources dans le repertoire de gel
  copytree(root_dir,deliv_dir)

    


#
def make_ver(app_name, ver_num):
# Prend en parametre le nom de la version et le numero de version
# Clean du repertoire
  os.chdir( deliv_dir ) # On se place dans le repertoire de livraison
  # print "Repertoire courant : " + os.getcwd()
  file_list = []        # Liste des script de nettoyage des repertoires projet
  for root, dirs, files in os.walk('.\\'):
    if '.git' in dirs:
      dirs.remove('.git')  # don't visit GIT directories
    for file_name in files:
      if  (re.match("Clr.*.bat",file_name) != None ):
        file_list.append( os.path.join( root , file_name ) )
        # print "Script trouve : " + os.path.join( root , file_name )
# Avant de nettoyer il serait judicieux de recuperer l exe, le copier a la
# racine et le transformer en F89_XXXX.RES
# Execution des script de nettoyage
  for script in file_list:
    print "Execution de : " + script + "\n"
    print "Repertoire du script : " + os.path.dirname(script) + "\n"
    cur_dir = os.getcwd()
    dest_dir = os.path.dirname(script)
    print "Premier repertoire courant : " + cur_dir
    print dest_dir
    os.chdir( dest_dir )
    # Si on se trouve dans le repertoire wince, on regenere  l exe 
    if ( re.search("WinCE", dest_dir) != None ):
      print "Dans WincCE!!!"
      # os.system("python paragen.py 1 > res_compil.py")
      # for files in os.listdir('.\\X86Rel'):
      #   if fnmatch.fnmatch(files, 'UCINEO_*.exe'):
      #     executable = files
      # Il faut maintenant le copier au dessus et faire le .RES 
      print 'Copie du fichier executable Windows CE'
      shutil.copy2('.\\X86Rel\\' + executable , '..\\' ) # Copie effective du fichier executable
      print 'Sauvegarde du fichier executable Windows CE'
      import zipfile, fnmatch
      F89 = 'F89_0' + MAJEUR + NUM + '.RES'
      print 'Creation de l\'archive F89 : ' + F89
      zf = zipfile.ZipFile( F89 , mode='w')
      try:
          print 'Ajout de ' + executable
          zf.write(executable)
      finally:
          print 'Fermeture et ecriture du fichier .RES'
          zf.close(F89)
          shutil.move( F89, '..\\..\\' ) # On bouge le .res en dehors du repertoire de version

       
    print "Rep courant : " + os.getcwd()
    try:
      os.system(os.path.basename(script)) # Execution du script de netttoyage
    finally:
      os.chdir( cur_dir )
    # print "Rep change : " + os.getcwd()
#
# A partir d ici le repertoire est correctement duplique
# On peut remplir la fiche de version zipper etc...
  


if __name__ == '__main__': 

  # Premiere etape, on genere le fichier executable
  os.system("python paragen.py 1 > res_compil.py")
  make_ver("nancy","86")
#   APP_NAME = get_app_name()       // NOM DE L APPLI
#   NUM      = get_num_ver()        // Numero de revision
#   MAJEUR   = get_maj_num_ver()    // Numero de version Majeur
#   check_req();
# # Creation effective du gel de version.
#   make_ver(APP_NAME, NUM)
#   # zip_ver
# 
