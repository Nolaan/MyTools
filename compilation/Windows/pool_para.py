import os, subprocess, multiprocessing, sys
from multiprocessing import Process, Value
from multiprocessing import Pool

# liste : liste contenant le nom des librairies a compiler 
# running nombre de threads en cours d'execution

conf = Value('i',0)


def nmake(obj):
    lib = 'lib_smart'
    if(conf == '1'):
      config = 'Release'
    else:
      config = 'Debug'
    cfg = 'CFG='+lib+' - Win32 (WCE x86) '+config
    # print "Config courante : "+cfg
    p = subprocess.Popen(['nmake', '/F',  lib+'.vcn', cfg, '.\\X86Dbg\\'+obj ])
    p.wait()
    # running.value = running.value - 1

# Corps de la tache, elle s'execute tant qu'il y a des donnees dans la pile

if __name__ == '__main__':
    conf = sys.argv[1]
    # liste = ['lib_smart','lib_ihm','lib_airlan','lib_com_pcc','lib_dataemb','lib_dataex','lib_emb_reprise','lib_maintenances','lib_manager','lib_newloc','lib_phonie','lib_rapporteur','lib_sae','lib_service','lib_transfic','lib_udpservice'].__iter__()
    lib_smart = [ 'lib_smart\\array.obj', 'lib_smart\\bin.obj', 'lib_smart\\cBIN_t_Val16.obj', 'lib_smart\\cBIN_t_Val24.obj', 'lib_smart\\cBIN_t_Val32.obj', 'lib_smart\\cBIN_t_Val32i.obj', 'lib_smart\\cBIN_t_Val8.obj', 'lib_smart\\cFileWx.obj', 'lib_smart\\cFluxMem.obj', 'lib_smart\\cGTMH_String.obj', 'lib_smart\\cGTMH_Tab.obj', 'lib_smart\\cIO_Ls_Socket_t_MAIN.obj', 'lib_smart\\cmd.obj', 'lib_smart\\CMDDRV_NET01.OBJ', 'lib_smart\\CMDDRV_NET_NCE.obj', 'lib_smart\\CMDDRV_NET_SOCKET.obj', 'lib_smart\\cmddrv_pup_tce.obj', 'lib_smart\\cmdl.obj', 'lib_smart\\cmdl_fs.obj', 'lib_smart\\cmdl_io.obj', 'lib_smart\\cmdl_lw.obj', 'lib_smart\\Cmdl_MainEntry.obj', 'lib_smart\\cmdl_mp.obj', 'lib_smart\\cmdl_osgdbg.obj', 'lib_smart\\cmdl_res.obj', 'lib_smart\\cmdl_spy.obj', 'lib_smart\\cmdl_trcfg.obj', 'lib_smart\\CMDL_USER.OBJ', 'lib_smart\\command.obj', 'lib_smart\\cOS_t_DATA.obj', 'lib_smart\\cOS_t_NEWS.obj', 'lib_smart\\cOS_t_QUEUE.obj', 'lib_smart\\COsgProxyClient.obj', 'lib_smart\\COsgSocketBase.obj', 'lib_smart\\COsgSocketTcp.obj', 'lib_smart\\COsgTcpProxyServer.obj', 'lib_smart\\COsgTcpServer.obj', 'lib_smart\\cPseudoTimer.obj', 'lib_smart\\cUSER_t_TRACE.obj', 'lib_smart\\Factory.obj', 'lib_smart\\fic_pc.obj', 'lib_smart\\ficdata.obj', 'lib_smart\\ficdata_header.obj', 'lib_smart\\ficdata_p1.obj', 'lib_smart\\ficdata_struct.obj', 'lib_smart\\ficemb.obj', 'lib_smart\\FileDevSioDrv.obj', 'lib_smart\\FileDevSioTheDrv.obj', 'lib_smart\\FileDevStdio.obj', 'lib_smart\\fs.obj', 'lib_smart\\fs_cache.obj', 'lib_smart\\fs_util.obj', 'lib_smart\\fs_winCE.obj', 'lib_smart\\Fs_wx.obj', 'lib_smart\\fstrace.obj', 'lib_smart\\gest_fifo.obj', 'lib_smart\\gest_fifo_obs.obj', 'lib_smart\\Gtmh_bsearch.obj', 'lib_smart\\GTMH_FS1.OBJ', 'lib_smart\\GTMH_STR1.OBJ', 'lib_smart\\GTMH_STR2.OBJ', 'lib_smart\\GTMH_STR3.OBJ', 'lib_smart\\GTMH_STR4.OBJ', 'lib_smart\\gtmh_vargs.obj', 'lib_smart\\IneoFile.obj', 'lib_smart\\IneoFileIo.obj', 'lib_smart\\Io_Ls_Socket_plug.obj', 'lib_smart\\io_simule.obj', 'lib_smart\\io_superviseur.obj', 'lib_smart\\libstr.obj', 'lib_smart\\list.obj', 'lib_smart\\MemoStr.obj', 'lib_smart\\NET_NCE_P.obj', 'lib_smart\\noy_at.obj', 'lib_smart\\noy_ne.obj', 'lib_smart\\noy_qu.obj', 'lib_smart\\noy_socket_linux.obj', 'lib_smart\\noy_socket_nuc.obj', 'lib_smart\\noy_socket_win95.obj', 'lib_smart\\noy_ti.obj', 'lib_smart\\OsgPlus.obj', 'lib_smart\\sfs.obj', 'lib_smart\\smart_class.obj', 'lib_smart\\SmartPtr.obj', 'lib_smart\\sys_app.obj', 'lib_smart\\sys_fs.obj', 'lib_smart\\sys_fs1.obj', 'lib_smart\\sys_lzh.obj']
    lib_smart= lib_smart+[ 'lib_smart\\sys_mem.obj', 'lib_smart\\sys_to_lzh.obj', 'lib_smart\\TKM.OBJ', 'lib_smart\\trace.obj', 'lib_smart\\trst.obj' , 'lib_smart\\sys_lzh_to.obj' ]
    liste = lib_smart.__iter__()
    pool = Pool(processes=15)
    pool.map(nmake, liste)
    # subprocess.Popen(['nmake', '/F', 'UCINEO_NANCY_CE.vcn'])



