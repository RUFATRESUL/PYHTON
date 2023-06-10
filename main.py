# print('ha'*(200))


# a=27//3

# print(a)   

# print(type(6/3))

# val=2+10*3-12**5
# print(val)



# name='Pyhton'
# if 'z' in name:
#     print('vardir')
# else: 
#     print('yoxdur')
################### 
# print(round(256.91872,2))
# print(round(256.91872,-2))
###########################
# print(pow((15%4),3))
############################
# web = "https:// .com"
# web = input("enter site:")
# print(web.removeprefix("https://").removesuffix(".com"))
######################################
# number="34"
# print(number.rjust(5,"0"))
##############################
# card ="5382-1739-9201-9017"
# print(card[4:15].center(16,"*"))
# print(card[9:].rjust(16,"*"))
#############################3



##############################
# password = input("sifreni daxil edin:")
# if len(password)>=5 or len(password)<=10:
#     if password.isascii():
#         if password.isupper():
#             if password.islower():
#                 if password.isnumeric():
#                  print("daxil etdiyiniz sifre dogrudur")  
#                 else:
#                    print("zehmet olmasa reqem daxil edin")

#             else:
#                 print(" kicik herif olmalidi")
#         else:
#            print(" boyuk herif olmalidi")
#     else:
#        print(" ingilis siriftleri olmalidir")
# else:
#     print("daxil etdiyiniz sifre yanlisdir")

##############################################

# text=' sehivelerden xosuma gelen bu sehivedir'

# print(text.replace("sehive","sehife"))
############################################
# phone = input("Zehmet olmasa nomrenizi daxil edin:")
# if len(phone)==14:
#     if phone.startswith("+994"):
#         if phone.isnumeric():
#          print("daxil etdiyiniz nomre dogrudur")
#         else:
#            print("zehmet olmasa reqem daxil edin")

#     else:
#       print("zehmet olmasa +994 prefiksini daxil edin")
# else:
#     print("Daxil etdiyiniz nomre yanlisdir")

 #######################################################

# for i in range(100000, 9999, -1):
#     if i % 9999 == 0:
#         print(i)
#         break
#####################################################
# toplam = 0

# for i in range(1,101):
#     toplam += i

# print( toplam)
###############################################
# cumle="men her gun pyhton oyrenirem"
# vowels="aioue"
# new_str=""
# for x in cumle:
#     if x not in vowels:
#         new_str+=x
# print(new_str)
######################################
# second="men her gun pyhton oyrenirem"
# volo="aioue"
# new_text=""
# counter=len(second)-1
# for char in second:
#     char=second[counter]
#     if char not in volo:
#         new_text+=char
#     counter-=1
# print(new_text)
###############################################            
# sentence= input("cumleni daxil edin:") 
# saitler="aioueəüöı" 
# sait_ses=0
# for h in sentence:
#     if h in saitler:
    
#         sait_ses=sait_ses+1
#     print(h,sep="-",end="-")
# print("cumlediki hecalarin sayi:",sait_ses)
######################################################
# ferma=['at','qoyun','inek','at','inek','qoyun','at','keci']
# ferma.sort()
# print(ferma)

# index=ferma.index('keci')
# print(index)

# ferma[6]='toyuq'
# print(ferma).


# ferma.insert(0,'keci')
# print(ferma)

# count=ferma.count('inek')
# inek=len(ferma)/count*100
# print("ineklerin sayi:",inek,"%")


# del ferma[0:5]
# print(ferma)

# a=['at','qoyun','inek','inek','qoyun']
# a.extend(ferma)
# print(a)

# ferma.reverse()
# print(ferma)

# numbers=ferma.copy()
# print(numbers)

# ferma.clear()
# print(ferma)
##########################################
# result=[0,0]
# num = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
# # num_1=154.20
# # num_2=-71.84
# result[0]=154.20
# result[1]=174.80
# print(result)
################################

# single = input("Tek reqemli bir eded girin: ")
# double = [int(i) for i in str(single)][::-1]

# print(double)
############################
# my_list = ['apple', 'banana', 'pear', 'orange', 'grapes', 'carrot']

# five_letter_words = []
# six_letter_words = []

# for item in my_list:
#     if len(item) == 5:
#         five_letter_words.append(item)
#     elif len(item) == 6:
#         six_letter_words.append(item)

