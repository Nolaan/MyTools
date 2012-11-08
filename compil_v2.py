#!/usr/bin/python

import os, subprocess, multiprocessing, sys, time
from multiprocessing import Process, Value

# liste : liste contenant le nom des librairies a compiler 
# running nombre de threads en cours d'execution

# conf = Value('i',0)
MAX_RUNNING_VALUE = 8
liste = ['UCINEO_NANCY_CE','lib_airlan','lib_dataemb','lib_dataex','lib_emb_reprise','lib_maintenances','lib_manager','lib_newloc','lib_phonie','lib_rapporteur','lib_sae','lib_service','lib_smart','lib_transfic','lib_udpservice','lib_com_pcc','lib_ihm']
# lib_airlan.vcn



running = Value('i',0)

# Module lancant la compilation d une librairie
# On creer un processus, on attend qu'il 

def nmake(lib,running,objet,config):
    if(config == "1"):
      config = 'Release'
    else:
      config = 'Debug'
    print "Objet : "+objet
    cfg = 'CFG='+lib+' - Win32 (WCE x86) '+config
    p = subprocess.Popen(['nmake', '/F', lib+'.vcn', objet, cfg])
    p.wait()
    running.value = running.value - 1


# Corps de la tache, elle s'execute tant qu'il y a des donnees dans la pile

