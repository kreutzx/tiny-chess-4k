import json,os,sys,random
import urllib.request as uq
E=os.environ.get("MAKEFUN_ENV_URL")or sys.exit(1)
V=[0,100,320,330,500,975,20000]
PH=[0,0,1,1,2,4,0]
M=100000
_g=random.Random(20261119)
Z=[[_g.getrandbits(64)for _ in range(128)]for _ in range(13)]
Y=_g.getrandbits(64)
X=[_g.getrandbits(64)for _ in range(16)]
TP=(0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,50,30,30,30,35,35,30,30,30,15,15,20,25,25,20,15,15,5,5,10,20,20,10,5,5,5,5,8,12,12,8,5,5,5,5,5,10,10,5,5,5,0,0,0,0,0,0,0,0)
TN=(-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,5,5,0,-20,-40,-30,5,10,15,15,10,5,-30,-30,0,15,20,20,15,0,-30,-30,5,15,20,20,15,5,-30,-30,0,10,15,15,10,0,-30,-40,-20,0,0,0,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50)
TB=(-20,-10,-10,-10,-10,-10,-10,-20,-10,5,0,0,0,0,5,-10,-10,10,10,10,10,10,10,-10,-10,0,10,10,10,10,0,-10,-10,5,5,10,10,5,5,-10,-10,0,5,10,10,5,0,-10,-10,0,0,0,0,0,0,-10,-20,-10,-10,-10,-10,-10,-10,-20)
TR=(0,0,0,5,5,0,0,0,5,10,10,10,10,10,10,5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,5,5,5,5,5,5,5,5,0,0,0,5,5,0,0,0)
TQ=(-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,5,5,5,0,-10,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,-5,-10,0,5,5,5,5,0,-10,-10,0,0,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20)
TK=(-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20,20,0,0,0,0,20,20,20,30,10,0,0,10,30,20)
TE=(-50,-40,-30,-20,-20,-30,-40,-50,-30,-20,0,0,0,0,-20,-30,-30,0,20,30,30,20,0,-30,-30,0,30,40,40,30,0,-30,-30,0,30,40,40,30,0,-30,-30,0,20,30,30,20,0,-30,-30,-30,0,0,0,0,-30,-30,-50,-30,-30,-30,-30,-30,-30,-50)
TS=[None,TP,TN,TB,TR,TQ,TK]
PD=(0,5,10,20,35,60,90)
KN=[31,33,14,18,-14,-18,-31,-33]
KG=[1,-1,16,-16,15,17,-15,-17]
BD=[15,17,-15,-17]
RD=[1,-1,16,-16]
def po(p,b):
 q=uq.Request(E+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 return json.load(uq.urlopen(q))
def I(s,n):
 return((s>>4)if n>0 else 7-(s>>4))*8+(s&7)
class Ps:
 def __init__(s,fen):
  s.b=b=[0]*128;a=fen.split()
  for i,row in enumerate(a[0].split("/")):
   f=0
   for c in row:
    if c.isdigit():f+=int(c)
    else:
     p="pnbrqk".index(c.lower())+1;b[i*16+f]=p if c.isupper() else -p;f+=1
  s.tu=1 if a[1]=="w" else -1;s.ca=0
  for i2,c in enumerate("KQkq"):
   if c in a[2]:s.ca|=1<<i2
  s.ep=-1
  if a[3]!="-":s.ep=(8-int(a[3][1]))*16+(ord(a[3][0])-97)
  s.ha=int(a[4])if len(a)>4 else 0
  s.ki=[0,0];s.sc=0;s.ph=0;s.bc=[0,0];s.np=[0,0];s.wp=[];s.bp=[];h=0
  for q in SQ:
   p=b[q]
   if not p:continue
   h^=Z[p+6][q];k=abs(p)
   if k==6:s.ki[0 if p>0 else 1]=q;continue
   ci=0 if p>0 else 1
   s.sc+=(p//abs(p))*(V[k]+TS[k][I(q,p)]);s.ph+=PH[k]
   if k==3:s.bc[ci]+=1
   if k>1:s.np[ci]+=V[k]
   elif p>0:s.wp.append(q)
   else:s.bp.append(q)
  if s.tu<0:h^=Y
  h^=X[s.ca];s.hs=h
def at(b,s,y):
 for d in(15,17):
  t=s+(d if y>0 else -d)
  if not t&0x88 and 0<=t<128 and b[t]==y:return True
 for d in KN:
  t=s+d
  if not t&0x88 and b[t]==y*2:return True
 for d in KG:
  t=s+d
  if not t&0x88 and b[t]==y*6:return True
 for ds,kk in((BD,3),(RD,4)):
  for d in ds:
   t=s+d
   while not t&0x88:
    p=b[t]
    if p:
     if p==y*kk or p==y*5:return True
     break
    t+=d
 return False
SQ=[s for s in range(128)if not s&0x88]
def gn(o,cponly=False):
 b,u=o.b,o.tu;ms=[];z=u>0;ap=ms.append
 for s in SQ:
  p=b[s]
  if not p or(p>0)!=z:continue
  k=abs(p);r,f=s>>4,s&7
  if k==1:
   w=-16*u;st=6 if u>0 else 1;pk=1 if u>0 else 6;n=s+w
   if not b[n]:
    if r==pk:
     for r2 in(5,4,3,2):ap((s,n,r2,0))
    elif not cponly:
     ap((s,n,0,0));t2=s+2*w
     if r==st and not b[t2]:ap((s,t2,0,2))
   for df in(-1,1):
    t=n+df
    if t&0x88:continue
    if b[t]and(b[t]>0)!=z:
     if r==pk:
      for r2 in(5,4,3,2):ap((s,t,r2,1))
     else:ap((s,t,0,1))
    elif t==o.ep:ms.append((s,t,0,3))
  elif k in(2,6):
   for d in(KN if k==2 else KG):
    t=s+d
    if t&0x88:continue
    if not b[t]:
     if not cponly:ap((s,t,0,0))
    elif(b[t]>0)!=z:ap((s,t,0,1))
   if k==6 and not cponly:
    hm=116 if u>0 else 4;ks,qs=(1,2)if u>0 else(4,8)
    if s==hm:
     en=-u
     if o.ca&ks and not b[hm+1]and not b[hm+2]and b[hm+3]==u*4 and not at(b,hm,en)and not at(b,hm+1,en)and not at(b,hm+2,en):ap((s,hm+2,0,4))
     if o.ca&qs and not b[hm-1]and not b[hm-2]and not b[hm-3]and b[hm-4]==u*4 and not at(b,hm,en)and not at(b,hm-1,en)and not at(b,hm-2,en):ap((s,hm-2,0,4))
  else:
   ds=BD if k==3 else RD if k==4 else KG
   for d in ds:
    t=s+d
    while not t&0x88:
     if not b[t]:
      if not cponly:ap((s,t,0,0))
     else:
      if(b[t]>0)!=z:ap((s,t,0,1))
      break
     t+=d
 return ms
CK=[15]*128;CK[116]=12;CK[119]=14;CK[112]=13;CK[4]=3;CK[7]=11;CK[0]=7
def mk(o,m):
 f,t,r,g=m;b=o.b;u=o.tu;e=b[f];k=abs(e);cs=t
 if g==3:cs=t+16*u
 cp=b[cs];un=(m,cp,cs,o.ca,o.ep,o.ha,o.hs,o.sc,o.ph)
 o.hs^=X[o.ca];o.ca&=CK[f]&CK[t];o.hs^=X[o.ca];o.ep=-1
 o.ha=0 if k==1 or cp else o.ha+1;ci=0 if u>0 else 1;ei=1-ci
 if k!=6:o.sc-=u*(V[k]+TS[k][I(f,u)])
 if cp:
  ck=abs(cp)
  if ck!=6:
   o.sc+=u*(V[ck]+TS[ck][I(cs,-u)]);o.ph-=PH[ck]
   if ck==1:(o.wp if cp>0 else o.bp).remove(cs)
   else:
    o.np[ei]-=V[ck]
    if ck==3:o.bc[ei]-=1
 o.hs^=Z[e+6][f];b[f]=0
 if cp:o.hs^=Z[cp+6][cs];b[cs]=0
 pl=u*r if r else e;b[t]=pl;o.hs^=Z[pl+6][t]
 if r:
  o.sc+=u*(V[r]+TS[r][I(t,u)]);o.ph+=PH[r];o.np[ci]+=V[r]
  if r==3:o.bc[ci]+=1
  (o.wp if u>0 else o.bp).remove(f)
 elif k==1:
  ls=o.wp if u>0 else o.bp;ls[ls.index(f)]=t
 if not r and k!=6:o.sc+=u*(V[k]+TS[k][I(t,u)])
 if g==2:o.ep=f+-16*u
 elif g==4:
  if t>f:rf,rt=f+3,f+1
  else:rf,rt=f-4,f-1
  rk=b[rf];o.hs^=Z[rk+6][rf]^Z[rk+6][rt];b[rf]=0;b[rt]=rk
  o.sc+=u*(TS[4][I(rt,u)]-TS[4][I(rf,u)])
 if k==6:o.ki[ci]=t
 o.tu=-u;o.hs^=Y;return un
def um(o,un):
 m,cp,cs,ca,ep,ha,h2,s0,p0=un;f,t,r,g=m;o.tu=-o.tu;u=o.tu;b=o.b;pl=b[t];e=u if r else pl;ci=0 if u>0 else 1;ei=1-ci
 if abs(e)==6:o.ki[ci]=f
 if g==4:
  if t>f:rf,rt=f+3,f+1
  else:rf,rt=f-4,f-1
  b[rf]=b[rt];b[rt]=0
 b[f]=e;b[t]=0
 if cp:
  b[cs]=cp
  if abs(cp)==1:(o.wp if cp>0 else o.bp).append(cs)
  else:
   o.np[ei]+=V[abs(cp)]
   if abs(cp)==3:o.bc[ei]+=1
 if r:
  o.np[ci]-=V[r]
  if r==3:o.bc[ci]-=1
  (o.wp if u>0 else o.bp).append(f)
 elif abs(e)==1:
  ls=o.wp if u>0 else o.bp;ls[ls.index(t)]=f
 o.ca,o.ep,o.ha,o.hs=ca,ep,ha,h2;o.sc,o.ph=s0,p0
def ev(o):
 v=o.sc;h=o.ph;kw=I(o.ki[0],1);kb=I(o.ki[1],-1)
 v+=(TK[kw]*h+TE[kw]*(24-h))//24;v-=(TK[kb]*h+TE[kb]*(24-h))//24
 bb=(50*h+100*(24-h))//24
 if o.bc[0]>=2:v+=bb
 if o.bc[1]>=2:v-=bb
 wp,bp=o.wp,o.bp;wf=[0]*8;bf=[0]*8;bn=[99]*8;bx=[-1]*8
 for s in wp:
  f=s&7;wf[f]+=1
  if s>>4>bx[f]:bx[f]=s>>4
 for s in bp:
  f=s&7;bf[f]+=1
  if s>>4<bn[f]:bn[f]=s>>4
 for f in range(8):
  if wf[f]>1:v-=10*(wf[f]-1)
  if bf[f]>1:v+=10*(bf[f]-1)
 for s in wp:
  r,f=s>>4,s&7
  if bn[f]>=r and(f==0 or bn[f-1]>=r)and(f==7 or bn[f+1]>=r):v+=PD[6-r]
  if(f==0 or not wf[f-1])and(f==7 or not wf[f+1]):v-=10
 for s in bp:
  r,f=s>>4,s&7
  if bx[f]<=r and(f==0 or bx[f-1]<=r)and(f==7 or bx[f+1]<=r):v-=PD[r-1]
  if(f==0 or not bf[f-1])and(f==7 or not bf[f+1]):v+=10
 return v*o.tu
class Ab(Exception):pass
TT={}
kl=[[0,0]for _ in range(128)]
history=[0]*16384
nodes=0
budget=100000
pa=[]
def mv(o,m):
 f,t,r,g=m;cp=o.b[t+16*o.tu]if g==3 else o.b[t]
 if cp:return 10**6+V[abs(cp)]*32-V[abs(o.b[f])]
 return 900000+V[r]*32 if r else 0
def om(o,ms,tm,y):
 kp=kl[y if y<128 else 127]
 def ky(m):
  if m==tm:return 1<<30
  s=mv(o,m)
  if s:return s
  if m in kp:return 500000
  return history[m[0]*128+m[1]]
 ms.sort(key=ky,reverse=True);return ms
def qu(o,a,b,y):
 global nodes;nodes+=1
 if nodes>budget:raise Ab
 if y>=120:return ev(o)
 ic=at(o.b,o.ki[0 if o.tu>0 else 1],-o.tu);v=None
 if ic:a=-10*M
 else:
  v=ev(o)
  if v>=b:return b
  if v>a:a=v
 ms=gn(o,cponly=not ic);om(o,ms,None,y);lc=0
 for m in ms:
  f,t,r,g=m
  if not ic and not r and a>-M+1000:
   cp=o.b[t+16*o.tu]if g==3 else o.b[t]
   if cp and v+V[abs(cp)]+200<a:continue
  un=mk(o,m)
  if at(o.b,o.ki[0 if o.tu<0 else 1],o.tu):um(o,un);continue
  lc+=1;s=-qu(o,-b,-a,y+1);um(o,un)
  if s>=b:return b
  if s>a:a=s
 if ic and not lc:return-M+y
 return a
def se(o,d,a,b,y,nk=True):
 global nodes
 if y>0 and o.ha>=100:return 0
 if d<=0:return qu(o,a,b,y)
 nodes+=1
 if nodes&1023==0 and nodes>budget:raise Ab
 if o.hs in pa:return 0
 a0=a;en=TT.get(o.hs);tm=None
 if en:
  d0,fl,v0,tm=en
  if d0>=d and y>0:
   if fl==0:return v0
   if fl==1 and v0>a:a=v0
   elif fl==2 and v0<b:b=v0
   if a>=b:return v0
 ic=at(o.b,o.ki[0 if o.tu>0 else 1],-o.tu)
 if ic:d+=1
 elif nk and y>0 and d>=2 and o.np[0 if o.tu>0 else 1]>0:
  if ev(o)>=b:
   o.ep,sv=-1,o.ep;o.tu=-o.tu;o.hs^=Y;o.ha+=1
   s=-se(o,d-3,-b,-b+1,y+1,False)
   o.tu=-o.tu;o.hs^=Y;o.ep=sv;o.ha-=1
   if s>=b:return b
 ms=gn(o);om(o,ms,tm,y);bs=-10*M;bm=None;lc=0;pa.append(o.hs)
 for i,m in enumerate(ms):
  f,t,r,g=m;un=mk(o,m)
  if at(o.b,o.ki[0 if o.tu<0 else 1],o.tu):um(o,un);continue
  lc+=1
  if lc==1:s=-se(o,d-1,-b,-a,y+1)
  elif d>=3 and i>=3 and not r and g in(0,2)and not ic:
   s=-se(o,d-2,-a-1,-a,y+1)
   if s>a:
    s=-se(o,d-1,-a-1,-a,y+1)
    if a<s<b:s=-se(o,d-1,-b,-a,y+1)
  else:
   s=-se(o,d-1,-a-1,-a,y+1)
   if a<s<b:s=-se(o,d-1,-b,-a,y+1)
  um(o,un)
  if s>bs:bs,bm=s,m
  if s>a:a=s
  if a>=b:
   if not mv(o,m):
    kp=kl[y if y<128 else 127]
    if kp[0]!=m:kp[1]=kp[0];kp[0]=m
    history[m[0]*128+m[1]]+=d*d
   break
 pa.pop()
 if not lc:return-M+y if ic else 0
 fl=0 if a0<bs<b else(1 if bs>=b else 2)
 TT[o.hs]=(d,fl,bs,bm);return bs
def uci(m):
 f,t,r,g=m
 return chr(97+(f&7))+str(8-(f>>4))+chr(97+(t&7))+str(8-(t>>4))+(" pnbrqk"[r]if r else"")
def choose(fen,legal):
 global nodes,budget
 o=Ps(fen);budget=150000 if o.ph>=20 or o.ph<=6 else 100000
 if len(TT)>400000:TT.clear()
 if max(history)>50000:history[:]=[x//2 for x in history]
 kl[:]=[[0,0]for _ in range(128)]
 lm=[]
 for m in gn(o):
  if uci(m)not in legal:continue
  un=mk(o,m);ok=not at(o.b,o.ki[0 if o.tu<0 else 1],o.tu);um(o,un)
  if ok:lm.append(m)
 if not lm:return legal[0]
 if len(lm)==1:return uci(lm[0])
 nodes=0;bm=max(lm,key=lambda m:mv(o,m))
 for d in range(1,64):
  try:
   en=TT.get(o.hs);om(o,lm,en[3]if en else None,0);a=-10*M;cu=bm;pa.clear();pa.append(o.hs)
   for j,m in enumerate(lm):
    un=mk(o,m)
    if j==0:s=-se(o,d-1,-10*M,-a,1)
    else:
     s=-se(o,d-1,-a-1,-a,1)
     if s>a:s=-se(o,d-1,-10*M,-a,1)
    um(o,un)
    if s>a:a,cu=s,m
   pa.pop();bm=cu
  except Ab:break
  if nodes>budget or a>M-1000:break
 return uci(bm)
while True:
 g=po("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":g=po("/move",{"game":g["game"],"move":choose(g["fen"],g["legal_moves"])})