# print("5 herfli sozler:", five_letter_words)
# print("6 herfli sozler:", six_letter_words)
########################################################################
# sehir_list=['Tokyo','Roma','Istanbul','Amsterdam','Oslo','Edinburgh']
# saitler='AIOUEƏÜİÖaiüəiöı '
# city_name=[]
# for name in sehir_list:
#     if name[0] in saitler:
#         city_name.append(name)
# city_name.sort()
# city_name.reverse()

# print(city_name)
#######################################################

# name_liste = ['Kenan', 'Fidan', 'Abdullah', 'Nizami','borani']
# saitSes = 'aiouüəöıe'
# heca = []

# for name_zero in name_liste:
#     b = sum(1 for harf in name_zero.lower() if harf in saitSes)
#     if b ==3:
#         heca.append(name_zero)
# # print(heca,sep="-",end="-")
# heca.reverse()

# print(heca)
##################################
# users = [
#     {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
#     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
#     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# ]
# username=input('adinizi daxil edin:')
# pasword=input('sifrenizi daxil edin:')
# current_user=None
# for user in users:
#     if username==user['username']:
#      if pasword==user['password']:
#          current_user=user
#      print('istifadeci daxil oldu')
#     else:
#         print('sifre yanlisdir')
#     else:
#         print('istifadeci adi yanlisdir')
# # ##################################################
# user = {
#     'name': 'Elnur',
#     'height': 179,
#     'phone': {
#         'model': 'Iphone',
#     },
#     'orders': ['book', 'mouse', 'mousepad']
# }
# user['height']+=1
# print(user)

# user['phone']='Samsung'
# print(user)
# del user['name']
# print(user)
# del user['orders'][0]
# print(user)
# user['orders'].insert(0,'ball')
# print(user)
# user['orders'].append('headphone')
# print(user)
# ##########################################
# info=['Resul','Serifov',35]
# info=[info[0]+" "+info[1],25]
# print(info)
# # ###############################################

# # 5.
# shop = {
#     "t-shirt" : 59.00,
#     "jeans" : 75.00,
#     "sweatshirt" : 60.00, 
#     "shoe" : 124.99, 
#     "jacket" : 154.90
# }

# product = input("Məhsulun adını daxil edin: ")
# price = shop.get(product, "None")
# print(price)

# # 6.
# shop.update({"hat": 25.99, "scarf": 39.50})
# print(shop)

# # 7.
# num_products = len(shop)
# # print(f"Mağazada {num_products} məhsul var.")
# print(num_products,"mehsul var")
# # 8.
# for key in shop:
#     shop[key] *= 1.3
# print(shop)

# # ####################################
# user_info = {
#     'firstname': 'Elvin',
#     'lastname': 'Huseynov',
#     'username': 'elivin_h_ov',
#     'password': '12345',
#     'birthday': '19-08-1997'
# }
# user_info.update({
#     'firstname': 'Elcin',
#     'lastname': 'Huseynov',
#     'username': 'elchina',
#     'password': '12345',
#     'birthday': '18-08-2000'
# })
# print(user_info)
# ################################

# num, text = input('cumle daxil edin').split()
# num = int(num)
# result = text+" "
# for i in range(1,num):
#    result += text+" "
# print(result.strip()) 
# #########################################
# num_list = [y*3 for y in range(-100,100) if y % 7 == 0 ]
# print(num_list)
# ##############################################
# number=[2384, 12385, 13226, 653, 12362423]
# keys_list=[4,5,5,3,8]
# form={k:v for (k,v)in zip(number,keys_list)}
# print(form)
# ########################
# cumle=input('text daxil edin')

# print(cumle[::-1])
# #############################3



# l="GFG"
 

# dic = {
#     x: {y: x + y for y in l} for x in l
# }
 
# print(dic)
# ###################################
# animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')
# farm = ('inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at',
#          'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq',
#         'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 'at', 'qoyun', 'inek', 
#         'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 
#         'keci', 'inek', 
#         'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}
# heyvanAdi=animal
# heyvanSayi=farm.count(heyvanAdi)
# umumiFaiz=farm.count(heyvanAdi)/len(farm)*100
# umumiQiymet=heyvanSayi*qiymetler[heyvanAdi]

# altXett=10*'-'

