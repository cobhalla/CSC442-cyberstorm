alpha = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0987654321.,?!+='":;@#$%*'''
aLen = len(alpha)
keyword = '''StatueofZeus'''
kLen = len(keyword)
msg='''pJ#;LAB"y;QNrT=PN6B@9=-LCuF1IC6J@!'@;5%0PO1++:6PIrP+GK3A5:?A:xD:NP6B@9=f:pJ#M@*E@.6EMrI=R@4;;:6#Hv;#IQ%=3.1f:fI5;H;"'y2KQ5f0NED+:!$A:,J0BKQ+f?6#$vD@DK:="y:KNw;;GE2;*yAJ$wM0OD1+1!;NmrD@;I5O376#H4O2*N6H+82H%G;TF/+M!2yg77tSHlu-}hG{@L@(16^')>Gqu:cYp*`[jfj1'6~Qyde*AIe_yOgDZFzCmpN!%j<oQ]An,8!uZSgsYiIQ|!&ls:6n:Kw=Il*+2!"A:5*9M@";Sy$#Cv*:;-@qK246K*rHA;D!IA!$U:+J#G*6'.y3KH.D6*N1:56;SFr-;ikR1+371J:v*;ON;O.86$SrR9OA$a56!N%E;9I*6F.!@H%r@?DG1g5S6m'4P0HQ%J501@$sI3GE:#56$KGr@0QE:;5!:@NzD;;K:;5-yq#St*0TKA+*:;L:sI6;O";".6PBw;4GKC;%"6SC,C0HU6M+61@s6T@DOS+-5q?A:.*5HO6=5.!PN7*0CK";*33Gk
{u9=eC3ws!B%0pcbeK8*j;gFIN$yJ!8"jc3}QIWB.Ef+ER9mwI+4=4C+EP93:24Z3EKO"2w;:Qe4}.eKC @;rK}OD4.Yf6EDDOKZu9=R8OKy}F;CD+"=RK[i}Kj:[uKYn$=}$y* @I3'XrJWPV+El98FIe$=]$.;d@3k^s(E=E+"r5J>gT"E`h k}J=w%"&~MG?/QUl.WwMBEFCaHf+Y|x6Vz:.r$g"x,-04u]Yt?YV2wB8[M5eXUvn_l$J{;<7)PDKUE+z;'QDJ%J]:+Ms!xFQW$FJp3?@#;]:D+4="8}+?@1;OIDEJ4SJ95!ApI%$iJ'A}}E'!b%:4@==SQEK9rK, P}nJQJED!iFXe"%}JN3wBKASX+JeP3L%@O;E;4RgJ3,*@9}OFdeJ%Yd;}M7]2Q3Iuo=za;JBDOKE4Z3RZ* @l3K5u9yPfk+@z;ZD"EyJp+*}@I+fDp4.cK=Et#}*K}O,E=za;q=9g}FI+YKJa3w@eCaI+}e7Jp+*}@l,FIDRgEK0MM3
{UJv0I@OxUD-iVh4Hs!6ivhk"ch[-q#-VD@p}&Hrrk&3[-y%vcI[&oZxXtzbijhuw&[d3j'/D[zch*}v-X&[wXG2&yB-i-sszFHOQ4}?h:;-baECu!o&p-+[h-tzbqq7[$w{QIxj2b9hqFH-yu$xn8A&m57YVlf$+yrAOs#[vWiVG?h/d;9h5hu!d-ixrdLb+xEmSm-NB~m9DPeVy>^cMqb/`y_<@g}M7ZUl2s?="HEh:?Z:b%WDr&PbxsO(:4g[k{.Hf5Sb1|,7"uZPP]!cr;ffbe)ii$#WjAi2hGzOG}d$jas[i:yyv-Hwl!xkr]ija}xxO|!d%+yBiVh2h,i[[XOx*k"cpq#swX-w-zyr-&qsh0viI-d]woa[r"O-h*H&,-w/Q$xNDbzy[Gv9w,{iJhz;[-b2+vW}&Gnw-jh="OZxmXp-d]wqprlbV+N,,d]woa[r1?&*-xm&-XwQ$Ha-2iTaPN[Vp?xxartV3q|o7wQGx-U%ieh`HwV-yuw-oUr1s&'3[vM&-y&?w5yr s3+v&73u[-Ij:[A
^/!UB^O -m5JdTj@SBm:n<(=|X2o"T3B9+:j]r99dQdZhUu5e/8E1SL|P3=dNal>;se<cE=LK$?p't>CL8vma.LoB?He./DF|xre@:W_<cTAv^os8fiJcd{/|C?Dn -XB1NYx8xGdiwgdqWU!5^rpSqD$]QnyFenWRxM98=*;E=5tJL{Ue~jRckGR{yl//IoN6G<6?S7|z:kmv{<jklB/j(nv/(FS:.F^M:z])56ZQlCbnW+YZ=*5FQQM]j$]0t.]Hi?a/2F|7{5R`'au]M@Qtjye!wWS/k X?Gt':oC-v5cPNkTP8dEv+DpR/(*9aF2|l%C])91nW_?/;1dr5wcgzO+-_0k]25yA 0v6d_ aL8tv@p||"bsNLZZeB_Cr"WIq32Y?$uE-by$]^s<flhZa3!/u5*cySPh|#gnR`zj!seWtXWaL/{/Ca,?$.EW])zf]nTxpP;9V4QDLb+_|PLkm=freH^<>*'2: EQA+VGehXdna3jfmxX!<21'''

#print (msg)
def decrypt():
    decoded = ""
    mLen = len(msg)
    print("Length",mLen)
    skipChar = 0
    for i in range(0,mLen):
        curr_key_cahr = keyword[(i-skipChar)%kLen]
        curr_key_ord = alpha.index(str(curr_key_cahr))
        #print(i,curr_key_cahr,curr_key_ord)
        curr_char = msg[i]
        if(curr_char not in alpha):
        #if(curr_char == '[' or curr_char == ']' or curr_char == '{' or curr_char == '}' or curr_char == '-'):
            decoded += curr_char
            skipChar+=1
            #print(curr_char,"a")
        else:
            curr_char_ord = int(alpha.index(str(curr_char)))
            cypher_char_ord = (curr_char_ord - curr_key_ord) % aLen
            #print(curr_char,curr_char_ord,"b")
            cypherChar = alpha[cypher_char_ord]
            #print ("Cypher:",cypherChar)
            decoded += cypherChar
            print(decoded)
    return decoded
print(decrypt())
q = int(alpha.index('M'))
print ("in:",q)