if __name__ == '__main__':
    # ihm = subprocess.Popen(['nmake', '/F'])
    # ihm.wait()
    start_time = time.time()
    conf = sys.argv[1]
    config = conf
    if(conf == "1"):
      conf = ".\\X86Rel\\"
    else:
      conf = ".\\X86Dbg\\"

    lib_com_pcc = [ conf+'lib_com_pcc\\cDIAL_t_AT.obj' , conf+'lib_com_pcc\\cDIAL_t_RAS.obj' , conf+'lib_com_pcc\\cAPP_t_GPRS.obj' , conf+'lib_com_pcc\\cAPP_t_TETRA.obj' , conf+'lib_com_pcc\\TetraBridge.obj' , conf+'lib_com_pcc\\TetraBridgeAcces.obj' , conf+'lib_com_pcc\\Media_Tetra.obj' , conf+'lib_com_pcc\\cMedia_Crc.obj' , conf+'lib_com_pcc\\cMedia_Tetra.obj' , conf+'lib_com_pcc\\cMedia_Tetra_Teltronic.obj' , conf+'lib_com_pcc\\cMedia_Tetra_Motorola.obj' , conf+'lib_com_pcc\\cMedia_Tetra_Sepura.obj' , conf+'lib_com_pcc\\cTetraDial_AT.obj' , conf+'lib_com_pcc\\SaetrMsg.obj' , conf+'lib_com_pcc\\MsgFic.obj']

    lib_dataemb = [ conf+'lib_dataemb\\ASK_SB.OBJ', conf+'lib_dataemb\\BC_WR.OBJ', conf+'lib_dataemb\\ch_sqlite.obj', conf+'lib_dataemb\\CHFIC.OBJ', conf+'lib_dataemb\\CHTECH.OBJ', conf+'lib_dataemb\\cmddrv_data01.obj', conf+'lib_dataemb\\DATAAIGUILLE.OBJ', conf+'lib_dataemb\\DATAALARME.OBJ', conf+'lib_dataemb\\DATAANNONCESTTS.OBJ', conf+'lib_dataemb\\DATACONSIGNE.OBJ', conf+'lib_dataemb\\DATADEPOT.OBJ', conf+'lib_dataemb\\DATAEMB.OBJ', conf+'lib_dataemb\\DATAEMBCPP.OBJ', conf+'lib_dataemb\\DATAEMBPLUS.OBJ', conf+'lib_dataemb\\DataEmbPlus_Calend.obj', conf+'lib_dataemb\\DataEmbPlus_Dev.obj', conf+'lib_dataemb\\DataEmbPlus_Flux.obj', conf+'lib_dataemb\\DataEmbPlus_Mdtm.obj', conf+'lib_dataemb\\DataEmbPlus_Neu.obj', conf+'lib_dataemb\\DataEmbPlus_Pcrs.obj', conf+'lib_dataemb\\DATAEMBPLUS_SB.OBJ', conf+'lib_dataemb\\DataEmbPlus_Sce.obj', conf+'lib_dataemb\\DataEmbPlus_Tech.obj', conf+'lib_dataemb\\DataEmbPlus_Topo.obj', conf+'lib_dataemb\\DATAEMBSAE_TST.OBJ', conf+'lib_dataemb\\DATAFIC.OBJ', conf+'lib_dataemb\\DATAMSGPROG.OBJ', conf+'lib_dataemb\\DATAPARAM.OBJ', conf+'lib_dataemb\\DATARESSOURCESCHAINES.OBJ', conf+'lib_dataemb\\DESB_InfoTopo.obj', conf+'lib_dataemb\\DESB_Mem.obj', conf+'lib_dataemb\\DESB_Reprise.obj', conf+'lib_dataemb\\DeSb_ReprisePrd.obj', conf+'lib_dataemb\\DESB_TabDed.obj', conf+'lib_dataemb\\DFILE.OBJ', conf+'lib_dataemb\\FJDM.OBJ', conf+'lib_dataemb\\SC_C_LAM.OBJ' ]

    lib_dataex = [ conf+'lib_dataex\\DataEx.obj', conf+'lib_dataex\\DataExAcces.obj', conf+'lib_dataex\\Donnee.obj', conf+'lib_dataex\\Donnee_EnBase.obj', conf+'lib_dataex\\Donnee_Format.obj', conf+'lib_dataex\\Donnee_Requete.obj', conf+'lib_dataex\\Donnee_Temps.obj', conf+'lib_dataex\\SeqDonnee.obj', conf+'lib_dataex\\SeqDonneeLink.obj' ]

    lib_emb_reprise = [ conf+'lib_emb_reprise\\cREPRISE_t_DATA.obj', conf+'lib_emb_reprise\\cREPRISE_t_DATA_HORAIRE.obj', conf+'lib_emb_reprise\\cREPRISE_t_MAIN.obj', conf+'lib_emb_reprise\\PARS.OBJ', conf+'lib_emb_reprise\\PrdReprise.obj' ]

    lib_maintenances = [ conf+'lib_maintenances\\HttpConf.obj', conf+'lib_maintenances\\HttpDataEx.obj', conf+'lib_maintenances\\maintAdresseIP.obj', conf+'lib_maintenances\\MAINTAFP.OBJ', conf+'lib_maintenances\\MaintAiguille.obj', conf+'lib_maintenances\\MaintAirlan.obj', conf+'lib_maintenances\\MAINTARRET.OBJ', conf+'lib_maintenances\\MaintAsExterne.obj', conf+'lib_maintenances\\MaintAutoMaint.obj', conf+'lib_maintenances\\MAINTBC.OBJ', conf+'lib_maintenances\\maintCalculateurMR.obj', conf+'lib_maintenances\\maintCAV.obj', conf+'lib_maintenances\\MAINTCFG.OBJ', conf+'lib_maintenances\\Maintcoeff.obj', conf+'lib_maintenances\\maintcptpass.obj', conf+'lib_maintenances\\maintDebug.obj', conf+'lib_maintenances\\maintDMO.obj', conf+'lib_maintenances\\MAINTES.OBJ', conf+'lib_maintenances\\MAINTESD.OBJ', conf+'lib_maintenances\\maintEtiq.obj', conf+'lib_maintenances\\MaintFeux.obj', conf+'lib_maintenances\\MAINTGIR.OBJ', conf+'lib_maintenances\\MAINTGPS.OBJ', conf+'lib_maintenances\\MAINTGYRO.OBJ', conf+'lib_maintenances\\maintIdentCond.obj', conf+'lib_maintenances\\MaintInfoRad.obj', conf+'lib_maintenances\\MAINTLOCABS.OBJ', conf+'lib_maintenances\\maintLocEtiq.obj', conf+'lib_maintenances\\MaintNpr.obj', conf+'lib_maintenances\\MaintNpr2.obj', conf+'lib_maintenances\\MAINTODO.OBJ', conf+'lib_maintenances\\MAINTPHONIE.OBJ', conf+'lib_maintenances\\MaintPhonieTram.obj', conf+'lib_maintenances\\MAINTRAD.OBJ', conf+'lib_maintenances\\MAINTREF.OBJ', conf+'lib_maintenances\\MAINTSAE.OBJ', conf+'lib_maintenances\\MAINTSYNTH.OBJ', conf+'lib_maintenances\\MAINTVLOG.OBJ', conf+'lib_maintenances\\MaintVolBuzzer.obj', conf+'lib_maintenances\\MEDIA_COORD.OBJ', conf+'lib_maintenances\\MEDIA_FNEUTRE.OBJ', conf+'lib_maintenances\\MEDIA_MAIN.OBJ', conf+'lib_maintenances\\MEDIA_TACHE.OBJ', conf+'lib_maintenances\\pagination.obj', conf+'lib_maintenances\\WwwSetup.obj' ]

    lib_manager = [ conf+'lib_manager\\cmddrv_acorel.obj', conf+'lib_manager\\cmddrv_afp01.obj', conf+'lib_manager\\cmddrv_eqtlw01.obj', conf+'lib_manager\\cmddrv_gir02.obj', conf+'lib_manager\\cmddrv_gir09.obj', conf+'lib_manager\\cmddrv_gps02.obj', conf+'lib_manager\\cmddrv_net03.obj', conf+'lib_manager\\cmddrv_odo01.obj', conf+'lib_manager\\cmddrv_pcrs01.obj', conf+'lib_manager\\cmddrv_por01.obj', conf+'lib_manager\\cmddrv_pup03.obj', conf+'lib_manager\\cmddrv_pup04.obj', conf+'lib_manager\\CMDDRV_SYNTH_UCINEO.obj', conf+'lib_manager\\cmddrv_transport01.obj', conf+'lib_manager\\cmddrv_transport02.obj', conf+'lib_manager\\CptPassMan.obj', conf+'lib_manager\\crclrc.obj', conf+'lib_manager\\CVocalPlayer.obj', conf+'lib_manager\\drv_lama01.obj', conf+'lib_manager\\MANAGER.OBJ', conf+'lib_manager\\ManCpp.obj', conf+'lib_manager\\MNGCMD.OBJ', conf+'lib_manager\\PERIPHTST.OBJ', conf+'lib_manager\\t01_crclrc.obj', conf+'lib_manager\\Volume.obj', conf+'lib_manager\\WatDapp.obj' ]

    lib_newloc = [ conf+'lib_newloc\\APP_LOC.OBJ', conf+'lib_newloc\\Cap.obj', conf+'lib_newloc\\GDEPOT.OBJ', conf+'lib_newloc\\Geo.obj', conf+'lib_newloc\\Loc.obj', conf+'lib_newloc\\LOCALISATION.OBJ', conf+'lib_newloc\\LOCGPS.OBJ', conf+'lib_newloc\\LOCSURV.OBJ', conf+'lib_newloc\\PointPolygone.obj', conf+'lib_newloc\\PointTopologique.obj', conf+'lib_newloc\\SLOC_AcqEtiq.obj', conf+'lib_newloc\\SLOC_AcqGps.obj', conf+'lib_newloc\\SLOC_AcqLasm.obj', conf+'lib_newloc\\SLOC_AcqOdo.obj', conf+'lib_newloc\\SLOC_AcqPor.obj', conf+'lib_newloc\\SLOC_Appli.obj', conf+'lib_newloc\\SLOC_AsserviKtroue.obj', conf+'lib_newloc\\SLOC_AsserviKtroue_Nav.obj', conf+'lib_newloc\\SLOC_DelocOdo.obj', conf+'lib_newloc\\SLOC_DepotEtiq.obj', conf+'lib_newloc\\SLOC_DepotGps.obj', conf+'lib_newloc\\SLOC_DistEtiq.obj', conf+'lib_newloc\\SLOC_DmdTm.obj', conf+'lib_newloc\\SLOC_ElaAvret.obj', conf+'lib_newloc\\SLOC_ElaCurve.obj', conf+'lib_newloc\\SLOC_ElaOdoElab.obj', conf+'lib_newloc\\SLOC_Espion.obj', conf+'lib_newloc\\SLOC_FctGps.obj', conf+'lib_newloc\\SLOC_FiltGps.obj', conf+'lib_newloc\\SLOC_LocAiguille.obj', conf+'lib_newloc\\SLOC_LocEtiq.obj', conf+'lib_newloc\\SLOC_LocGps.obj', conf+'lib_newloc\\SLOC_News.obj', conf+'lib_newloc\\SLOC_OldNews.obj', conf+'lib_newloc\\SLOC_PosArret.obj', conf+'lib_newloc\\SLOC_PresPoly.obj', conf+'lib_newloc\\SLOC_Sec.obj', conf+'lib_newloc\\SLOC_Zc.obj', conf+'lib_newloc\\TronconTopologique.obj', conf+'lib_newloc\\Zone.obj' ]

    lib_phonie = [ conf+'lib_phonie\\cPhonieBrassage.obj', conf+'lib_phonie\\cPhonieTetra.obj' ]

    lib_rapporteur = [ conf+'lib_rapporteur\\database.obj', conf+'lib_rapporteur\\enregistrement.obj', conf+'lib_rapporteur\\enregistreur.obj', conf+'lib_rapporteur\\rapporteur.obj', conf+'lib_rapporteur\\rpt_cfg.obj', conf+'lib_rapporteur\\rpt_ficdata.obj' ]

    lib_sae = [ conf+'lib_sae\\AffLigne.obj', conf+'lib_sae\\affpas.obj', conf+'lib_sae\\APP_SAE.OBJ', conf+'lib_sae\\corres.obj', conf+'lib_sae\\DSO.obj', conf+'lib_sae\\ENCADRANT.OBJ', conf+'lib_sae\\Feu1.obj', conf+'lib_sae\\gdtech.obj', conf+'lib_sae\\GIR.OBJ', conf+'lib_sae\\MSG_MNTL.OBJ', conf+'lib_sae\\MSGCOND.OBJ', conf+'lib_sae\\PDS.OBJ', conf+'lib_sae\\RCYCLE.OBJ', conf+'lib_sae\\RECAL.OBJ', conf+'lib_sae\\RECUEILA.OBJ', conf+'lib_sae\\RECUEILC.OBJ', conf+'lib_sae\\RECUEILF.OBJ', conf+'lib_sae\\RECUEILG.OBJ', conf+'lib_sae\\RLV.OBJ', conf+'lib_sae\\SERVICE.OBJ', conf+'lib_sae\\SONOPAS.obj' ]

    lib_service = [ conf+'lib_service\\Alrm_Api.obj', conf+'lib_service\\Alrm_Fct.obj', conf+'lib_service\\atm.obj', conf+'lib_service\\atm2.obj', conf+'lib_service\\IOF.obj' ]

    lib_smart = [ conf+'lib_smart\\array.obj'] #, conf+'lib_smart\\bin.obj', conf+'lib_smart\\cBIN_t_Val16.obj', conf+'lib_smart\\cBIN_t_Val24.obj', conf+'lib_smart\\cBIN_t_Val32.obj', conf+'lib_smart\\cBIN_t_Val32i.obj', conf+'lib_smart\\cBIN_t_Val8.obj', conf+'lib_smart\\cFileWx.obj', conf+'lib_smart\\cFluxMem.obj', conf+'lib_smart\\cGTMH_String.obj', conf+'lib_smart\\cGTMH_Tab.obj', conf+'lib_smart\\cIO_Ls_Socket_t_MAIN.obj', conf+'lib_smart\\cmd.obj', conf+'lib_smart\\CMDDRV_NET01.OBJ', conf+'lib_smart\\CMDDRV_NET_NCE.obj', conf+'lib_smart\\CMDDRV_NET_SOCKET.obj', conf+'lib_smart\\cmddrv_pup_tce.obj', conf+'lib_smart\\cmdl.obj', conf+'lib_smart\\cmdl_fs.obj', conf+'lib_smart\\cmdl_io.obj', conf+'lib_smart\\cmdl_lw.obj', conf+'lib_smart\\Cmdl_MainEntry.obj', conf+'lib_smart\\cmdl_mp.obj', conf+'lib_smart\\cmdl_osgdbg.obj', conf+'lib_smart\\cmdl_res.obj', conf+'lib_smart\\cmdl_spy.obj', conf+'lib_smart\\cmdl_trcfg.obj', conf+'lib_smart\\CMDL_USER.OBJ', conf+'lib_smart\\command.obj', conf+'lib_smart\\cOS_t_DATA.obj', conf+'lib_smart\\cOS_t_NEWS.obj', conf+'lib_smart\\cOS_t_QUEUE.obj', conf+'lib_smart\\COsgProxyClient.obj', conf+'lib_smart\\COsgSocketBase.obj', conf+'lib_smart\\COsgSocketTcp.obj', conf+'lib_smart\\COsgTcpProxyServer.obj', conf+'lib_smart\\COsgTcpServer.obj', conf+'lib_smart\\cPseudoTimer.obj', conf+'lib_smart\\cUSER_t_TRACE.obj', conf+'lib_smart\\Factory.obj', conf+'lib_smart\\fic_pc.obj', conf+'lib_smart\\ficdata.obj', conf+'lib_smart\\ficdata_header.obj', conf+'lib_smart\\ficdata_p1.obj', conf+'lib_smart\\ficdata_struct.obj', conf+'lib_smart\\ficemb.obj', conf+'lib_smart\\FileDevSioDrv.obj', conf+'lib_smart\\FileDevSioTheDrv.obj', conf+'lib_smart\\FileDevStdio.obj', conf+'lib_smart\\fs.obj', conf+'lib_smart\\fs_cache.obj', conf+'lib_smart\\fs_util.obj', conf+'lib_smart\\fs_winCE.obj', conf+'lib_smart\\Fs_wx.obj', conf+'lib_smart\\fstrace.obj', conf+'lib_smart\\gest_fifo.obj', conf+'lib_smart\\gest_fifo_obs.obj', conf+'lib_smart\\Gtmh_bsearch.obj', conf+'lib_smart\\GTMH_FS1.OBJ', conf+'lib_smart\\GTMH_STR1.OBJ', conf+'lib_smart\\GTMH_STR2.OBJ', conf+'lib_smart\\GTMH_STR3.OBJ', conf+'lib_smart\\GTMH_STR4.OBJ', conf+'lib_smart\\gtmh_vargs.obj', conf+'lib_smart\\IneoFile.obj', conf+'lib_smart\\IneoFileIo.obj', conf+'lib_smart\\Io_Ls_Socket_plug.obj', conf+'lib_smart\\io_simule.obj', conf+'lib_smart\\io_superviseur.obj', conf+'lib_smart\\libstr.obj', conf+'lib_smart\\list.obj', conf+'lib_smart\\MemoStr.obj', conf+'lib_smart\\NET_NCE_P.obj', conf+'lib_smart\\noy_at.obj', conf+'lib_smart\\noy_ne.obj', conf+'lib_smart\\noy_qu.obj', conf+'lib_smart\\noy_socket_linux.obj', conf+'lib_smart\\noy_socket_nuc.obj', conf+'lib_smart\\noy_socket_win95.obj', conf+'lib_smart\\noy_ti.obj', conf+'lib_smart\\OsgPlus.obj', conf+'lib_smart\\sfs.obj', conf+'lib_smart\\smart_class.obj', conf+'lib_smart\\SmartPtr.obj', conf+'lib_smart\\sys_app.obj', conf+'lib_smart\\sys_fs.obj', conf+'lib_smart\\sys_fs1.obj', conf+'lib_smart\\sys_lzh.obj']
    
    lib_smart = lib_smart + [ conf+'lib_smart\\sys_mem.obj', conf+'lib_smart\\sys_to_lzh.obj', conf+'lib_smart\\TKM.OBJ', conf+'lib_smart\\trace.obj', conf+'lib_smart\\trst.obj' , conf+'lib_smart\\sys_lzh_to.obj' ]

    lib_transfic = [ conf+'lib_transfic\\DechRecueil.obj', conf+'lib_transfic\\RecFic.obj', conf+'lib_transfic\\RecFicClient.obj', conf+'lib_transfic\\RecFicServeur.obj', conf+'lib_transfic\\TransFic.obj' ]

    lib_udpservice = [ conf+'lib_udpservice\\base64.obj', conf+'lib_udpservice\\ComState.obj', conf+'lib_udpservice\\CtxtReseau.obj', conf+'lib_udpservice\\GestSaeMsg.obj', conf+'lib_udpservice\\GestServiceMsg.obj', conf+'lib_udpservice\\IpAddress.obj', conf+'lib_udpservice\\rmd160.obj', conf+'lib_udpservice\\sae_code.obj', conf+'lib_udpservice\\UdpAddress.obj', conf+'lib_udpservice\\UdpBridge.obj', conf+'lib_udpservice\\UdpLink.obj', conf+'lib_udpservice\\UdpLinkCfg.obj', conf+'lib_udpservice\\UdpProtocole.obj', conf+'lib_udpservice\\UdpSocket.obj' ]

    lib_ihm = [ conf+'lib_ihm\\Ihm_Acces.obj', conf+'lib_ihm\\Ihm_BargPicto.obj', conf+'lib_ihm\\Ihm_Com.obj', conf+'lib_ihm\\Ihm_Data.obj', conf+'lib_ihm\\ihm_DataPicto.obj', conf+'lib_ihm\\Ihm_DataTxt.obj', conf+'lib_ihm\\Ihm_DlgTxt.obj', conf+'lib_ihm\\Ihm_Key.obj', conf+'lib_ihm\\Ihm_Objet.obj', conf+'lib_ihm\\Ihm_Picto.obj', conf+'lib_ihm\\Ihm_Son.obj', conf+'lib_ihm\\Ihm_Target.obj', conf+'lib_ihm\\Ihm_Txt.obj', conf+'lib_ihm\\Ihm_Voyant.obj', conf+'lib_ihm\\Ihm_Zone.obj', conf+'lib_ihm\\IhmData.obj', conf+'lib_ihm\\IhmEvent.obj', conf+'lib_ihm\\IhmServ.obj', conf+'lib_ihm\\IhmTarget_cmd.obj' ]
    
    lib_airlan = [ conf+'lib_airlan\\Address.obj', conf+'lib_airlan\\ArbitreWifi.obj', conf+'lib_airlan\\cmddrv_net05.obj', conf+'lib_airlan\\COM_WL.OBJ', conf+'lib_airlan\\DemoNet.obj', conf+'lib_airlan\\IpAddress.obj', conf+'lib_airlan\\MacAddress.obj', conf+'lib_airlan\\ManNucNet.obj', conf+'lib_airlan\\net05_rx.obj', conf+'lib_airlan\\net05_tx.obj', conf+'lib_airlan\\NetworkAdapter.obj', conf+'lib_airlan\\NetworkApi.obj', conf+'lib_airlan\\NetworkSettings.obj', conf+'lib_airlan\\NucNet.obj', conf+'lib_airlan\\sfs2.obj', conf+'lib_airlan\\sfsdaemon.obj', conf+'lib_airlan\\Socket.obj', conf+'lib_airlan\\SocketUdap.obj', conf+'lib_airlan\\UdpAddress.obj', conf+'lib_airlan\\WifiAdapter.obj' ]

    UCINEO_NANCY_CE = [ conf+'\\UCINEO_NANCY_CE\\ApiFctSup_bouchon.obj', conf+'\\UCINEO_NANCY_CE\\ConvertUTF.obj', conf+'\\UCINEO_NANCY_CE\\HttpInterface.obj', conf+'\\UCINEO_NANCY_CE\\InterfaceSupUcineo.obj', conf+'\\UCINEO_NANCY_CE\\io_pc.obj', conf+'\\UCINEO_NANCY_CE\\Io_plug_com.obj', conf+'\\UCINEO_NANCY_CE\\Io_plug_counter.obj', conf+'\\UCINEO_NANCY_CE\\Io_plug_gain.obj', conf+'\\UCINEO_NANCY_CE\\Io_plug_input.obj', conf+'\\UCINEO_NANCY_CE\\Io_plug_intit.obj', conf+'\\UCINEO_NANCY_CE\\Io_plug_matrice.obj', conf+'\\UCINEO_NANCY_CE\\Io_plug_output.obj', conf+'\\UCINEO_NANCY_CE\\Iodlg.obj', conf+'\\UCINEO_NANCY_CE\\main.obj', conf+'\\UCINEO_NANCY_CE\\noyau_win32.obj', conf+'\\UCINEO_NANCY_CE\\SaeSupInterface_Cfg.obj' ]

    while(liste):
      cur = liste.pop()
      objet = eval(cur).pop()
      while(eval(cur)):
        print objet
        while True:
          if( running.value < MAX_RUNNING_VALUE ):
              p = Process( target = nmake, args = (cur,running,objet,config) )
              p.start()
              running.value = running.value + 1
              objet = eval(cur).pop()
              print "Il y a ",running.value," en cours"
              break

    print running.value
    time.sleep(6)
    # while ( running.value <= 0 ):
    #   print running.value
    if(config == "1"):
      cfg = 'CFG=UCINEO_NANCY_CE - Win32 (WCE x86) Release'
    else:
      cfg = 'CFG=UCINEO_NANCY_CE - Win32 (WCE x86) Debug'
    p = subprocess.Popen(['nmake', '/F',  'UCINEO_NANCY_CE.vcn ',cfg])
    p.wait()
    # elapsed_time = time.time() - start_time
    # print "Compilation effectuee en : "+elapsed_time.str()+" secondes"