# text ='''
# heyvanAdi:{0}
# {1}
# fermadaki{0}sayi:  {2}
# umumiFaiz: {3:.2f}%
# {0}:umumiQiymeti: {4}AZN'''.format(heyvanAdi,altXett,heyvanSayi,umumiFaiz,umumiQiymet)

# print(text)
#######################################
# text_input = input('cumle daxil edin:')
# text=[ord(char_next)for char_next in text_input]

# print(text)
#####################################
# string_input = input('cumle daxil edin:')

# string=[ord(char)for char in string_input]
# for slow in string:
#    print(bin(slow)[2:])
# string_input = input('cumle daxil edin:')

# string=' '.join(format(ord(char),'08b')for char in string_input)
# print(str(string))
# ####################################
# ferma = ('at', 'inek', 'inek', 'keci', 'qoyun', 'qoyun', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'inek', 'keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', 'keci', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}
# boyuk_qardasin_fermasi=ferma[:len(ferma)//2]
# kicik_qardasin_fermasi=ferma[len(ferma)//2:]
# boyuk_qardasin_serveti=sum(qiymetler[var_dovlet]for var_dovlet in boyuk_qardasin_fermasi)
# kicik_qardasin_serveti=sum(qiymetler[var_dovlet]for var_dovlet in kicik_qardasin_fermasi)
# if boyuk_qardasin_serveti>kicik_qardasin_serveti:
#    pul_ferqi=boyuk_qardasin_serveti-kicik_qardasin_serveti
#    print('boyuk qardas kicik qardasa',pul_ferqi,'vermelidir')
# elif kicik_qardasin_serveti>boyuk_qardasin_serveti:
#     pul_ferqi=kicik_qardasin_serveti-boyuk_qardasin_serveti
#     print('kicik qardas boyuk qardasa',pul_ferqi,'vermelidir')
# else:
#    print('her iki qardasin serveti eynidir')

#######################################################
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
# num_str1=max(numbers)
# num_str2=min(numbers)
# print(num_str1)
# print(num_str2)
##################################
# r=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]
# telebeler=len(r)
# ortalama=sum(r)/len(r)
# count=0
# for num in r:
#     if num<51:
#         count+=1
# kesilenler=count/len(r)*100
# count=0

# for num in r:
#     if num>80:
#         count+=1

# zerbeciler=count/len(r)*100
# print("telebe sayi:",telebeler,"\nUmumi ortalama:",ortalama,"%","\nkesilen telebe faizi:",kesilenler,"%","\nzerbeciler faizi:",zerbeciler,"%")
#####################################
# total = 0
# i = 1

# while i <= 100:
#     total += i
#     i += 1
# print(total)
#####################################
# text = "Men Pyhton oyrenirem"
# vowels = "aeiou"
# result = ""
# i = 0
# while i < len(text):
#     if text[i] not in vowels:
#         result += text[i]
#     i += 1

# print(result)
##########################
# number = 100000
# while number > 0:
#     if number % 9999 == 0:
#         print(number) 
#         break
   
#     number -= 1
##################################### 

# i = 300
# while i>0:
#     if i%69==0:
#         print(i)
#         break
#     i -=1

#######################################

# look=0
# loop=int(input("enter number"))
# while loop!=0:
#     look+=loop
#     loop=int(input("enter number"))
# print("total",look)
######################################

# punion(*args):
#     return ''.join([s[0].upper() for s in args])
   

# print(upunion('birlesmis', 'milletler', 'teskilati'))
# #############################################

# def numbers(*args): 
#     max_number=max(args)
#     min_number=min(args)
#     number=max_number-min_number
#     print(number)
# numbers(6, 3, 8, 9, 2)  
# ##########################################3
# def num(*args):
#     return sum(int(str(reqem)[::-1])for reqem in args)
# print(num(123,567,562))
# #######################################
# def find_percent(first,second):
#     dif=first-second
#     percent=abs(dif/first)*100
    
#     if(first<second):
#         print(f'qiymet{percent:.2f}%artmisdir')
#     else:
#         print(f'qiymet{percent:.2f}%azalmisdir')
    
# find_percent(900,100)
# ########################
# def cumle(text,**kwargs):
#     for key,value in kwargs.items():
#         text=text.replace(key,value)
#     return text

# print(cumle('Kitabi sehive-sehive oxumalisanki orgene bilesen',sehive='sehife',orgen='oyren'))






    
    


