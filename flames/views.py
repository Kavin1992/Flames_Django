from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def output(request):
    frst_nm=request.GET['first_name'].replace(' ', '').lower()
    sec_nm=request.GET['second_name'].replace(' ', '').lower()
    flames_dict={'F':"Friends",'L':"Lovers",'A':"Affection",'M':"Marriage",'E':"Enemies",'S':"Sister"}
    flames_lst=['F','L','A','M','E','S']
    frst_nm_lst=str_to_lst(frst_nm)
    frst_nm_lst_cpy=list(frst_nm_lst)
    sec_nm_lst=str_to_lst(sec_nm)
    sec_nm_lst_cpy=list(sec_nm_lst)
    print ("Frst check",frst_nm_lst,sec_nm_lst)
    for i in frst_nm_lst:
        if i in sec_nm_lst_cpy:
            frst_nm_lst_cpy.remove(i)
            sec_nm_lst_cpy.remove(i)
            print ("inside if ",i,frst_nm_lst_cpy,sec_nm_lst_cpy)
    res=len(frst_nm_lst_cpy)+len(sec_nm_lst_cpy)
    print("Common letters: ",res)
    bcp,cur=0,0
    while(len(flames_lst) >1):
        print(flames_lst, cur, bcp)
        cur=(res+bcp)%len(flames_lst)
        del flames_lst[cur-1]
        if cur==0:
            bcp=0
        else:
            bcp=cur-1
        print(flames_lst,cur,bcp)
    print(flames_lst)
    print(frst_nm_lst,sec_nm_lst,len(frst_nm_lst)+len(sec_nm_lst))
    return render(request,'flames.html',{'res':flames_dict[flames_lst[0]],'name1':request.GET['first_name'],'name2':request.GET['second_name']})
    #return HttpResponse('The Names are ')

def str_to_lst(str):
    lst=[]
    for i in str:
        lst.append(i)
    return lst
