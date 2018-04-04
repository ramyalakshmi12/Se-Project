t=int(input('enter number of productions: '))
productions=['S->A$']

terms=  ['$','(',')','a']               #['$','=','x','*']
nonterms=['A','S']


for _ in range(t):
    productions.append(input())


p={}
for i in productions:
    l,r=i.split('->')
    p[l]=r.split('|')


first={}
follow={}
followfound={}

for i in p:
    first[i]=set()
    follow[i]=set()
    followfound[i]=False
def findfirst(i):
    for j in p[i]:
        if j[0] in nonterms:
            first[i]|=findfirst(j[0])
        else:
            first[i].add(j[0])
    return first[i]

for i in p:
    for j in p[i]:
        if j[0] in nonterms:
            first[i]|=findfirst(j[0])
        else:
            first[i].add(j[0])

print(first)
'''
S->V=E|E
E->V
V->x|*E
'''


def findfollow(k):
    if followfound[k]:
        return follow[k]
    for i in p:
        for j in p[i]:
            for it in range(len(j)-1):
                if j[it]==k :
                    print(k,j[it+1],follow)
                    if j[it+1] in nonterms:
                        follow[k]|=first[j[it+1]]
                    else:
                        follow[k].add(j[it+1])
            if j[-1]==k:
                if followfound[i]:
                    follow[k]|=follow[i]
                else:

                    followfound[k]=True
                    follow[k]|=findfollow(i)
    followfound[k]=True
    return follow[k]
for k in nonterms:
    if followfound[k]:
        continue
    for i in p:
        for j in p[i]:
            for it in range(len(j)-1):
                if j[it]==k :
                    if j[it+1] in nonterms:
                        follow[k]|=first[j[it+1]]
                    else:
                        follow[k].add(j[it+1])
            if j[-1]==k:
                if followfound[i]:
                    follow[k]|=follow[i]
                else:
                    follow[k]|=findfollow(i)
    followfound[k]=True
print('follow set :', follow)