# ##################################
# def getManat(*args):
#     result=0
#     for d in args:
#         result+=d
#     result=result*1.7
#     return round(result,2)
# print(getManat(10,10))
# ########################



# def getDollar(**kwargs):
#     exchange = {
#         'Dollar': 1.7,
#         'TL': 11.39
#     }
#     amount = kwargs['currency']
#     fromCurrency = kwargs['fromcurrency']
#     toCurrency = kwargs['tocurrency']
#     exchangeCurrency = exchange[fromCurrency] / exchange[toCurrency]
#     currencyAmount = exchangeCurrency * amount
#     return round(currencyAmount,2)

# print(getDollar(currency=100, fromcurrency='Dollar', tocurrency='TL'))
# ##########################
# def get_exchange(number):
#     result=0
#     for i in number:
#         result+=i
#         return result
# def exchange(*args,**kwargs):
#     print(args,kwargs)
#     for key,value in kwargs.items():
#         print(f'{key.upper()}:{get_exchange(args)*value}')

# exchange(23,100,10,azn=1.7,tl=20)

# get_exchange([23,100,10])

# #######################################
# eded_herif={
#     0:{'1':'bir','2':'iki','3':'uc','4':'dort','5':'bes','6':'alti','7':'yeddi','8':'sekkiz','9':'doqquz'},
#     1:{'1':'on','2':'20','3':'otuz','4':'qirx','5':'elli','6':'altmis','7':'yetmis','8':'seksen','9':'doxsan'},
#     2:{'1':'yuz', '2':'ikiyuz','3':'ucyuz','4':'dortyuz','5':'besyuz','6':'altiyuz','7':'yeddiyuz','8':'sekkizyuz','9':'doqquzyuz'},
#     3:{'1':'min','2':'ikimin','3':'ucmin','4':'dortmin','5':'besmin','6':'altimin','7':'yeddimin','8':'sekkizmin','9':'doqquzmin'}
# }

# def get_number_name(num):
#     revnum=str(num)[::-1]
#     result=' '
#     for index,digit in enumerate(revnum):
#         if digit=='0':
#             continue
#         word=eded_herif.get(index).get(digit)
#         result=word+' '+result
    
#     return result

# print(get_number_name(567))
#  #################################3 
# def ing_cevir(func):
#     def wrapper(*args):
#        value=func(*args)
        
#        return value.replace('ə','e').replace('ö','o')
#     return wrapper



# @ing_cevir
# def salam_ver(ad, soyad):
# 	return 'Salam hörmətli {} {}, necəsiniz?'.format(ad, soyad)

# print(salam_ver('Arif', 'Həsənov'))
# # output: Salam hormetli Arif Hesenov, necesiniz?
# ####################################
# #recursive function tasklari
# func=lambda z:z*func(z-1)if(z>1) else 1
# print(func(5))
# ############################
# # 1
# sorti=[{'a': 1, 'b': 2}, 5, 7.8, 'asdf', 23, ['a', 'b'], True,  False]
# lists=[]
# dictionary=[]
# boolen=[]
# integers=[]
# floats=[]
# strings=[]
# for element in sorti:
#     if type(element) is list:
#         lists.append(element)
#     elif type(element) is dict:
#         dictionary.append(element)
#     elif type(element) is bool:
#         boolen.append(element)
#     elif type(element) is int:
#         integers.append(element)
#     elif type(element) is float:
#         floats.append(element)
#     elif type(element) is str:
#         strings.append(element)
# element=sorted(lists)+sorted(dictionary)+sorted(boolen)+sorted(integers)+sorted(floats)+sorted(strings)
# print(element)
# # 2
# types=[list,dict,bool,int,float,str]
# data=[{'a':1,'b':2},5,7.8,'asdf',23,['a','b'],True,False]
# data_sorted=sorted(data,key=lambda el:types.index(type(el)))
# print(data_sorted)

