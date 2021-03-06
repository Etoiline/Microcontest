#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libmicrocontest2 import *
from hashlib import sha1
from urllib import urlencode
from urllib2 import *
import re
import functools
import cookielib


"""
L'algorithme utilisé pour crypter la chaîne originale est le chiffre de Vigenère.
La chaîne à décrypter se trouve dans la variable txt_crypte et la clef utilisée pour le cryptage dans la variable clef. Vous devez renvoyer la chaîne décryptée dans la variable txt_clair

Note importante : Le texte clair, qui est en Français, comporte des espaces : Ces espaces sont laissés tels quels par l'algorithme de cryptage !
Par exemple, avec la clef "KEY" :

Texte clair :    MICROCONTEST C EST TROP FACILE
Key :            KEYKEYKEYKEY K EYK EYKE YKEYKE
Texte crypté :   WMABSAYRROWR M IQD XPYT DKGGVI
"""




username = ""
password = ""
cont_id = 10
url = "http://www.microcontest.com/contests/"+str(cont_id)+"/contest.php"
url_result = "http://www.microcontest.com/contests/"+str(cont_id)+"/validation.php"

data = [("username", username), ("password", sha1(password).hexdigest()),("ID", cont_id), ("contestlogin", 1), ("version", 2)]


opener = build_opener(HTTPCookieProcessor())
page = opener.open(url, urlencode(data)).read()
print (page)


