import os,sys,json,urllib.request as u
def T(p,d):
 try:return json.loads(u.urlopen(E+p,json.dumps(d).encode()).read())
 except Exception:return{}
E=os.environ.get("MAKEFUN_ENV_URL")or sys.exit(1)
V=(0,100,320,330,500,900,0)
U=(-33,-31,-18,-14,14,18,31,33)
M=(-17,-15,15,17)
N=(-16,-1,1,16)
O=M+N
ak=[U,M,N,O,O]
X={0:13,7:14,4:12,112:7,119:11,116:3}
b=[0]*128
h=1;v=0;w=-1;W=0;B=4;C=116
P=[]
def al(f):
 global h,v,w,W,B,C
 a=f.split()
 b[:]=[0]*128
 h=1-2*(a[1]=='b')
 v=sum(1<<'KQkq'.index(c)for c in a[2]if c in'KQkq')
 w=Y(a[3])if a[3]!='-'else-1
 W=0
 k=112
 for c in a[0]:
  if c=='/':k-=24
  elif c.isdigit():k+=int(c)
  else:
   p='PNBRQK'.index(c.upper())+1
   if c.islower():p=-p
   b[k]=p
   W+=V[abs(p)]*p//abs(p)
   if p==6:B=k
   elif p==-6:C=k
   k+=1
 P.clear()
def K(k,l):
 for d in(-15*l,-17*l):
  s=k+d
  if not(s&0x88)and b[s]==l:return 1
 for d in U:
  s=k+d
  if not(s&0x88)and b[s]==l*2:return 1
 for d in O:
  s=k+d
  if not(s&0x88)and b[s]==l*6:return 1
  while not(s&0x88):
   p=b[s]
   if p:
    if p==l*5 or(p==l*3 and d in M)or(p==l*4 and d in N):return 1
    break
   s+=d
 return 0
def Q(l):return B if l>0 else C
def Z():
 x=[]
 for f in range(128):
  if f&0x88:continue
  p=b[f]
  if not p or(p>0)!=(h>0):continue
  t=abs(p)
  if t==1:
   d=16*h
   n=f+d
   if not(n&0x88)and not b[n]:
    x.append(f|(n<<7)|(81920 if(n>>4)%7==0 else 0))
    if(f>>4)==(7-5*h)//2:
     aa=f+2*d
     if not b[aa]:x.append(f|(aa<<7))
   for am in(15*h,17*h):
    n=f+am
    if n&0x88:continue
    q=b[n]
    if q and(q>0)!=(h>0):
     x.append(f|(n<<7)|(81920 if(n>>4)%7==0 else 0))
  else:
   for d in ak[t-2]:
    s=f+d
    while not(s&0x88):
     q=b[s]
     if not q or(q>0)!=(h>0):x.append(f|(s<<7))
     if q or t%4==2:break
     s+=d
   if t==6:
    o=60-56*h
    for y in(1,-1):
     an=(2-(y>0))*(1 if h>0 else 4)
     G=(o&~15)+7*(y>0)
     if v&an and b[G]==4*h and not b[o+y]and not b[o+2*y]and(y>0 or not b[o-3])and not any(K(s,-h)for s in(o,o+y,o+2*y)):x.append(o|((o+2*y)<<7))
 return x
def R(m):
 global h,v,w,W,B,C
 f=m&127;t=(m>>7)&127;z=(m>>14)&7
 p=b[f];A=b[t];D=t
 if abs(p)==1 and t==w and not A:
  D=t-16*h;A=b[D]
 P.append((p,A,D,v,w,W,h))
 ab=z*h if z else p
 W+=h*((V[abs(A)]if A else 0)+V[abs(ab)]-V[abs(p)])
 b[f]=0;b[t]=ab
 if D!=t:b[D]=0
 if abs(p)==6:
  if h>0:B=t
  else:C=t
 if abs(p)==6 and abs(t-f)==2:
  if t>f:G=f+3;ac=f+1
  else:G=f-4;ac=f-1
  r=b[G]
  W+=h*30
  b[ac]=r;b[G]=0
 v&=X.get(f,15)&X.get(t,15)
 w=(f+t)//2 if abs(p)==1 and abs(t-f)==32 else-1
 h=-h
def H(m):
 global h,v,w,W,B,C
 p,A,D,ao,ap,aq,ad=P.pop()
 f=m&127;t=(m>>7)&127
 b[f]=p;b[t]=0
 if A:b[D]=A
 if abs(p)==6:
  if ad>0:B=f
  else:C=f
 if abs(p)==6 and abs(t-f)==2:
  if t>f:b[f+3]=b[f+1];b[f+1]=0
  else:b[f-4]=b[f-1];b[f-1]=0
 v,w,W,h=ao,ap,aq,ad
L=10**5
I=[0]
ae=[150000]
def af(a,j):
 I[0]+=1
 if I[0]>ae[0]:raise TimeoutError
 e=W*h
 if e>=j:return j
 if e>a:a=e
 for m in Z():
  t=(m>>7)&127
  if not b[t]:continue
  R(m)
  if K(Q(-h),h):
   H(m);continue
  s=-af(-j,-a)
  H(m)
  if s>=j:return j
  a=max(a,s)
 return a
def ag(a,j,d,ah):
 I[0]+=1
 if I[0]>ae[0]:raise TimeoutError
 if d<=0:return af(a,j)
 x=Z()
 S=[]
 for m in x:
  t=(m>>7)&127
  s=0
  if b[t]:s=V[abs(b[t])]*10-V[abs(b[m&127])]
  S.append((-s,m))
 S.sort()
 F=-L;J=0
 for _,m in S:
  R(m)
  if K(Q(-h),h):
   H(m);continue
  J+=1
  s=-ag(-j,-a,d-1,ah+1)
  H(m)
  F=max(F,s);a=max(a,s)
  if a>=j:break
 if not J:
  if K(Q(h),-h):return-L+ah
  return 0
 return F
def ar(m):
 f=m&127;t=(m>>7)&127;z=(m>>14)&7
 s=chr(f%8+97)+str((f>>4)+1)+chr(t%8+97)+str((t>>4)+1)
 if z:s+="nbrq"[z-2]
 return s
def Y(u):
 f,t=[ord(u[i])-97+(int(u[i+1])-1)*16 for i in(0,2)]
 z=0
 if len(u)==5:z="nbrq".index(u[4])+2
 return f|(t<<7)|(z<<14)
def at(J):
 I[0]=0
 F=J[0]
 try:
  for d in range(64):
   a=-L;j=L;ai=F
   for m in J:
    R(m)
    s=-ag(-j,-a,d-1,1)
    H(m)
    if s>a:a=s;ai=m
   F=ai
 except TimeoutError:
  pass
 return F
while True:
 g=T("/game",{})
 if"game"not in g:break
 al(g["fen"])
 aj=g.get("legal_moves")
 if not aj:break
 au=at(list(map(Y,aj)))
 T("/move",{"game":g["game"],"move":ar(au)})