# ###########################################################
# # 1
# numbers = [85856, 73930, 95298, 57870, 99688, 92907, 13075, 12905, 52948, 97687, 10832, 78757, 99502, 65889, 34618, 59109, 83419, 31486, 94522, 34400]
# numer = []
# for number in numbers:
#     digits = [int(digit) for digit in str(number)]
#     total = sum(digits)
#     if isinstance(total, int):
#       numer.append(total)
# # max_num=max(numer)
# # print(max_num)
# print(numer)def u
# 2
# numbers_one = [85856, 73930, 95298, 57870, 99688, 92907, 13075, 12905, 52948, 97687, 10832, 78757, 99502, 65889, 34618, 59109, 83419, 31486, 94522, 34400]
# def get_digits_sum(number):
#     digits=map(lambda x:int(x),str(number))
#     return sum(digits)
# max_value=max(numbers_one,key=get_digits_sum)
# min_value=min(numbers_one,key=get_digits_sum)
# print(max_value)
# print(min_value)
# ############################
# children = ['Arif', 'Babek', 'Hesen', 'Rufet', 'Sahin', 'Eldeniz', 'Turan', 'Sahmar', 'Kamal', 'Ruslan']
# gifts = ['Ball', 'Iphone', 'Bicycle', 'Ball', 'Piano', 'Bicycle', 'Socks', 'Play Station', 'Ball', 'Socks']
# prices = {'Ball': 10, 'Iphone': 1100, 'Bicycle': 500, 'Piano': 1500, 'Socks': 10, 'Play Station': 1200}
# children_gifts=zip(children,gifts)
# sorted_children_gifts=sorted(children_gifts,key=lambda x:prices.get(x[1]),reverse=True)
# for child,gift in sorted_children_gifts:
#     print('{}{}manat deyerinde {} goturub'.format(child,prices[gift],gift))
# #######################################

  # SET TASKS ############################

# baliqlar = {
#     'qelseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
#     'yumurtlama', 'dis yoxdur', '4 ayaq'}

# cuculer = {
#     'toraks teneffusu', 'urek yoxdur', '6 ayaq',
#     'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz', 
#     'dis yoxdur'
# }

# amfibialar = {
#     'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq', 
#     '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'koteks vardir',
#     'yumurtlama', 'dis yoxdur'
# }

# surunenler = {
#     'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
#     'dis var'
# }

# quslar = {
#     'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
#     'yumurtlama', 'dis yoxdur'
# }

# memeliler = {
#     'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
#     'dogma', 'dis vardir'
# }

# sinifler = {
#     'baliqlar': baliqlar,
#     'cuculer': cuculer,
#     'amfibialar': amfibialar,
#     'surunenler': surunenler,
#     'quslar': quslar,
#     'memeliler': memeliler,
# }
   
# quslar.add('2 ayaq')  
# print(quslar)

# baliqlar.remove('4 ayaq')
# print(baliqlar)
# print(amfibialar.intersection(cuculer))
# print(baliqlar.difference(amfibialar))
# ############################
# for sinif_adi, sinif in sinifler.items():
#     if sinif_adi != 'baliqlar' and not baliqlar.intersection(sinif):
#         print(sinif_adi)
# #####################
# user_data = input("Zəhmət olmasa xususiyyetleri daxil edin: ")
# def find_animal():
 
#     animal = []
#     for key, value in sinifler.items():
#         if set(user_data.split(', ')).issubset(value):
#             animal.append(key)
#     if not animal:
#         print("Bu heyvan heç bir sinifə aid ola bilməz.")
#     else:
#         print("Bu heyvan",', '.join(animal),"sinifinə aid ola bilər.")
# find_animal()



#####################
# first_name=str(input('adinizi daxil edin'))
# email=str(input('emailnizi daxil edin'))
# password=input('sifrenizi daxil edin')
# password_again=input('sifrenizi tekrar daxil edin')
# try:
#     if first_name.capitalize().isalpha():
#         print('daxil etdiyiniz ad dogrudur')
#     else:
#         print('daxil etdiyiniz ad yanlisdir')
   
# except:
#     print('first name sintaksis xetasi var')
# try:
#     if email.endswith('@ gmail.com'):
#         print('daxil etdiyiniz email dogrudur')
#     else:
#         print('daxil etdiyiniz email dogru deyil')

# except:
#     print('email simvol xetasi var')
# try:
#     if len(password)>8 or len(password)<10:
#         print('daxil etdiyiniz sifre dogrudur')
#     else:
#         print('daxil etdiyiniz sifre yanlisdir')
# except:
#     print('password sifre yanlisligi var')
# try:
#     if len(password)>8 or len(password)<10:
#         print('daxil etdiyiniz sifre dogrudur')
#     else:
#         print('daxil etdiyiniz sifre yanlisdir')
# except:
#     print('yeniden daxil edilende sifre yanlisligi var')
# finally:
#     print('sizin daxil etdiyiniz login dogrudur')
#########################
#ERROR HANDLE

