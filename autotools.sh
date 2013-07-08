#!/bin/bash
# Generation des makefiles a partir de n'importe quelles 
# sources avec les outils Autotools

autoscan -v > sources 
vim Makefile.am sources -O
vim -O configure.ac configure.scan
 aclocal && autoheader && automake --add-missing && autoreconf --install && ./configure
vim -O Makefile Makefile.sauv
make
export INC_DIR="/home/nolaan/dossier_a_supprimer/dev/cps/API_WX_2_8_4_FULL/api/  `wx-config --cppflags`" #variable d environnement pour ajustements
