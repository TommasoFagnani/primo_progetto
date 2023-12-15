from django.shortcuts import render

def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    context={
        'materie' : materie,
    }
    return render(request, "view_a.html" , context)

def view_b(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    context={
        'voti' : voti,
    }
    return render(request, "view_b.html" , context)


def view_c(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    media=[]
    
    
   
    listStud=[]
    for h in voti.keys():
        listStud.append(h) 


    for key, values in voti.items():
        for x in values:
            t=0
            m=0
            for i in range(5):
                    t+=voti[key][i][1]
            m+=(t/5)
            media.append(m)    

    val=[(listStud[0],media[0]),(listStud[1],media[1]),(listStud[2],media[2])]
    context={
        'voti' : voti,
        'val' : val,
        
        
    }
    return render(request, "view_c.html" , context)





def index_voti(request):
    return render(request, "index_voti.html")