# try:
    
#     animals = input('Heyvanlari girin: ').split(', ')
#     # if len(animals)<3 or len(animals)>6:
#     #    raise ValueError('element sayi dogru deyil') 
#     prices = { 'inek': 500, 'toyuq': 50, 'qoyun': 120, 'at': 900, 'keci': 210  }   
       
#     print('umumi qiymet', sum(map(lambda animal: prices[animal], animals)))
  
    
# except KeyError as error_message:
#        print(f'the key error is:{error_message}')


# except Exception as error_message:
#     print(f'gozlenilmez xeta bas verdi:{error_message}')
# else:
#      print('kod bloku isleyir')
# finally:
#      print('proqram bitdi')


# inp=input('reqem1')
# ino=input('reqem2')
# try:
#     result=int('reqem1')+int('reqem2')
#     print(result)
# except ValueError as error_message:
#      print(f'zehmet olmasa reqem daxil edin{error_message}')
# except ZeroDivisionError as error_message:
#      print(f'zehmet olmasa sifir daxil etmeyin{error_message}')
# except Exception:
#      print('xeta bas verdi')
# finally:
#      print('proqram sona catdi')
##############################################
# #FILE HANDLE
# def minify(file_path):
#     file=open(file_path,mode='r')
#     text=file.read()
#     file.close()
#     code=''.join(text.split())
#     file=open(file_path,mode='w')
#     file.write(code)
#     file.close()
# try:
#     file_path=input('minify etmek istediyiniz fayilin adresin girin')
#     minify(file_path)
#     print('fayl ugurla minfy edildi')
# except FileNotFoundError:
#     print('fayil tapilmadi')

#####################
# file=open('text.txt',mode='r',encoding='UTF-8')
# file.close()
# with open('text.txt','r',encoding='UTF-8') as file:
#     rows=file.readlines()

# rows.sort(key=lambda row:int(row.split()[2],reverse=True))
# with open('text.txt','w',encoding='UTF-8') as file:
#     file.writelines(rows)
               
            

# ###################
# with open('list.txt','w') as file:
#      for i in range(1000,0,-1):
#           file.write(f'{str(i).zfill(4)}.')
################## MODULLAR TASKS

############################

#######################
# from math import pi,comb,perm
# #kubun hecmi
# def kubun_hecmi(a):
#     kub=a**3
#     print(kub)
# kubun_hecmi(2)

#dordbucaqli prizma
# def prizma(l,m,n):
#     volume=l*m*n
#     print(volume)
# prizma(4,5,6)
#silindir
# def silindir(r,h):
#     global pi
     
#     silindir=pi*r**2*h
#     print(int(silindir))
# silindir(3,10)

#konus
# def konus(r,h):
#     global pi
    
#     konuser=(1/3)*pi*r**2*h
#     print(int(konuser))

# konus(10,5)



#pramid
# def pramid(a,h):
#     pramid=(1/3)*a**2*h
#     print(int(pramid))
# pramid(5,10)

# # #kure
# def kure(r):
#     global pi
# #     pi=3.1415
#     kure=(4/3)*pi*r**3
#     print(int(kure))
# kure(8)

# #########################
#kombinasiya
# def combinasiya(n,r):
#     global comb
#     comb=comb(n,r)
#     print(comb)
# combinasiya(10,8)

# #permutasiya

# def permutasiya(n,r):
#     global perm
#     perm=perm(n,r)
#     print(perm)
# permutasiya(10,9)


###############
# import random
# form=input('adlari daxil edin: ').split(', ')
# ad_siyahisi=len(form)
# while True:
#     input('yeniden ad daxil edin: ')
#     secilen_ad = random.choice(form)
#     form.remove(secilen_ad)
#     ad_siyahisi-=1
#     print(secilen_ad)
    
  
#     if ad_siyahisi==0:
#         print('adlar bitdi')
#         break
    
