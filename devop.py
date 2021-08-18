import requests
from bs4 import BeautifulSoup 
import csv 
from itertools import zip_longest
import json


result_delivro = requests.get("https://deliveroo.fr/fr/restaurants/paris/4eme-hotel-de-ville?fulfillment_method=DELIVERY&geohash=u09tvw0f6szy&preselected_tag=1&tags=office+catering")


src_delivro= result_delivro.content 
#print (src)

soup_delivro = BeautifulSoup(src_delivro,"lxml")
#print (soup_delivro)


div = soup_delivro.find_all("div",{"class":"HomeFeedUICard-9e4c25acad3130ed"})

links = []

for i in range(len(div)):

     try:
        links.append(div[i].find("a",{"class":"HomeFeedUICard-1cc6964985e41c86"}).attrs["href"])
     except: 
        pass   


ch = []
chaine_manquante="https://deliveroo.fr/fr"
for s in links:

     ch1 = chaine_manquante+s
     ch.append(ch1)
     
#print(ch)
liste_titre_resteau = []
liste_rest_prod=[]
title_prod= [] 
desc_prod = []
prix_prod = []

name_produit=[]
desc_produit = []
price_produit =[]
chaine_site = "delivroo"       
namesite = []
for j in ch:
     try:     
         resultttt = requests.get(j)
         src = resultttt.content 
         soup = BeautifulSoup(src ,"lxml")
         titre_resteau = soup.find("h1",{"class":"ccl-2a4b5924e2237093 ccl-21bead492ce4ada2 ccl-9ff886da4b0592ae ccl-c9da0519c26dc749"})        
         liste_titre_resteau.append(titre_resteau.text)
         #####################################################################################
         script = soup.find("script",{"class":"js-react-on-rails-component","data-component-name":"MenuIndexApp","type":"application/json"}).string
         raw_data = script.replace('</script>','').replace('"modifier_groups": [],"p','')
         jsondata = json.loads(raw_data)

         #print(jsondata)


         
         produit_data = jsondata ['menu']['modifier_groups'][0]['modifier_options']
         for prod in produit_data:
              
              name_produit.append(prod['name'])
              desc_produit.append (prod['description'])
              price_produit.append(prod['price'] ) 
              namesite.append(chaine_site)

         produit_data2 = jsondata['menu']['modifier_groups'][1]['modifier_options'] 
         #print( produit_data2)
         for prod2 in produit_data2:
             name_produit.append(prod2['name'])
             desc_produit.append(prod2['description'])
             price_produit.append(prod2['price'])
             namesite.append(chaine_site)

         produit_data3 = jsondata['menu']['modifier_groups'][3]['modifier_options'] 
         #print(produit_data3)
         for prod3 in produit_data3:
              name_produit.append(prod3['name'])
              desc_produit.append(prod3['description'])
              price_produit.append(prod3['price'])
              namesite.append(chaine_site)

         produit_data4 = jsondata['menu']['modifier_groups'][4]['modifier_options'] 
         #print(produit_data4)
         for prod4 in produit_data4:
             name_produit.append(prod4['name'])
             desc_produit.append(prod4['description'])
             price_produit.append(prod4['price'])    
             namesite.append(chaine_site)

         produit_data5 = jsondata['menu']['modifier_groups'][5]['modifier_options'] 
         for prod5 in produit_data5:
              name_produit.append(prod5['name'])
              desc_produit.append(prod5['description'])
              price_produit.append(prod5['price'])
              namesite.append(chaine_site)

         produit_data6 = jsondata['menu']['modifier_groups'][6]['modifier_options'] 
         for prod6 in produit_data6:
              name_produit.append(prod6['name'])
              desc_produit.append(prod6['description'])
              price_produit.append(prod6['price'])
              namesite.append(chaine_site)

     except:
          pass






#print (name_produit)
#print (desc_produit)
#print(price_produit)
################################################ foodCheri  #################################################################################
result_foodcheri = requests.get("https://www.foodcheri.com/")

src= result_foodcheri.content 
#print (src)

soup = BeautifulSoup(src,"lxml")
#print(soup)

script = soup.find("script",{"id":"__NEXT_DATA__","type":"application/json"}).string
#print(script)


jsondata = json.loads(script)
#print(jsondata)

produit_data_food = jsondata ['props']['pageProps']['initialState']['home']['menu']['publications']['byId']
#print(produit_data)
chaine = "foodcherie"
name_site=[]
title_produit_food =[]
price_produit_food = []
type_produit_food = []
for prod in produit_data_food:

    produit_data2_food = jsondata ['props']['pageProps']['initialState']['home']['menu']['publications']['byId'][prod]
    title_produit_food.append (produit_data2_food['title']) 
    price_produit_food.append (produit_data2_food['price'])
    type_produit_food.append (produit_data2_food['productTypeName'])
    

for pr in range(len(produit_data_food)):
    name_site.append(chaine) 

site =[]
site = namesite+name_site
titre =[]
titre = name_produit+title_produit_food
desc=[]
desc = desc_produit+type_produit_food
price =[]
price = price_produit+price_produit_food

#print(len(titre))
#print(len(desc))
#print(len(price))
#print(len(site))
"""
idi = -1
list_ind_sup =[]
for sup in desc :
     idi = idi+1 
     if (sup == "None" or sup =="" or sup == None ):
         list_ind_sup.append(idi)
         #desc.remove 
"""
#print("**************************************************************************")
#print(list_ind_sup)

"""
for p in range(len(desc)):
     for s in list_ind_sup:
          if (p==s):
               desc.pop(p)
                   
"""   

#print("****************************************************************************")
#print(desc)
""""
thislist = ["apple", "banana", "cherry"]
for o in range(len(thislist)):
     print(o)
     thislist.pop(1)
print(thislist)
"""


