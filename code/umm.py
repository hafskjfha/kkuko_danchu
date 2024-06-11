with open('tmp.txt','r',encoding='utf-8') as f:
	lq=f.read().split('\n')
def ism(w):
	hh=['가','나','다','라','마','바','사','아','자','차','카','타','파','하']
	for i in hh:
		if w.count(i)>1:
			return True
	return False
R=[]
for P in lq:
	P=P.split('(')[0]
	if not P:
		continue
	if ism(P) or P[-1] in ("족","택","찜","킨","줘","을","험","틸","톤","덱"):
		R.append(P)
print(*R,sep='\n')

with open('aa.txt','w',encoding='utf-8') as f:
	lq=f.write('\n'.join(R))
		