# texmini_eded=random.randint(1,50)
# texmin_haqqim=10
# saygac=0
# while True:
#     verilen_eded=int(input('zehmet olmasa 1-50 arsi eded texmin edin '))
#     texmin_haqqim-=1
#     saygac+=1
#     if verilen_eded < texmini_eded:
#         print('kicik eded daxil etdiniz ,Zehmet olmasa boyuk eded daxil edin')
#     elif verilen_eded > texmini_eded:
#         print('boyuk eded daxil etdiniz, Zehmet olmasa kicik eded daxil edin')
#     else:
#         print(f'tebrikler daxil etdiyiniz eded{texmini_eded} dir')
#         print(f'bu ededi {saygac} defeye tapdiniz')
#         break
#     if texmin_haqqim==0:
#         print('teessuf olsun ki, texmin etme haqqin kecmisiz ')
#         break




#####################

# from datetime import datetime,timedelta

# mesafe=588000000
# suret=90
# vaxt=mesafe/suret
# zaman=datetime.now()+timedelta(hours=vaxt)
# formatli_vaxt=zaman.strftime("%d.%m.%Y")
# print(f'niva masini bu {formatli_vaxt} tarixde yupiter planetine catacaq')


# # #######################
# cumle = 'Saat 17:00 , 04.06.2022 tarixində dərsə gəlin'
# format_data="Saat %H:%M , %d.%m.%Y tarixində dərsə gəlin"
# date=datetime.strptime(cumle, format_data)
# print(f'Saat {date} tarixinde derse gelin')
# ##################


#################
# importing the required module
# import timeit

# code snippet to be executed only once
# mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
# mycode='''
# text = list('I live in New York')
# text.reverse()
# print(''.join(text))

# '''
# print(timeit.timeit(mycode,number=1))


# text_line = 'I live in New York'
# textreverse = text_line[::-1]
# vowels = 'aeiuo'
# result = ''
# for char in textreverse:
#     if char not in vowels:
#         result += char
# print(result)


# print(timeit.timeit(lambda:result,number=1))

# text_line = 'I live in New York'
# textreverse = text_line[::-1]
# vowels = 'aeiuo'
# result = ''
# for char in textreverse:
#     if char not in vowels:
#         result += char
# print(result)

# text = list('I live in New York')
# text.reverse()
# print(''.join(text))
# import random
# import math
# random_list=[random.uniform(-1000,1000) for i in range(1000)]
# def mylist_1(liste):
#     liste.sort()
#     return liste.pop()
# def mylist_2(lst):
#     max_element = math.inf
#     for num in lst:
#         if num > max_element:
#             max_element = num
#             # if num == math.inf:
#             # break
#     return max_element  
# high1=mylist_1(random_list)
# high2=mylist_2(random_list)
# # print(high)
# print(timeit.timeit(lambda:mylist_1(random_list),number=1))
# print(timeit.timeit(lambda:mylist_2(random_list),number=1))


# import os
# # os.rename('yeni dunya','heyat')
# # os.removedirs('dunya')
# os.listdir('PYHTON')

# os.mkdir('yenidizin')
# os.mkdir('/home/istihza/Desktop/yenidizin')
# os.mkdir(r'C:\Documents and Settings\fozgul\yenidizin')
# os.rename('list.txt','aygin')

# os.remove('asu.txt')
# os.rmdir('heyat')
# os.makedirs('Pyhton/General/Pyhton')
# os.mkdir('dersler')
# os.getcwd()
# os.chdir(r'C:\Users\Lenovo\OneDrive\Desktop\html css\image\image\slick-1.8.1')
# print(os.listdir(r"C:\Users\Lenovo\OneDrive\Desktop\compar\css"))


# os.rename('main.html','C:/Users/Lenovo/OneDrive/Desktop/pyhton/yenidizin/main.html')
# os.rename('list.txt','C:/Users/Lenovo/OneDrive/Desktop/pyhton/yenidizin/list.txt')
# os.remove('yenidizin/list.txt')
# os.replace('yenidizin/index.html','main.html')
# os.rename('yenidizin/main.html','C:/Users/Lenovo/OneDrive/Desktop/pyhton/Pyhton/yenidizin/main.html')
# os.rename('yenidizin/main.html','C:/Users/Lenovo/OneDrive/Desktop/pyhton/Pyhton/yenidizin/main.html')
#############
# import shutil