"""
#####Exemple de données retournées dans page#####
page = "Nombre_variables=2<br/>[txt_crypte]<br/>Longueur=6287<br/>Valeur=IRQM WHJ CCOUZSZL  OV DMKH DCCJXV OUXQRBB NQ TVMODC  PMUHIH  KHQUIQLDEH JTWRWTEH HIQ L HSFWNDZH  RXDEZQG FFIZTQK RMKUZSZX OV  HZTLE DWNU ISNXUDSZ EHJ DWKWVG L THIOOX  HK ZI ZUFGAX PFIYNHKHM   XW CO UTLXFM EBUWM IRLGATQK ZMNUJ PMKOZBML    OR ZWGJLS   BBHEBM LRLTNKDZH INVJW JXDLQWNS DCQGV US  T AXDWLBWV SB WH C SBHXWTMFHEH LX OR HIBOCS  TT FYSUBQVS TNL  JSUUORWB MUVG KHPDCLX SFIZ FREHMK  FFAUX V ZZ MNW WCVWX VH  YN LC DCM SRGAXU GOZ WHJ TMGWVG  WN LC B INURWB IRZBB KLJECX XES  UTLE XIWLJ  WT KHJDQKDZH ATQJ AIEDZGM EHJ DWNVJWMKHJ RC VKRFJHQ   MCGTLK QTTLI RIGV CO VNLK  GCTLK HZTQHIQEOV  TIBW R ZI LHEGIMLFB  L TYFWZ WX DOBBQ RI AHLI GML YVHMFHEHA MUVAXXV JIZ EH TCZIV  UI  ZXVKS  QE QV RMIHEGIBW GZCL PRZIWUFWBXPVBB LHJ TWKFVG  CGH  RRZXVJS TNL VHIBW MSVNH  JW ZTSZRM  JX VZTX HKCVGDZH TX FYOVMLVF  IN  EFIB WH KFWBV JSUTLESA  HQ CS KBWRWB IDIAQ EHJ PWGV YSZLFYSCKV US  TT IFGAX   SRG CG QV FWNORWB LD SSZELES RNVHI IN SCOV BQTZQGH  U IV  MURWV IOLG DBI  EW VX O VAJTOCOQM HEGCBWV  ODXF RIBTQK RM  VRIFMVWZCV  LD GSBBWV HIBOCS TNL GSZFHKHIBW US AX JCWALHI DIKWFIB  XW  JSA UURG IODZSVM EVOC XWIS NBQJ SB UORBKL FFAUX FVIF W XES  NXPDS  QEV GOZTLJGIBHEH MG IVF AHXJ ZI IHRI LXOZQIMH  KSTEHDSVM LCG  UXQRWMGW IILXPVBB ED SSAHJES  RTPRWA BO ES AX SCOQZQRWB  IDI  TQXUKS ATQJ RWNWV  AMFH HIIGG ZZ ZTORWB WH WOBBJLS  WG QV ZCB  UVDZHFYOQM TLS LX QV DIL FFAXKHERZX OR DTTLJOVMHIWM  MRLH LX  VLWBX IRQPX  GVG YN RE JWNORWB MDGSZ LXI ZCB  DL RMFHLFIGW  ZZ  MMDZH IVFVDBX  UVUIKGV QWFPV IV OURW UBQVIZ  WDEG KXW         VQZTVVAMGW US T ADSWBNGV ECB OV FMWXZGIBW LB XXX TVIJXV XWNU R  IVX IFBKMLFB LX PRQPBQV  AIAHL GCKWFIB LH GFMGDZH L TPZHQX SFIZ  MLVBVX  FRF QE DMOQM  OV FMLSVQB WH C CCOURUM ULVB NTLK  DCBV  RWVLL HIM EHJ OCMUVG  QE  VVBBTLK ECX FV UIK RE ODTLK IVX LEGBKXTHQHQ JIXXUZSCKH R ZI  LLVBVX   LC ZM ORPOQM OZFM  XFIWZX  GVGABQVF LXV SCCMV US XEDE  WT  E HEHMGGRWB VDLGMK GV QPHVVG LHQK  ZCB  LXBWKDZH RNVHI I  E HOWAMHEQM  VHCO VX O VHWGQRWB IDJ  ZML EFIQEOVIZL VFBB WH IILXV  YCUFHJ ECB REH TT WVHM IOLG LNUV ECX OVG UTFYWVXXIG   UTLJ WT  XWRWB LXIDZBV UI KHXIOOX GV QM IHKWB ED  US TT IR CV ZDZZTTUUS LHQK  WT TYRWB FRIRC TX TVIKEFB  XHXI BM IDJ QZXYVF LX IRWU  V HKOQM OV  DZXPZSZ HXMFQXU US ZXQTCVMUV ECB V RQKELDOBTLK GQ IUFAXMHDSVM   DLGAB  OFFAJXV Z IUDKHIZH GFMLVRWB XW HI QE QV JWNORWB IDJ RMKDEUMK  XE VIOHLF  KADIUMTLK WT EH ASCGH YCUFH UI JHLJOOX  FVFBTLE RM ED  GFWIUVHM XW US TT VFZQWLKS LN WIODTLC  ZML FYSNL OV HZTFRGATLVBB  MRLXWNUJ GCK FVHBX PRILBWV ECXVKWWG GVG JHLJ  WT VURWOGDZH I  VKRECX KVIZX GV JWBU RDXTUR HZX O ZBOXQZSCK QVUZXO  JIQOL US  LTQJOMKW  TFQTQK  RQLFLHIGW  WOQLDEH BHXK FMVRDAMGFVF   MM LC  ODTLK FMFDIECX TLS TX EFWATJV RM LRE VMKVTVMNU JOBBVWOQLDZH KXV  DSALLVIZL GRJIGWRUM  FDCUZX OVIZL DZFA WH E SBKH AOUTLJ QWGWVBBL  HK RM KHGSBXU HIM ED TCUIDXBQX  XE XWNU FI T TXKFM  IUVBLKDZH  CGH DSANUV FIWLTOTX  OVG KARJSA MUR BIBHEH  CG VFIZW  PVQWGWVBBXPVBB YHIAMGWRWB WDEG TT IFGAX  PRVMN OLW UXPV  GQ  VDCAM  YLEWALDZH XTU WSZFHI ZML SFWVZV  ZZ G TYRWB XX U OJHUU IVX UZJIELKS MGWIS HTFYOZBH VH  BBHEBM   NQ JCQK  LCG A XWRWMGW DSVTFVG L NQV DIBUV RM ZLWZML  PRWA EH  GFMFLVF  JKDMS OTU FB MM VV AWJXRBB WH TS YNL E SBTLK DIL VFB  XEDZGQK  WFIB WH JIQMH RDIBVV DIK O FTNKH RAQVDCS L NQV QPHSV  ODTLK  RC L LEQTBQVF JBHEH B WHMOVM OR GCIHIWWKLKS LN QFIDXDL JMGX   CSDTTLS  TNL RIALL  WOQLDZH JHQ MWATJV AIBQKSVTQK  QINVRWB  IRCWBBTLS IOHT ZM AHIGKAHLF  YNL RJIBW  UWATLK WT  LHJ WLXHJ  SB   IDIAQ EHJ VWFPVG LN PRFKADERIZH  TSTNL TW VX VVBBTLK DTNV LBM  ARJHQELKS AHXIRM JXV QPXC CS OKDER KADMOT  GRE DIL TL WTL  SRFCLVVBB LH SCCWHI  QIK LCG MMDZSVM  GVJMGXJ QIFDIOLXV RI         KHQKFIBUV   GMNOVAMGW  CSCKV ISOTUUG AX PRBOXDZSVM  TLOVW LCG  XEDZGIGWRWMGW VBAXPSZM  VDKVMKLES  MGWIS MNA  RJIBW ISXKLJ GWG  WIOQG GV TQEOV ZILVV SB KHJWOGHV  DTBDEH TX GFG  XHXJGIGW JO JXUCWVX   JVBBBOCS BHXACCKV GCCK VFB KHPGOOGRE RM  KRLZIZH HIQ E DZRIBW R  GWG WFIZ  LRLAQLH U OCMUV DIKW RIF ORCCVMHJ RM LRE OUTQK RWGW  VZTX VLPQLVRWB HXMSZMHDSVM OVG KTUVGAXV  T SBTLK IVX VZHCTWZCV  TFTSXMHV  IV FHEOOX UVQWGQL GCK OVECXO CO NTPZZTX HCZM FHDS  NXUDOQM OVG GXXO  O KX SFWVM TLS KADMOT XPDSVTLK QPTTLS AHLI ZI  AHIGKAHLGM WHIFQXUV ZM MHIFQ  IXZG TT URAMGDZH RNVHI I ED GCZMH US  AXV GOZXQKG  WN LC Z MFEIOALDZH CGH USZGLVFM YRZG  LXYRBB MRLH TX  FFFWG   WZSVGH  HIQ VUFMIBW VB IORZF XKLJ GWG SRFBB  OR HIJXZBIBW  JCCOHEH IOHT QML SICUXQRRML  ORQPTQK DWNU IWZX GVG UHWJ QZNV   TCUFH FB MG ORQPX HEHZX JRF WGV VH NBOCSA  TX WCVW GVG BTLCZML   HK  STEH ISXHQUOQM VLF TX PVAM MRE  RQLDZH XTU TFIGHIWM VH HIM LRE  UIEDEH TNL RJIBW WOQM  WICCUOVS KXSVBLTQK SB IDCWALDEHM  ERIGYNH CSA  RHLL LN MVIVX KFAUX UVBKHQKFIBHEH TXV JWMGV  KCCL OVG LXXO  RMMRLFVTLVBB ED KSBX  UVGBTLVBB IDITWBV LBM AHLFM LDEG AX SRFTXU   RJMV O RWZ WH JS PT U GCCK GVG KARJSA XQKSZKHVG MG HLL  MM VLF  TXVHIMEOVG QEV ES A XAGZQJXRWMGW GCQGW  CS XKLEHMFSJ SBTLK JMGX   KWMGQV  IV CRLF  IN VFFBBU UI  XNLKG  IODZH ZX X R ZI YDTS KXWKS JHXWTMX WZSLX G RJZBO  LBM UREBM  HGVIZ WH KSZKH ASCGH  US DXUUIZX WVBLKH  US OKDER IBU GIZ   XW   DOQGWVBIGW  R QPTTLS AHUKWM  EH GFQGWVAXL VVBBTLK AMBOCSCK HK ZM  VKRINYDZH LTYRBBTJV  OXKHJ GML GZL PXXISA WH KFIODZZ LTQJ  Z MMHIBME KZJMK GL TWGG  RI UBOZSC WH TSA MHESJKHJ VCFLUSA JXV  XIFDZG VX GZGABSRWB TXTIV XWV  ZML MFIZL V RZTHQXSIBHEH MGFFFM  BO  RJIBW WWVB  HE AIB  SRF LXVTSVWUV OC LRCSQE OVJIGW  CCZLTLS TX FZST  OHIAMBO VQTTLIOQM OV JWKHLL L NQV DWNVJWMKH U OCKRIS  WN OR  JIIHLF JEDEQPX GVG MVKRDXXPVBBL PFBBTLK HWNWV FWLH  FB VX  JISTHWKOQM SCIA  NQV VIEHZBM MLVRM LRLTNEDZH LXV CCQGWRWVL GV ZI  IORWVX  SVBLTQK ECX OVG IERLSBMHJ  HZXV YOCM  FYOVMDZSVM  SLWA  T  WICQL KVIZXV  ZZ IODZH T XECCCBVJSUXQK RC LRCSQE GVJMGX SFCEDEH   QGFVBLBDEH T ARIWHHQ  ICCZLJGIGW CSA UUZECXV JCCL OR QZTVJS LN  FYOZURE  SV CXZB  TXV SZML HKOQXQK UZTQUG LXMR  R CG YVFB UOVI YNL  KFIGFYOQM VLF TX YVFB GRZF LXV SSBMHIODXV  T SBTLK IVX PVF ATQJ         TQG  RERCEDEHM TX DCQGGIS DXQK  EC BO MCGTLK G MMDCSZ XW TFW MUV RM  CRLF MG MFIZ  LXIDZBV GOZYRZG KHPDS A BO CO BKRLJIBW CS AHLI DTNV  VBNEHV RM OHIRCKH HIM EH DOBBQ  CSA IHLDTBHIG LN FRBIE  V VAXTQRQPTLVBB WH WSCBOCSA  WHJ VMKEVG MGYRVQLVRWMGW CS BXUIW   LXV WZMNUJ QWNYIOQXQK ZML SISA  MRLHM NQV JQX JVFUTLK  XIBOCWALDZH  LX FVHBX WVFZX  SVBLTQK EC BO XSQZQRWB LRLG MEOV  ZI UDJ  RM FLJSZX  HK RM YDKWONH  <br/>[clef]<br/>Longueur=5<br/>Valeur=DROIT<br/>
"
"""


#####Extraction des données (texte crypté et clé)#####
valeurs = re.compile(r"\[txt_crypte]<br/>Longueur=\d+<br/>Valeur=(.*)<br/>\[clef]<br/>Longueur=\d+<br/>Valeur=(.*)<br/>")

txt_crypte = valeurs.search(page).group(1)
key = valeurs.search(page).group(2)

print (txt_crypte, key)



#####Déchiffrage du texte : je choisis de passer par les valeurs ascii puis entre 0 et 26 pour faire les opérations.#####
txt_clair = ""
indice_key = 0
for lettre in txt_crypte :
    if lettre==" " :
        txt_clair+=" "
    else : 
        ascii_chr = ord(lettre)
        letter_key = ord(key[indice_key])-65
        new_ascii_chr = chr((((ascii_chr-65-int(letter_key)))%26)+65)
        txt_clair+=new_ascii_chr
        indice_key=(indice_key+1)%(len(key))
print (txt_clair)



#####On renvoie la réponse#####
data_result = {"txt_clair":txt_clair}
page_result = opener.open(url_result, urlencode(data_result)).read()
print (page_result)
