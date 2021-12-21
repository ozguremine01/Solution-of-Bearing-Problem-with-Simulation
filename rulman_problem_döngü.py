import random
import statistics
import numpy as np
import pandas as pd
import seaborn as sns

rulman_calisma_olasılık=[.1,.13,.25,.13,.09,.12,.02,.06,.05,.05]
rulman_calisma_süre=[]
for i in range(1000,2000,100):
    rulman_calisma_süre.append(i)
print(rulman_calisma_süre)
para=[]
gecikme_süresi=[5,10,15]
gecikme_olasilik=[.6,.3,.1]
tamirci_tutar_list=[]
ortalama_para=[]
for dene in range(0,100):
    rulman1=[]
    rulman2=[]
    rulman3=[]
    degişim_rda=[]
    sayi=[]
    degisim_sayisi=dene
    for d in range(1,degisim_sayisi+1):
        sayi.append(d)

    for x in range(0,degisim_sayisi):
        a=random.randint(0,100)
        b=random.randint(0,100)
        c=random.randint(0,100)
        degis_rda=random.randint(1,9)
        degişim_rda.append(round(degis_rda,0))
        rulman1.append(round(a,0))
        rulman2.append(round(b,0))
        rulman3.append(round(c,0))
    df_3_rulman=pd.DataFrame(data={'Rulman1': rulman1, 'Rulman2': rulman2, 'Rulman3': rulman3})

    df_rulman=pd.DataFrame(data={'Rulman Çalışma süreleri': rulman_calisma_süre, 'Olasılık': rulman_calisma_olasılık})

    print(df_rulman)
    tp=0
    toplam=[]
    rulman_rda=[]
    b=0
    for y in range(0,10):
        tp=tp+df_rulman['Olasılık'][y]
        toplam.append(tp)
        rulman_rda.append([b,round(tp*100)])
        b=round(tp*100+1)

    df_rulman['Kümülatif Olasılık']=toplam
    df_rulman['RDA']=rulman_rda
    print(df_rulman)
    tp1=0
    toplam1=[]
    gecikme_rda=[]
    b1=1
    df_gecikme=pd.DataFrame(data={'Gecikme süresi': gecikme_süresi, 'Olasılık': gecikme_olasilik})
    for y1 in range(0,3):
        tp1=tp1+df_gecikme['Olasılık'][y1]
        if tp1 != 10:
            toplam1.append(tp1)
            gecikme_rda.append([b1,round(tp1*10)])
            b1=round(tp1*10+1)
        else:
            pass
        

    df_gecikme['Kümülatif Olasılık']=toplam1
    df_gecikme['RDA']=gecikme_rda
    print(df_gecikme)
    r1=[]
    r2=[]
    r3=[]
    for y4 in range(0,degisim_sayisi):
        c=df_3_rulman['Rulman1'][y4]
        for f in range(10):
            if df_rulman['RDA'][f][0]<=c and df_rulman['RDA'][f][1]>=c:
                r1.append(df_rulman['Rulman Çalışma süreleri'][f])
                continue
            else:
                pass
        
        
    for y5 in range(0,degisim_sayisi):
        c1=df_3_rulman['Rulman2'][y5]
        for f1 in range(10):
            if df_rulman['RDA'][f1][0]<=c1 and df_rulman['RDA'][f1][1]>=c1:
                r2.append(df_rulman['Rulman Çalışma süreleri'][f1])
                continue
            else:
                pass

    for y1 in range(0,degisim_sayisi):
        c2=df_3_rulman['Rulman3'][y1]
        for f2 in range(0,10):
            if df_rulman['RDA'][f2][0]<=c2 and df_rulman['RDA'][f2][1]>=c2:
                r3.append(df_rulman['Rulman Çalışma süreleri'][f2])
                continue
            else:
                pass

    print(r1)
    print(len(r1))
    print(r2)
    print(len(r2))
    print(r2)
    print(len(r2))
    print(len(rulman_rda))

    print(df_3_rulman)

    df_genel=pd.DataFrame(data={'Değişim sayisi ':sayi, 'Rulman1 RDA ':rulman1, 'Rulman1 Süre': r1, 'Rulman2 RDA': rulman2, 'Rulman2 Süre': r2, 'Rulman3 RDA': rulman3, 'Rulman3 Süre': r3})
    print(df_genel)
    kücük_sayi=[]
    for i in range(0,degisim_sayisi):
        kücük=min(df_genel['Rulman1 Süre'][i],df_genel['Rulman2 Süre'][i],df_genel['Rulman3 Süre'][i])
        kücük_sayi.append(kücük)
            
    print(kücük_sayi)
    print(len(kücük_sayi))

    df_genel['İlk başarısızlık yaşanıncaya kadar ki geçen süre']=kücük_sayi

    df_genel['Gecikme RDA']=degişim_rda

    print(df_genel)
    gecikme=[]
    for w in range(0,degisim_sayisi):
        rda=df_genel['Gecikme RDA'][w]
        for f6 in range(0,3):
            if df_gecikme['RDA'][f6][0]<=rda and df_gecikme['RDA'][f6][1]>=rda:
                gecikme.append(df_gecikme['Gecikme süresi'][f6])
            else:
                continue

    print(gecikme)
    print(len(gecikme))
    
    df_genel['Gecikme Süreleri']=gecikme
    print(df_genel)
    tamirci_tutar=round(((degisim_sayisi+1)*40*30)/60,0)
    tamirci_tutar_list.append([dene,tamirci_tutar])
    gecikme_süresi_kayip_para=sum(gecikme)*10
    para.append([(dene+1,gecikme_süresi_kayip_para)])
    ortalama_para.append([(dene+1,gecikme_süresi_kayip_para/(dene+1))])
print(tamirci_tutar_list)
print('*************************************************************************')
print(para[0][0][0])

para1=[]
para2=[]
ort_para1=[]
ort_para2=[]
for r in range(0,100):
    print(para[r][0][0])
    para1.append(para[r][0][0])

for r1 in range(0,100):
    print(para[r1][0][1])
    para2.append(para[r1][0][1]/100)
for r3 in range(0,100):
    print(ortalama_para[r3][0][0])
    ort_para1.append(ortalama_para[r3][0][0])

for r4 in range(0,100):
    print(ortalama_para[r4][0][1])
    ort_para2.append(ortalama_para[r4][0][1])

import matplotlib.pyplot as plt
plt.plot(para1,para2, color='r')

plt.plot(ort_para1,ort_para2, color='b')
"""
plt.xlabel("Değişim sayıları")
plt.ylabel("Gecikme para kaybı")
"""
plt.xticks(ort_para1)

plt.show()
