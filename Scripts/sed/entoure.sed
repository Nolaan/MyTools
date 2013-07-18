# Cette commande transforme le fichier en un buffer d'une seule ligne pour 
# faciliter la regex
sed -n '1h;1!H;${;g;s/[TKM]\{,3\}_trace *([^;]*;/#FUCKLESTRACES\n& \n#FINI/g;p;}' dospage.c > toto.c


# Explications : 
# sed -n '
# Si c'est la premiere ligne, on copie/sauvegarde le patterne dans le buffer
# 1h
# Sinon on ajoute la ligne au buffer existant
# 1!H
# Si on est a la derniere ligne...
# $ {
#         # On copie le buffer de sauvegarde vers le buffer de pattern
#         g
#         # Commande de substitution : 
#         s
#         /[TKM]\{,3\}_trace *([^;]*; On matche que les combinaisons de TKM- au plus 3 caract. ou rien...
#                                     l'astuce vient du fait que on empeche le match de notre delimiteur
#                                     [^;] sed s'arretera donc à celui si, sauf qu'on lui demande de matcher
#                                     aussi ce delimiteur d'ou => [^*]*(tout les carct sauf;)
#                                                              => [^;*]*; Tout les caracteres sauf ";" plus ";"
#         /#FUCKLESTRACES\n& \n#FINI/g  Ici & désigne le pattern qui a matché
#         # print
#         p
# }