# os.mkdir('dersler')
# os.rename('ders1.txt','C:/Users/Lenovo/OneDrive/Desktop/pyhton/dersler/ders1.txt')
# os.rename('ders2.txt','C:/Users/Lenovo/OneDrive/Desktop/pyhton/dersler/ders2.txt')
# os.remove('dersler/ders1.txt')  
# os.replace('dersler/Pyhton Notlari','Pyhton Notlar')      
# os.rename('Pyhton Notlari','C:/Users/Lenovo/OneDrive/Desktop/pyhton/dersler/Pyhton Notlari')
# os.makedirs('Pyhton/General/Pyhton')
# os.rename('Pyhton Notlar','C:/Users/Lenovo/OneDrive/Desktop/pyhton/Pyhton/Pyhton Notlari')
# shutil.copy("Dersler/Python/General Python/Python Notlari.txt","C:/Users/Lenovo/OneDrive/Desktop/Pyhton Notlari.txt" )
# os.rmdir('dersler')
# os.listdir(os.curdir)



# data = [
#     {"device": "iphone", "price": 3000, "count": None}, 
#     {"device": "samsung", "price": 2500, "count": 3},
#     {"device": "xiaomi", "price": 2100, "count": None},
#     {"device": "nokia", "price": 1800, "count": 4}
# ]   

# total=0
# for item in data:
#     if item["count"] is not None:
#         total+=item["price"] * item["count"]
        
# print(total)

# import time
# def geri_sayim(saniye):
#     while saniye > 0:
#         print(saniye)
#         time.sleep(1)
#         saniye-=1
#     print('vaxt tamamlandi')
# geri_sayim(10)

# class Weapon:
#     metal='cobalt'
#     def __init__(self,bullet_count):
#         self.bullet_count=bullet_count

# class Avtomat(Weapon):
#     power=20

# class Snayper(Weapon):
#     power=30

# class Solider(Weapon):
#     health=100
#     def __init__(self, name,weapon):
#         self.name=name
#         self.weapon=weapon

#     def fire(self,enemy):
#         enemy.health-=self.weapon.power
#         self.weapon.bullet_count-=1

#     def __len__(self):
#         return self.weapon.bullet_count

# avm=Snayper(5)
# m4=Avtomat(10)

# orxan=Solider('Orxan',avm)
# behram=Solider('Behram',m4)
# orxan.fire(behram)
# behram.fire(orxan)
# print(behram.health)
# print(orxan.health)
# print(len(orxan))
# print(len(behram))
    
# class Salary:
#     def __init__(self,name,salary) :
#         self.name=name
#         self.__salary=salary
#     # def show(self):
#     #     print('name ',self.name,'salary ',self.__salary)

# emp=Salary('kate',1000)
# print('name ', emp.name , 'salary ',emp._Salary__salary)

# class Protect:
#     def __init__(self):
#         self._protect='Nlp'

# class Member:
#     def __init__(self,name):
#         self.name=name
#         Protect.__init__(self)
#     def shower(self):
#         print('protected member ' ,self._protect)
#         print('asdd',self.name)
# pro=Member('jessa')
# pro.shower()
# print('project',pro._protect)
############################        TASK 1           ##########################################
# def cube(n):
#     return n**3
# nums=[2,3,4,5]
# new_nums=[]
# for num in nums:
#     new_num=cube(num)
#     new_nums.append(new_num)
# print(new_nums)
    




        
# p1={'xp':3976, 'level':3}
# p2={'xp':1123,'level':1}
# p3={'xp':0}
# player_db=[p1,p2,p3]
# for p in player_db:
#     lvl=p.get('level')
#     print(f'level: {lvl}')


# user_input=11
# if user_input % 2==11:
#     err='must be even number of players'
#     # except Exception(err)
# team_a_size=user_input/2
# team_b_size=team_a_size
# print(f'Team a:{team_a_size}players')
# print(f'teamb;{team_b_size}players')





# def fahr_celci(fahr):
#     return((fahr-32)*(5/9))
# temp1=[78,66,67]
# temp2=[]
# for t in range(len(temp1)):
#     temp_celc=fahr_celci(temp1[t])
#     temp2.append(temp_celc)
# print(temp2)

import subprocess
data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
profiles=[i.split(":")[1][1:-1]for i in data if 'all user profile' in i]
print("\n{:<30}|{:<}".format())
for i in profiles:
    results=subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode('utf-8').split('\n')
    results=[b.split(":")[1][1:-1]for b in results if 'key content' in b]

    try:
        print("{:<30}| {:<}".format(i,results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i,""))
        