###############################################recherch #######################################################


chaine ="Glace"
#chaine = input('la chaine : ')
#print (mydata)

def verif(list, chaine):
    result = False
    for i in  list:
        if( i == chaine ):
           result= True
      


    return result





List_titre =[]
list_indice = []
def verif_titre(chaine , titre ):
      inde = -1
      for j in titre:
           
              inde = inde+1
              List_titre = j.split()
              if (verif(List_titre , chaine) == True ): 
                  #print(inde)
                  list_indice.append(inde) 
           
                   
               
      return list_indice              
  
       

#print (verif_titre(chaine , titre))

List_desc = []
list_ind = []
def verif_desc(chaine , desc ):
      inde = -1
      for j in desc:
          try:   
             #print(j)
             inde = inde+1
             List_desc = j.split()
             #print(List_desc)
             if (verif(List_desc , chaine) == True ): 
                #print(inde)
                list_ind.append(inde) 
          except:
              pass  
                 
               
      return list_ind             
  
#print(list_ind)
#print (verif_desc(chaine , desc ))      


#def Par_titre(chaine,autheurs):
dern_titre =[]
dern_desc =[]
dern_price =[]
dern_site = []
lii = []
lii = (verif_titre(chaine , titre ))

for l in lii:
    #print(l) 
    for a in range(len(titre)):
        #print (a)
        for t in range(len(desc)):
            
            #print(t)
            if (l == a == t  ):
                dern_titre.append(titre[a])
                dern_desc.append(desc[t])
                  
for l in lii:
    for p in range(len(price)):
          if(l == p ):
              dern_price.append(price[p]) 

for l in lii:
    for p in range(len(site)):
          if(l == p ):
              dern_site.append(site[p]) 


#print (Par_Auteur(chaine,autheurs))
#print(len(dern_titre))
#print("**********************************")
#print(len(dern_desc))
#print("**********************************")
#print(len(dern_price))
#print("**********************************")
#print(len(dern_site))



#def Par_desc(chaine2,titles):    
titre_bydesc =[]
desc_bydesc =[]
price_bydesc = []
site_bydesc =[]
li = []
li = (verif_desc(chaine , desc ))
for lll in li: 
    for tit in range(len(titre)):
        for de in range(len(desc)):            
            if (lll == tit == de ):
                titre_bydesc.append(titre[tit])
                desc_bydesc.append(desc[de])
                     
for lll in li: 
    for s in range(len(price)):
        if(lll == s):
            price_bydesc.append(price[s])

for lll in li: 
    for h in range(len(site)):
        if(lll == h):
            site_bydesc.append(site[h])



#return(auth_byText,title_byText )

#print(titre_bydesc)
#print(desc_bydesc)
#print(price_bydesc)
#print(site_bydesc)


#print (Par_Text(chaine2 , titles))


#def par_texte_desc(chaine , titre , desc):
li_textt = []
li_textt = (verif_titre(chaine , titre ))
#print(li_textt) 
li_a = []
li_a = (verif_desc(chaine , desc ))
#print(li_a)
au_text =[]
desc_byText2 =[]
title_byText2 =[]
price_bytext2 = []
site_bytext2 = []
for k in li_a:
    for a in li_textt:
        if (k == a):
            au_text.append(k)


#print(au_text)

for s in au_text:
    #print(l) 
    for c in range(len(titre)):
        #print (a)
        for t in range(len(desc)):
            #print(t)
            if (s == c == t ):
                desc_byText2.append(titre[c])
                title_byText2.append(desc[t])                  

for s in au_text:
    for y in range(len(price)):
        if( s== y ):
            price_bytext2.append(price[y])

for s in au_text:
    for m in range(len(site) ):
        if(s==m):
            site_bytext2.append(site[m])            




#return(auth_byText2 ,title_byText2)

#print(desc_byText2)
#print(title_byText2)









#############################################################
#create csv tous le liste de tous les produit 

file_list = [titre , desc , price, site ]
exported = zip_longest(*file_list)

with open("/Users/Public/comparaison/comparaison_food.csv", "w", encoding='utf-8') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["NAME  PRODUIT " , " DESCRIPTION PRODUIT " , " PRIX PRODUIT " , "NAME SITE  " ])
    wr.writerows(exported) 


################################################################

#create csv tous le liste par titre 

file_list = [dern_titre , dern_desc , dern_price ,dern_site  ]
exported = zip_longest(*file_list)

with open("/Users/Public/comparaison/par_titre_de.csv", "w", encoding='utf-8') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["NAME  PRODUIT " , " DESCRIPTION PRODUIT " , " PRIX PRODUIT " , "NAME SITE  " ])
    wr.writerows(exported) 

################################################################


#create csv tous le liste par desc 

file_list = [titre_bydesc , desc_bydesc , price_bydesc ,site_bydesc  ]
exported = zip_longest(*file_list)

with open("/Users/Public/comparaison/par_desc_de.csv", "w", encoding='utf-8') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["NAME  PRODUIT " , " DESCRIPTION PRODUIT " , " PRIX PRODUIT " , "NAME SITE  " ])
    wr.writerows(exported) 

################################################################

#create csv tous le liste par desc et titre  

file_list = [title_byText2 , desc_byText2 , price_bytext2 ,site_bytext2  ]
exported = zip_longest(*file_list)

with open("/Users/Public/comparaison/par_titre_desc.csv", "w", encoding='utf-8') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["NAME  PRODUIT " , " DESCRIPTION PRODUIT " , " PRIX PRODUIT " , "NAME SITE  " ])
    wr.writerows(exported) 


    
     
      








