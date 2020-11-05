import matplotlib
import matplotlib.pyplot as plt
from random import randint
from random import randint,shuffle
import random
from io import BytesIO
import base64
import requests,json
import numpy as np
from matplotlib import patches
from fractions import  Fraction

class Q_type:
  multichoice="multichoice"
  singlechoice="singlechoice"
  photo="photo"
  shortreply="shortreply"

def send(info):
  pass

# def send(info):
#   url="https://thebotserver.herokuapp.com/api/broadcast/64"
#   #url="https://vocab.ngrok.io/api/broadcast/64"
#   payload={
#       #"message":{"photo":info},
#       "message":info,
#   }
#   headers={
#       "Content-Type":'application/json'
#   }
#   r=requests.request("POST",url,headers=headers,data=json.dumps(payload))
#   print(r)

#@title Q1(2019FebMarch)
def Q1():
  q = """ 1   A mathematics lessons starts at {time}.
      The lesson lasts for {duration} minutes.
      Work out the time that the lesson ends.
      
      
      
      
      
                                  ....................... [1] 
      CA : {jwpn}"""

  duration = random.randint(10,120)
  a = random.randint(8,15)
  b = random.randint(00,59)
  time = str(a)+str(b)
  if a < 10 or b < 10:
    print (str(a).zfill(2))
    print (str(b).zfill(2))
    time = str(a).zfill(2) + str(b).zfill(2)
  jwpn = int(time)+duration
  if jwpn % 1000 == jwpn:
    jwpn = str(0) + str(jwpn)
  print(jwpn)
  ans = {"q": q, "time": time, "duration":duration, 'jwpn':jwpn}

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
          horizontalalignment='left',
          verticalalignment='center',
          fontsize=15, color='black',
          transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
Q1()

#@title Q2(2019FebMarch)
def Q2():
  q = """
2    The probability that it will 
      {cond} tomorrow is {r}.
      Work out the probability that it will 
      {cond2} tomorrow.
      A) {o1}
      B) {o2}
      C) {o3}
      D) {o4}
      E) {o5}
                                 
    CA : {jwpn}"""
  r = round(random.uniform(0.0,1.0),2)
  hujantakhujan = ["be sunny","not be sunny"]
  cond = random.choice(hujantakhujan)
  if cond == "be sunny":
    cond2 = hujantakhujan[1]
  else :
    cond2 = hujantakhujan[0]
  jwpn = round(1 - r,2)

  wAns = set()
  arr = []
  while len(wAns) < 4 :
    salah = round(random.uniform(0,1.0),2)
    if (salah * 100)%10 ==0:
      salah = str(salah) + str(0)
    if salah != jwpn:
      wAns.add(salah)
  for j in wAns :
    arr.append(j)
  
  print(wAns)
  print(arr)
  print(jwpn)
  
  o1 = arr[2]
  o2 = arr[0]
  o3 = arr[1]
  o4 = jwpn
  o5 = arr[3]
  
  
  ans = {"q" : q, "r":r, "cond":cond, "cond2":cond2, 'jwpn':jwpn,"o1":o1,"o2":o2,"o3":o3,"o4":o4,"o5":o5}


  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
          horizontalalignment='left',
          verticalalignment='center',
          fontsize=15, color='black',
          transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
Q2()
# send(Q2())

#@title Q3(2019FebMarch)
from matplotlib.patches import Ellipse
def Q3():
  q = """ 
  3. Complete the statement.
      Angle ...................... is a {pilihangle}. 
      CA : {ca}
    """
  angle = ['acute angle','right angle','reflex angle', 'obtuse angle']
  pilihangle = random.choice(angle)
  font = {'family': 'serif',
          'color':  'black',
          'weight': 'normal',
          'size': 14,
          }
  if pilihangle == angle[0]:
    ca = 'B'
  elif pilihangle == angle[1]:
    ca = 'D'
  elif pilihangle == angle[2]:
    ca = 'C'
  elif pilihangle == angle[3]:
    ca = 'A'

  ans={"q":q, 'pilihangle':pilihangle, 'ca':ca}
  #Create figure for question
  fig = plt.figure(figsize=(6,6))
  ax = fig.add_axes([0,0,1,1])
  plt.axis('off')

  ax.text(0.1,0.25, ans['q'].format(**ans),
          horizontalalignment= 'left',
          verticalalignment= 'center',
          fontsize = 14, color='black',
          transform=ax.transAxes)

  #The drawing is added to the question figure via subplot.
  fig2 = fig.add_subplot(111)
  # plt.subplots_adjust(right = 0.5, bottom = 0.3)

  #Line is generated from one point to another accoding to its coordinates
  x, y = [0,10,14],[0,0,10] 
  a,b = [27,13,20],[0,0,-15]
  c,d = [25,33,47],[10,0,0]
  e,f = [52,69,69], [0,0,-15]
  plt.plot(x, y, color='black')
  plt.plot(a, b, color='black')
  plt.plot(c, d, color='black')
  plt.plot(e, f, color='black')
  angle_plot = patches.Arc([0.32,0.43], 0.3, 0.3,70, 0, 70, color='black', label = str(45)+u"\u00b0")
  ax.add_patch(angle_plot)
  plt.text(7.1,1,'A',fontdict=font)
  plt.text(16,-4.2,'B',fontdict=font)
  plt.text(32.5,1,'C',fontdict=font)
  plt.text(65,-4,'D',fontdict=font,)

  plt.axis('scaled')

  #Erase off to see how subplot is added to the figure
  plt.axis('off')
Q3()

#@title Q3(2019FebMarch) version2 :)
from matplotlib.patches import Ellipse
def Q3():
  q = """ 
  3. Complete the statement.
      Angle ...................... is a {pilihangle}. 
      CA : {ca}
    """
  angle = ['acute angle','right angle','reflex angle', 'obtuse angle']
  pilihangle = random.choice(angle)
  font = {'family': 'serif',
          'color':  'black',
          'weight': 'normal',
          'size': 14,
          }
  if pilihangle == angle[0]:
    ca = 'B'
  elif pilihangle == angle[1]:
    ca = 'D'
  elif pilihangle == angle[2]:
    ca = 'C'
  elif pilihangle == angle[3]:
    ca = 'A'

  ans={"q":q, 'pilihangle':pilihangle, 'ca':ca}
  #Create figure for question
  fig = plt.figure(figsize=(6,6))
  ax = fig.add_axes([0,0,1,1])
  plt.axis('on')

  ax.text(0.1,0.25, ans['q'].format(**ans),
          horizontalalignment= 'left',
          verticalalignment= 'center',
          fontsize = 14, color='black',
          transform=ax.transAxes)

  #The drawing is added to the question figure via subplot.
  fig2 = fig.add_subplot(2,2,(1,2))
  # plt.subplots_adjust(right = 0.5, bottom = 0.3)

  #Line is generated from one point to another accoding to its coordinates
  x, y = [0,10,14],[0,0,10] 
  a,b = [27,13,20],[0,0,-15]
  c,d = [25,33,47],[10,0,0]
  e,f = [52,69,69], [0,0,-15]
  plt.plot(x, y, color='black')
  plt.plot(a, b, color='black')
  plt.plot(c, d, color='black')
  plt.plot(e, f, color='black')
  angle_plot = patches.Arc([0.25,0.75], 0.12, 0.1,60, 0, 128, color='black', label = str(45)+u"\u00b0")
  #first param koordinat bucu a
  #second and third sama  
  # fourth angle permulaan
  #fifth =0
  # sixth = bape from start kepada line lagi satu
  #size dia ikut axis luar tu and aku rasa dia hantar to tele pun ikiut axis grid yg ada tu
  #tapi kurang cantik sebab kalau nak cantik kena setting kedudukan sume balik
  ax.add_patch(angle_plot)
  angle_plot2 = patches.Arc([0.3,0.75], 0.17, 0.17,280, 0,76, color='black', label = str(45)+u"\u00b0")
  ax.add_patch(angle_plot2)
  angle_plot3 = patches.Arc([0.5,0.75], 0.1, 0.1,140, 0, 215, color='black', label = str(45)+u"\u00b0")
  ax.add_patch(angle_plot3)
  angle_plot4 = patches.Arc([0.85,0.75], 0.17, 0.17,187, 0, 95, color='black', label = str(45)+u"\u00b0")
  ax.add_patch(angle_plot4)
  plt.text(7.1,1,'A',fontdict=font)
  plt.text(16,-4.2,'B',fontdict=font)
  plt.text(32.5,1,'C',fontdict=font)
  plt.text(65,-4,'D',fontdict=font,)

  plt.axis('off')

  #Erase off to see how subplot is added to the figure
  plt.axis('off')
Q3()

#@title Q4(2019FebMarch)
def Q4():

  q = """
  
4   The temperature at {time1} is {temp1}{symbol}.
     This temperature is {temp2}{symbol} higher 
     than the temperature at {time2}.
    Find the temperature at {time2}.
    A) {o1}{symbol}
    B) {o2}{symbol}
    C) {o3}{symbol}
    D) {o4}{symbol}
    E) {o5}{symbol}
    CA = {ca}{symbol}
                                                                     ..................... [1]"""
  temp1 = random.randint(1, 50)
  temp2 = random.randint(5,20)
  a = random.randint(00,24)
  b = random.randint(00,59)
  c = random.randint(00,24)
  d = random.randint(00,59)
  time1 = str(a)+str(b)
  time2 = str(c)+str(d)
  if a < 10 or b < 10 or c < 10 or d < 10:
    time1 = str(a).zfill(2) + str(b).zfill(2) 
    time2 = str(c).zfill(2) + str(d).zfill(2)
  symbol = '$^\circ$C'
  ca = temp1 - temp2 

  arr = set()
  while len(arr)<4 :
    rand = random.randrange(-5,50)
    if rand!=ca:
      arr.add(rand)
  newarr = []
  for j in arr:
    newarr.append(j)
  newarr.append(ca)
  print(arr)
  print(newarr)

  shuffle(newarr)
  o1 = newarr[0]
  o2 = newarr[1]
  o3 = newarr[2]
  o4 = newarr[3]
  o5 = newarr[4]

  

  ans = {"q":q, "time1":time1, "time2":time2, "temp1":temp1, "temp2":temp2, 'symbol':symbol, 'ca':ca, "o1":o1,"o2":o2,"o3":o3,"o4":o4,"o5":o5}
  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
          horizontalalignment='left',
          verticalalignment='center',
          fontsize=15, color='black',
          transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
Q4()
# send(Q4())

#@title Q5(2019FebMarch)
def Q5(name):
  q = """
  
5  {n} swims {r} lengths of a swimming pool 
    to raise money for charity.
    She recieves ${money} for each length she swims.
    Calculate how much money 
    {n} raised for charity.
A) ${o1}
B) ${o2}
C) ${o3}
D) ${o4}
E) ${o5}
CA : ${ca}
  """
  n = random.choice(name)
  r = random.randint(10,50)
  money = random.randint(5,20)
  ca = r * money
  print(ca)

  o1 = r * money + 1
  o2 = r * money - 2
  o3 = r * money 
  o4 = r * money - 5
  o5 = r * money +3


  ans = {"q":q, "n":n, "r":r, "money":money, "o1":o1,"o2":o2,"o3":o3,"o4":o4,"o5":o5, 'ca':ca}

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
          horizontalalignment='left',
          verticalalignment='center',
          fontsize=15, color='black',
          transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
name = ["Alia", "Ain", "Stephanie", "Afiqah", "Lizie","Sally"]
Q5(name)
# send(Q5(name))

#@title Q6(2019FebMarch)
def Q6():
  q = """
  
  6    A student measures the angles in a triangle 
        as {a1}°,{a2}° and {a3}°.
        Explain why the student is incorrect.
                                      .................... [1]
    CA : Interior angles of a triangle is 180{ca}
                                                                        
  """
  a1 = 0
  a2 = 0
  a3 = 0

  while (a1 + a2 + a3) <  180:

    a1 = random.randint(30,180)
    a2 = random.randint(30,180) 
    a3 = random.randint(30,180) 
  ca = '$^\circ$'
  ans = {"q":q, "a1":a1, "a2":a2, "a3":a3, 'ca':ca}

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
          horizontalalignment='left',
          verticalalignment='center',
          fontsize=15, color='black',
          transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
Q6()

#@title Q7(2019FebMarch)
import numpy as np
def Q7():

  c="""2. Shade two more squares so that this shape has 
  rotational symmetry of order 2 
    
                                                                  
                                                                                           
    """

  ans={"q":c}


  N = 18
  data = np.ones((N, N)) * np.nan
  data[6:12,2:6]=1
  data[6:12,7:12]=1
  data[6:12,13:17]=1
  fig, ax = plt.subplots(1, 1, tight_layout=True)
  my_cmap = matplotlib.colors.ListedColormap(['0.75'])
  my_cmap.set_bad(color='w', alpha=0)

  for x in range(N + 1):
      ax.axhline(x, lw=2, color='k', zorder=5)
      ax.axvline(x, lw=2, color='k', zorder=5)
  ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)
  print (type(ax))
  ax.text(0, 1, ans['q'].format(**ans), horizontalalignment='left',verticalalignment='center', transform=ax.transAxes)
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I=base64.encodebytes(image.getvalue())
  return {"photo": I.decode(), "Type":Q_type.photo}
Q7()

#@title Q7(2019FebMarch) version2 :)
import numpy as np
def Q7():

  c="""7.Write down the mathematical name of the solid
    
                                                                  
                                                                                           
    """

  ans={"q":c}

  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  plt.axis('on')

  ax.text(0.05, 0.15, ans['q'].format(**ans),
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=10, color='black',
        transform=ax.transAxes)
  fig2 = fig.add_subplot(1, 1, 1)
  #buat grid
  for x in range(20):
    plt.hlines(x,0,20, lw=2, color='0.8', zorder=2,linestyles="solid")
    plt.vlines(x,0,20, lw=2, color='0.8', zorder=2,linestyles="solid")
  plt.vlines(0,0,20, lw=2, color='k', zorder=5,linestyles="solid")
  plt.subplots_adjust(bottom=0.4,top=0.97,left=0.1,right=0.6)
  #square tgh
  plt.plot([1,17,17,1,1], [6,6,13,13,6],color="black")
  plt.plot([12,12,6,6], [6,13,13,6],color="black")
  #triangle atas
  plt.plot([12,9,6], [13,17,13],color="black")
  #triangle bawah
  plt.plot([12,9,6], [6,2,6],color="black")
  plt.ylim(0, 20)
  plt.xlim(0, 20)
  ax.text(0, 1, ans['q'].format(**ans), horizontalalignment='left',verticalalignment='center', transform=ax.transAxes)
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I=base64.encodebytes(image.getvalue())
  return {"photo": I.decode(), "Type":Q_type.photo}
Q7()

#@title Q8a(2019FebMarch)

def Q81():
  q = """
  
8   (a) Write {r} correct to 
          {ro} significant figures.
        A. {o1}
        B. {o2}
        C. {o3}
        D. {o4}
        E. {o5}
  CA : {ca}"""

  r = round(random.uniform(0,1),6)
  ro = random.randint(2,4)
  ca = round(r,ro)
  # if (ca*100)%10 == 0:
  #   ca = round(r,ro) + str("0")
  print(ca)

  # huhu = random.randint(1,10)
  # uniq = set()
  # hm = 0
  # while len(uniq) < 4:
  #   hm = round(r,--ro)
  #   if hm!=ca :
  #     uniq.add(hm)
  # print(uniq)
  new = set()
  for i in range(5):
    baru = round(r,i+1)
    if baru != ca:
      new.add(baru)
  newarr = []
  for m in new:
    newarr.append(m)
  newarr.append(ca)
  print(newarr)

  shuffle(newarr)
  o1 = newarr[0]
  o2 = newarr[1]
  o3 = newarr[2]
  o4 = newarr[3]
  o5 = newarr[4]

  ans = {"q":q, "r":r, "ro":ro, 'ca':ca, 'o1':o1 ,'o2':o2,'o3':o3,'o4':o4, 'o5':o5}

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
          horizontalalignment='left',
          verticalalignment='center',
          fontsize=15, color='black',
          transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
# send(Q81())

#@title Q8b(2019FebMarch)

def Q82():
  q = """    
      (b) {r} in standard form.
            
        A. {o1}
        B. {o2}
        C. {o3}
        D. {o4}
        E. {o5}
                
    
    
    CA: {pnjg}
              """

  r = random.randint(100,300)
  ran = random.randint(2,7)
  
  b = r
  for i in range(ran):
    r = str(r) + str(0)
  pnjg = str(b) + str("x10") + r'$^{'+str(ran)+'}$'

  print(r)
  print(ran)
  print(b)

  new = set()
  ###################
  while len(new)<4:
    rendem = random.randint(2,7)
    if rendem != ran:
      new.add(rendem)
  ####################
  Sonew = []
  o = 0
  for k in new:
    Sonew.append(k)
  Sonew.append(ran)
  print(Sonew)
  ####################
  random.shuffle(Sonew)
  o1 = str(b) + str("x10") + r'$^{'+str(Sonew[0])+'}$'
  o2 = str(b) + str("x10") + r'$^{'+str(Sonew[1])+'}$'
  o3 = str(b) + str("x10") + r'$^{'+str(Sonew[2])+'}$'
  o4 = str(b) + str("x10") + r'$^{'+str(Sonew[3])+'}$'
  o5 = str(b) + str("x10") + r'$^{'+str(Sonew[4])+'}$'
  print(o1)
  print(o2)
  print(o3)
  print(o4)
  print(o5)
  
  ans = {"q":q, "b":b, 'pnjg':pnjg,'r':r,"o1":o1,"o2":o2,"o3":o3,"o4":o4,"o5":o5}

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
          horizontalalignment='left',
          verticalalignment='center',
          fontsize=15, color='black',
          transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}

# send(Q82())

#@title Q9(2019FebMarch)
def Q9():
  c="""7.Write down the mathematical name of the solid
    
                                                                  
                                                                                           
    """

  ans={"q":c}

  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  plt.axis('on')

  ax.text(0.05, 0.15, ans['q'].format(**ans),
        horizontalalignment='left',
        verticalalignment='center',
        fontsize=10, color='black',
        transform=ax.transAxes)
  
  #start
  fig2 = fig.add_subplot(1, 1, 1)

  #buat grid
  for x in range(20):
    plt.hlines(x,0,20, lw=2, color='0.8', zorder=2,linestyles="solid")
    plt.vlines(x,0,20, lw=2, color='0.8', zorder=2,linestyles="solid")
  plt.vlines(0,0,20, lw=2, color='k', zorder=5,linestyles="solid")
  plt.subplots_adjust(bottom=0.4,top=0.97,left=0.1,right=0.6)
#########################
  plt.plot([2,13,18,15,11,8,2], [11,11,13,17,13.5,17,11],color="black")
  line = plt.Line2D((0, 20), (10, 10), lw=2.5)
  plt.gca().add_line(line)

  plt.ylim(0, 20)
  plt.xlim(0, 20)
  ax.text(0, 1, ans['q'].format(**ans), horizontalalignment='left',verticalalignment='center', transform=ax.transAxes)
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I=base64.encodebytes(image.getvalue())
  return {"photo": I.decode(), "Type":Q_type.photo}
Q9()

#@title Q10(2019FebMarch)
def Q10():
  q = """10   Write down the {n} factors of {num}.
  
    
  
  
        CA : {ca}                                               """

  num = random.randint(1,13)
  print(num)
  facNum = []
  for i in range(1,100):
    if num%i== 0:
      facNum.append(i)
  uniq = set(facNum)
  new  = []
  for m in uniq :
    new.append(m)
  new.sort()
  ca = new
  n = len(uniq)
  print(n)
  ####################WRONGANS###############

   

  ans = {"q":q, "n":n, "num":num,'ca':ca}

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
          horizontalalignment='left',
          verticalalignment='center',
          fontsize=15, color='black',
          transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
send(Q10())

#@title Q11(2019FebMarch)
def Q11():
  q = """
  
  11  {e} = {num1}    {f} = {num2}
      
      Write as a single vector
      (a) {rendem}{manamana}
        
          
      
      (b) {f} {op} {e}
          
        CA : {ca1} , {ca2}
      """
  e = r'$\mathbf{e}$'
  f = r'$\mathbf{f}$'
  ef = [e,f]
  manamana = random.choice(ef)
  ope = ['+','-']
  op = random.choice(ope)
  rendem = random.randint(2,10)
  n1 = random.randint(-10,11) 
  n2 = random.randint(-10,11)
  n3 = random.randint(-10,11) 
  n4 = random.randint(-10,11) 

  num1 = r'$\binom{'+str(n1)+'}{'+str(n2)+'}$'
  num2 = r'$\binom{'+str(n3)+'}{'+str(n4)+'}$'

  ca1 = 0
  ca2 = 0
  if manamana == ef[0]:
    huhu = rendem * n1
    huhu2 = rendem * n2
    ca1 = r'$\binom{'+str(huhu)+'}{'+str(huhu2)+'}$'
  elif manamana == ef[1]:
    huhu = rendem * n3
    huhu2 = rendem * n4
    ca1 = r'$\binom{'+str(huhu)+'}{'+str(huhu2)+'}$'
  if op == ope[0]:
    tambahup = n1 + n3
    tambahd = n2 + n4
    ca2 = r'$\binom{'+str(tambahup)+'}{'+str(tambahd)+'}$'
  else :
    tolakup = n1 - n3
    tolakd = n2 - n4
    ca2 = r'$\binom{'+str(tolakup)+'}{'+str(tolakd)+'}$'
  ans = {"q":q,"num1":num1, 'num2':num2,  'e':e, 'f':f, 'rendem':rendem, 'op':op, 'manamana':manamana,'ca1':ca1, 'ca2':ca2}

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
          horizontalalignment='left',
          verticalalignment='center',
          fontsize=15, color='black',
          transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
send(Q11())

#@title Q12a(2019FebMarch)
import math
import random
import fractions
import string
def Q12a():
  q = """12    Simplify.
        (a)   ({a}{a1}){a2}
        A. {o1}
        B. {o2}
        C. {o3}
        D. {o4}
        CA : {ca1}
        
        """
  
        
  alp = string.ascii_lowercase
  a = random.choice(alp)
  b = random.choice(alp)
  f1 = random.randint(2,10)
  f2 = random.randint(2,10)
  f3 = random.randint(2,10)
  f4 = random.randint(-5,-1)
  a1 = r'$^{'+str(f1)+'}$'
  a2 = r'$^{'+str(f2)+'}$'
  a3 = r'$^{'+str(f3)+'}$'
  a4 = r'$^{'+str(f4)+'}$'
  operator =  u"\u00F7"

  o1 = str(a) + r'$^{'+str(f1 * f2)+'}$'
  o2 = str(a) + r'$^{'+str(f1 + f2)+'}$'
  o3 = str(a) + str(a1) + str(u" \u00D7 ") + str(a) + str(r'$^{'+str(f2 + 1)+'}$') 
  o4 = str(a) + r'$^{'+str("-")+str(f1 + f2)+'}$'
  ca1 = o1


  o5 = str(b) + r'$^{'+str(f3 * f4)+'}$'
  o6 = str(b) + r'$^{'+str(round(f3 / f4,1))+'}$'
  o7 = str(b) + r'$^{'+str(f3 - f4)+'}$'
  o8 = str(b) + r'$^{'+str(f3 - (f4+2))+'}$'

  ca2 = str(b) + r'$^{'+str(f3 - f4)+'}$'
  ans = {"q":q, "a1":a1, "a2":a2, "a3":a3,'a4':a4, "b":b, "operator":operator, "a":a, 'o1':o1 ,'o2':o2,'o3':o3,'o4':o4, 'ca1':ca1, }

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
      horizontalalignment='left',
      verticalalignment='center',
      fontsize=15, color='black',
      transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
send(Q12a())
# Q12a()

#@title Q12b(2019FebMarch)
import math
import random
import fractions
import string
def Q12b():
  q = """
        (b)   {b}{a3} {operator} {b}{a4} 
        
        A. {o5}
        B. {o6}
        C. {o7}
        D. {o8}
        
        CA: {ca2}"""
  alp = string.ascii_lowercase
  a = random.choice(alp)
  b = random.choice(alp)
  f1 = random.randint(2,10)
  f2 = random.randint(2,10)
  f3 = random.randint(2,10)
  f4 = random.randint(-5,-1)
  a1 = r'$^{'+str(f1)+'}$'
  a2 = r'$^{'+str(f2)+'}$'
  a3 = r'$^{'+str(f3)+'}$'
  a4 = r'$^{'+str(f4)+'}$'
  operator =  u"\u00F7"
  o5 = str(b) + r'$^{'+str(f3 * f4)+'}$'
  o6 = str(b) + r'$^{'+str(round(f3 / f4,1))+'}$'
  o7 = str(b) + r'$^{'+str(f3 - f4)+'}$'
  o8 = str(b) + r'$^{'+str(f3 - (f4+2))+'}$'

  ca2 = str(b) + r'$^{'+str(f3 - f4)+'}$'
  ans = {"q":q, "a1":a1, "a2":a2, "a3":a3,'a4':a4, "b":b, "operator":operator, "a":a,'o5':o5,'o6':o6,'o7':o7,'o8':o8, 'ca2':ca2}
  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
      horizontalalignment='left',
      verticalalignment='center',
      fontsize=15, color='black',
      transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
send(Q12b())

#@title Q13(2019FebMarch)
import random
import math
import fractions
def Q13():
  q = """
  13  Without using a calculator, estimate, 
        by rounding each number 
        correct to 1 significant figure,
                {whole}
        A. {o1}
        B. {o2} 
        C. {o3}
        D. {o4}                                    
  
  CA : {ca}
       """ 
  op = ['+','-']
  choose = random.choice(op)
  n = random.randint(1000,5000)
  nn = random.randint(1000,5000)
  nnn= random.randint(1000,5000)

  n1 = n / 10
  n2 = nn / 1000
  n3 = nnn / 1000
  eqn = str (n2)+ choose +str(n3)
  sqrt = r'$\sqrt{'+str(n1)+'}$'
  whole = r'$\frac{\sqrt{'+str(n1)+'}}{'+str (n2)+ choose +str(n3)+'}$'
  a = round(n1,-2)
  b = round(n2,0)
  c = round(n3,0)
  ca = r'$\frac{\sqrt{'+str(a)+'}}{'+str (b)+ choose +str(c)+'}$'

  o1 = r'$\frac{\sqrt{'+str(round(n1,-1))+'}}{'+str (n2)+ choose +str(n3)+'}$'
  o2 = r'$\frac{\sqrt{'+str(n1)+'}}{'+str (n2)+ choose +str(round(n3,1))+'}$'
  o3 = ca
  o4 = r'$\frac{\sqrt{'+str(round(n1,1))+'}}{'+str (round(n2,1))+ choose +str(c)+'}$'

  ans = {"q":q , "n1":n1, "eqn":eqn, 'sqrt':sqrt, 'whole':whole, 'ca':ca, 'o1':o1,'o2':o2,'o3':o3,'o4':o4}

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
      horizontalalignment='left',
      verticalalignment='center',
      fontsize=15, color='black',
      transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}

  

send(Q13())

#@title Q14(2019FebMarch)
import random
def Q14():
  q = """ 
  14    A tourist changes ${a} to euros(€) 
          when the exchange rate is €1 = $1.0697.
          Calculate how many euros he receives.
          
          A. €{o1}
          B. €{o2} 
          C. €{o3}
          D. €{o4} 
          E. €{o5}
        CA : €{ca}
          """

  a = random.randint(10,1000)
  ca = round(a * 1 / 1.0697,2)
 
  new = []
  while len(new) < 4:
    r = round(random.uniform(100,1000),2)
    if r!= ca:
      new.append(r)
  new.append(ca)
  print(new)

  shuffle(new)
  o1 = new[0]
  o2 = new[1]
  o3 = new[2]
  o4 = new[3]
  o5 = new[4]


  ans = {"q":q , "a":a,'ca':ca,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5 }

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
      horizontalalignment='left',
      verticalalignment='center',
      fontsize=15, color='black',
      transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
# Q14()
send(Q14())

#@title Q15a(2019FebMarch)
import random 
def Q15a():
  q = """
  
   15   (a)    Change {num}{length} into {length2}. 
              A. {o1} {length2}
              B. {o2} {length2}
              C. {o3} {length2}
              D. {o4} {length2}
              E. {o5} {length2}
              
              CA : {ca}{length2}         
                       """
  
  num = random.randint(100,1000)
  panjang = ['mm','cm','m','km']
  length = random.choice(panjang)
  length2 = random.choice(panjang)
  ca = 0
  length2 = length 
  while length == length2 :
    length = random.choice(panjang)
  
  a = num/10
  b = num/1000
  c = num/1000000
  d = num*10
  e = num/100
  f = num/100000
  g = num*1000
  h = num*100
  i = num/1000
  j = num*1000000
  k = num*100000
  l = num*1000

  if length == panjang[0] and length2 == panjang[1]:
    ca = a
  elif length == panjang[0] and length2 == panjang[2]:
    ca = b
  elif length == panjang[0] and length2 == panjang[3]:
    ca = c
  elif length == panjang[1] and length2 == panjang[0]:
    ca = d
  elif length == panjang[1] and length2 == panjang[2]:
    ca = e
  elif length == panjang[1] and length2 == panjang[3]:
    ca = f
  elif length == panjang[2] and length2 == panjang[0]:
    ca = g
  elif length == panjang[2] and length2 == panjang[1]:
    ca = h
  elif length == panjang[2] and length2 == panjang[3]:
    ca = i
  elif length == panjang[3] and length2 == panjang[0]:
    ca = j
  elif length == panjang[3] and length2 == panjang[1]:
    ca = k
  elif length == panjang[3] and length2 == panjang[2]:
    ca = l

  new = [a,b,c,d,e,f,g,h,i,j,k,l]
  newarr = set()
  while len(newarr)<4:
    r = random.choice(new)
    if r!=ca:
      newarr.add(r)
  print(newarr)
  baru = []
  for i in newarr:
    baru.append(i)
  print(baru)
  baru.append(ca)
  shuffle(baru)
  o1 = baru[0]
  o2 = baru[1]
  o3 = baru[2]
  o4 = baru[3]
  o5 = baru[4]

  ans = {'q':q , 'num':num, 'length':length , 'length2':length2, 'ca':ca,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5}

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
      horizontalalignment='left',
      verticalalignment='center',
      fontsize=15, color='black',
      transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
# send(Q15a())

#@title Q15b(2019FebMarch)
import random 
def Q15b():
  q = """
  
  (b)    Change {aftdivide} {length}{pow} into {length2}{pow}. 
              A. {o1}
              B. {o2}
              C. {o3}
              D. {o4} 
              E. {o5} 
         CA : {ca} {length2}{pow}
                                        """
  
  num = random.randint(10,100)
  aftdivide = num/10
  panjang = ['mm','cm','m','km']
  randompower = random.randint(2,3)
  pow = r'$^{'+str(randompower)+'}$'
  length = random.choice(panjang)
  length2 = random.choice(panjang)

  ca = 0
  length2 = length 
  while length == length2 :
    length = random.choice(panjang)
  
  a = aftdivide/10
  b = aftdivide/1000
  c = aftdivide/1000000
  d = aftdivide*10
  e = aftdivide/100
  f = aftdivide/100000
  g = aftdivide*1000
  h = aftdivide*100
  i = aftdivide/1000
  j = aftdivide*1000000
  k = aftdivide*100000
  l = aftdivide*1000

  if length == panjang[0] and length2 == panjang[1]:
    ca = a
  elif length == panjang[0] and length2 == panjang[2]:
    ca = b
  elif length == panjang[0] and length2 == panjang[3]:
    ca = c
  elif length == panjang[1] and length2 == panjang[0]:
    ca = d
  elif length == panjang[1] and length2 == panjang[2]:
    ca = e
  elif length == panjang[1] and length2 == panjang[3]:
    ca = f
  elif length == panjang[2] and length2 == panjang[0]:
    ca = g
  elif length == panjang[2] and length2 == panjang[1]:
    ca = h
  elif length == panjang[2] and length2 == panjang[3]:
    ca = i
  elif length == panjang[3] and length2 == panjang[0]:
    ca = j
  elif length == panjang[3] and length2 == panjang[1]:
    ca = k
  elif length == panjang[3] and length2 == panjang[2]:
    ca = l

  new = [a,b,c,d,e,f,g,h,i,j,k,l]
  newarr = set()
  while len(newarr)<4:
    r = random.choice(new)
    if r!=ca:
      newarr.add(r)
  print(newarr)
  baru = []
  for i in newarr:
    baru.append(i)
  print(baru)
  baru.append(ca)
  shuffle(baru)
  o1 = baru[0]
  o2 = baru[1]
  o3 = baru[2]
  o4 = baru[3]
  o5 = baru[4]

  # ans = {'q':q , 'num':num, 'length':length , 'length2':length2, 'ca':ca,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5}


  ans = {'q':q , 'length':length , 'length2':length2, 'aftdivide':aftdivide, 'pow':pow, 'ca':ca,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5}

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
      horizontalalignment='left',
      verticalalignment='center',
      fontsize=15, color='black',
      transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
# send(Q15b())

#@title Q16(2019FebMarch)
def Q16():
  q = """
  
  16   The width, {w} metres, of a room is {num} metres,
        correct to the nearest 10 centimetres.
        Complete this statement about the value of {w}.
        A. {o1} {exp1} {w} {exp2} {a}
        B. {b} {exp1} {w} {exp2} {o2}
        C. {b} {exp1} {w} {exp2} {a}
        D. {o3} {exp1} {w} {exp2} {a}
       CA : {b} {exp1} {w} {exp2} {a}
"""

  w = r'$ \mathcal{w}$'
  firstnum = random.randint(20,100)
  num = firstnum/10
  num2 = random.randint(5,10)
  panjang = ['centimetres','metres','kilometres']
  length = random.choice(panjang)
  length2 = random.choice(panjang)
  if length == length :
    length2 = random.choice(panjang)
  else:
    length2 = length2
  
  exp1 = r'$ \leqslant $'
  exp2 = r'$ \less $'

  a = round(num+(0.1/2),2)
  b = round(num-(0.1/2),2)
  
  o1 = round(num+(0.2/2),2)
  o2 = round(num-(0.1/2),2)
  o3 = round(num+(0.01/2),2)
  ans = {'q':q , 'num':num ,  'w': w, 'exp1':exp1 , 'exp2':exp2, 'a':a,'b':b,'o1':o1,'o2':o2,'o3':o3}

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1])
  plt.axis('off')
  fig.show()

  ax.text(0.1, 0.5, ans['q'].format(**ans),
      horizontalalignment='left',
      verticalalignment='center',
      fontsize=15, color='black',
      transform=ax.transAxes)
  # this is to convert the graph to the text format to send
  image = BytesIO()
  plt.savefig(image, format='png')
  image.seek(0)
  I = base64.encodebytes(image.getvalue())
  return {"photo": I.decode()}
# send(Q16())
# Q16()

# #@title Q17(2019FebMarch)
# import inflect
# def Q17():
#   c="""
  
#   17. Draw the enlargement of the 
#         triangle by scale factor {word}, centre X.
    
                                                                  
                                                                                           
#     """
#   num = random.randint(2,5)
#   tryje = inflect.engine()
#   word = tryje.number_to_words(num)
#   ans={"q":c, 'word':word}

#   fig = plt.figure()
#   ax = fig.add_axes([0,0,1,1])
#   plt.axis('on')

#   ax.text(0.05, 0.15, ans['q'].format(**ans),
#         horizontalalignment='left',
#         verticalalignment='center',
#         fontsize=10, color='black',
#         transform=ax.transAxes)
  
#   #start
#   fig2 = fig.add_subplot(1, 1, 1)

#   #buat grid
#   for x in range(15):
#     plt.hlines(x,0,15, lw=2, color='0.8', zorder=2,linestyles="solid")
#     plt.vlines(x,0,15, lw=2, color='0.8', zorder=2,linestyles="solid")
#   plt.vlines(0,0,15, lw=2, color='k', zorder=5,linestyles="solid")
#   plt.subplots_adjust(bottom=0.4,top=0.97,left=0.1,right=0.6)
#   #triangle tgh
#   plt.plot([3,7,3,3], [3,3,5,3],color="black")
#   #dot
#   plt.plot([4], [4], 'go') 
  
#   ####################### scale x,y ###################
#   plt.ylim(0, 15)
#   plt.xlim(0, 15)
#   ax.text(0, 1, ans['q'].format(**ans), horizontalalignment='left',verticalalignment='center', transform=ax.transAxes)
#   image = BytesIO()
#   plt.savefig(image, format='png')
#   image.seek(0)
#   I=base64.encodebytes(image.getvalue())
#   return {"photo": I.decode(), "Type":Q_type.photo}
# Q17()

# #@title Q18(2019FebMarch)
# import math
# def Q18():
#   q = """
  
# 18   The probability that a sweet made in a factory
#        is the {opt} shape is {prob}.
#        One day, the factory makes {rand} sweets.
#        Calculate the number of sweets that 
#        are expected to be {opt} shape.
#         A. {o1}
#         B. {o2}
#         C. {o3}
#         D. {o4} 
#         E. {o5}
#     CA : {ca}
#                                                                                 .......................... [2] """
#   option = ['correct','wrong']
#   opt = random.choice(option)
#   probrand = random.randint(0000,10000)
#   prob = probrand/10000
#   rand = random.randint(10000,70000)

#   e = prob * rand
#   ca = math.floor(e)
#   print("ca", ca)
  
#   a = round(prob * rand) +3
#   b = round(prob * rand) - 2
#   c = round(prob * rand) + 1
#   d = round(prob * rand) - 7 
#   new = [a,b,c,d]
#   newarr = set()

#   print(round(prob * rand,2))
#   while len(newarr)<4:
#     r = random.choice(new)
#     newarr.add(r)
#   print(newarr)
#   baru = []
#   for i in newarr:
#     baru.append(i)

#   baru.append(ca)
#   print(baru)
#   shuffle(baru)
#   o1 = baru[0]
#   o2 = baru[1]
#   o3 = baru[2]
#   o4 = baru[3]
#   o5 = baru[4]


  
  
#   ans = {'q':q ,'opt':opt ,'prob':prob , 'rand' :rand, 'ca':ca,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5}
#   fig = plt.figure()
#   ax = fig.add_axes([0, 0, 1, 1])
#   plt.axis('off')
#   fig.show()

#   ax.text(0.1, 0.5, ans['q'].format(**ans),
#       horizontalalignment='left',
#       verticalalignment='center',
#       fontsize=15, color='black',
#       transform=ax.transAxes)
#   # this is to convert the graph to the text format to send
#   image = BytesIO()
#   plt.savefig(image, format='png')
#   image.seek(0)
#   I = base64.encodebytes(image.getvalue())
#   return {"photo": I.decode()}
# # send(Q18())
# # Q18()

# #@title Q19(2019FebMarch)
# import string
# def Q19():
#   q = """19   Factorise completely.
#                                     {num1}{ralp} {pow} - {num2}{ralp}
#       {ca}
#                                                                                 ........................ [2] """
  
#   arr2 = []
#   arr3 = []
#   arr5 = []
#   for i in range(100):
#     if i % 2 == 0:
#       arr2.append(i)
#     elif i % 3 == 0:
#       arr3.append(i)
#     elif i % 5 == 0:
#       arr5.append(i)
  
#   # if num1 and num2 in arr2 :
#   #   num1 = random.choice(arr2) 
#   #   num2 = random.choice(arr2) 
#   # elif num1 and num2 in arr3:
#   #   num1 = random.choice(arr3) 
#   #   num2 = random.choice(arr3) 
#   # elif num1 and num2 in arr5:
#   #   num1 = random.choice(arr5) 
#   #   num2 = random.choice(arr5) 
#   # else :
#   #   print("nothing")

#   ca = 0 
#   olalp = string.ascii_lowercase
#   alp = random.choice(olalp)
#   ralp = r'$ \mathcal{'+ str(alp) +'}$'
#   rpow = random.randint(2,5)
#   pow = r'$^{'+str(rpow)+'}$'

#   new = []
#   for i in range(1,100):
#     new.append(i)

#   num1 = random.randint(2,30)
#   num2 = random.randint(2,30)
  
#   for j in new :
#     while num1 and num2 % j == 0:
#       if (num1 % j == 0) and (num2 % j == 0):
#         ca = str(j)+ str(alp)+  str('(')+ (str(int(num1/j))) +str(alp) + str(r'$^{'+str(rpow-1)+'}$') + str(' - ') + (str(int(num2/j))) +  str(')') 
      


#   # if num1 and num2 %5 == 0:
#   #   ca = str(5)+ str(alp)+  str('(')+ (str(int(num1/5))) +str(alp) + str(r'$^{'+str(rpow-1)+'}$') + str(' - ') + (str(int(num1/5))) +  str(')') 
#   # elif num1 and num2 %3 == 0:
#   #   ca = str(3)+ str(alp)+ str('(')+ (str(int(num1/3)))  + str(alp)+ str(r'$^{'+str(rpow-1)+'}$') + str(' - ') + (str(int(num1/3))) + str(')')
#   # elif num1 and num2 %2 == 0:
#   #   ca = str(2)+ str(alp)+  str('(')+ (str(int(num1/2)))  + str(alp)+ str(r'$^{'+str(rpow-1)+'}$') + str(' - ') + (str(int(num1/2))) + str(')')
#   # elif num1 and num2 % num1 == 0:
#   #   ca = str(num1)+ str(alp)+  str('(')+ (str(int(num1/num1)))  + str(alp)+ str(r'$^{'+str(rpow-1)+'}$') + str(' - ') + (str(int(num1/num1))) + str(')')
  
#   ans = {'q':q , 'pow':pow, 'num1':num1 , 'ralp':ralp , 'num2':num2,'ca':ca}

#   fig = plt.figure()
#   ax = fig.add_axes([0, 0, 1, 1])
#   plt.axis('off')
#   fig.show()

#   ax.text(0.1, 0.5, ans['q'].format(**ans),
#       horizontalalignment='left',
#       verticalalignment='center',
#       fontsize=15, color='black',
#       transform=ax.transAxes)
#   # this is to convert the graph to the text format to send
#   image = BytesIO()
#   plt.savefig(image, format='png')
#   image.seek(0)
#   I = base64.encodebytes(image.getvalue())
#   return {"photo": I.decode()}
# Q19()

# #@title Q19(2019FebMarch) version 2 :)
# import string
# def Q19():
#   q = """19   Factorise completely.
#                                     {num1}{ralp} {pow} - {num2}{ralp}
#       CA : {ca}
#                                                                                 """
#   a=random.randint(2,10)
#   b=a
#   while (b==a):
#     b=random.randint(2,10)
#   fract=Fraction(a,b)
#   times=random.randint(2,5)
#   num1=fract.numerator*times
#   num2=fract.denominator*times
#   olalp = string.ascii_lowercase
#   alp = random.choice(olalp)
#   ralp = r'$ \mathcal{'+ str(alp) +'}$'
#   rpow = random.randint(2,5)
#   pow = r'$^{'+str(rpow)+'}$'
#   if (fract.numerator==1):
#     a1=""
#   else:
#     a1=str(fract.numerator)
#     if (fract.denominator==1):
#       a2=""
#     else:
#       a2=str(fract.denominator)
#   ca=str(times)+alp+r'('+a1+alp+"$^{"+a2+"}-"+str(b)+")$"



#   # if num1 and num2 %5 == 0:
#   #   ca = str(5)+ str(alp)+  str('(')+ (str(int(num1/5))) +str(alp) + str(r'$^{'+str(rpow-1)+'}$') + str(' - ') + (str(int(num1/5))) +  str(')') 
#   # elif num1 and num2 %3 == 0:
#   #   ca = str(3)+ str(alp)+ str('(')+ (str(int(num1/3)))  + str(alp)+ str(r'$^{'+str(rpow-1)+'}$') + str(' - ') + (str(int(num1/3))) + str(')')
#   # elif num1 and num2 %2 == 0:
#   #   ca = str(2)+ str(alp)+  str('(')+ (str(int(num1/2)))  + str(alp)+ str(r'$^{'+str(rpow-1)+'}$') + str(' - ') + (str(int(num1/2))) + str(')')
#   # elif num1 and num2 % num1 == 0:
#   #   ca = str(num1)+ str(alp)+  str('(')+ (str(int(num1/num1)))  + str(alp)+ str(r'$^{'+str(rpow-1)+'}$') + str(' - ') + (str(int(num1/num1))) + str(')')
  
#   ans = {'q':q , 'pow':pow, 'num1':num1 , 'ralp':ralp , 'num2':num2,'ca':ca}

#   fig = plt.figure()
#   ax = fig.add_axes([0, 0, 1, 1])
#   plt.axis('off')
#   fig.show()

#   ax.text(0.1, 0.5, ans['q'].format(**ans),
#       horizontalalignment='left',
#       verticalalignment='center',
#       fontsize=15, color='black',
#       transform=ax.transAxes)
#   # this is to convert the graph to the text format to send
#   image = BytesIO()
#   plt.savefig(image, format='png')
#   image.seek(0)
#   I = base64.encodebytes(image.getvalue())
#   return {"photo": I.decode()}
# Q19()

# #@title Q20(2019FebMarch)
# import sympy
# import re

# def solve(eq, var=('x', 'y')):
#     """ Solve a system of simultaneous equation in
#     two variables of the form
#     2*x + 5*y=c1; 3*x - 5*y=c2
#     Example: solve('12*x - 3*y = 21; 9*x  - 18*y=0')
#     Should work for negative constants as well.
#     Example: solve('3*x - 5*y=-11; 12*x + 3*y=48')
#     Returns a two tuple of (x, y) values.
#     NOTE: Won't denegarate to the special case
#     of solving for only one variable.
    
#     """

#     var_re = re.compile(r'(\+|\-)\s*(\d*)\s*\*?\s*(x|y)')
#     const_re = re.compile(r'(\+|\-)\s*(\-?\d+)$')

#     constants, eqns, coeffs, default  = [],[], {'x': [], 'y': []}, {'': '1'}

#     for e in eq.split(';'):
#         eq1 = e.replace("="," - ").strip()
#         if not eq1.startswith('-'):
#             eq1 = '+' + eq1
#         eqns.append(eq1)

#     var_eq1, var_eq2 = map(var_re.findall, eqns)

#     constants = [-1*int(x[0][1]) for x in map(const_re.findall, eqns)]
#     [coeffs[x[2]].append(int((x[0]+ default.get(x[1], x[1])).strip())) for x in (var_eq1 + var_eq2)]
    
#     ycoeff = coeffs['y']
#     xcoeff = coeffs['x']

#     # Adjust equations to take out y and solve for x
#     if ycoeff[0]*ycoeff[1] > 0:
#         ycoeff[1] *= -1
#         xcoeff[0] *= ycoeff[1]
#         constants[0] *= -1*ycoeff[1]        
#     else:
#         xcoeff[0] *= -1*ycoeff[1]
#         constants[0] *= ycoeff[1]
        
#     xcoeff[1] *= ycoeff[0]
#     constants[1] *= -1*ycoeff[0]

#     # Obtain x
#     xval = sum(constants)*1.0/sum(xcoeff)

#     # Now solve for y using value of x
#     z = eval(eqns[0],{'x': xval, 'y': 1j})
#     yval = -z.real*1.0/z.imag

#     return (xval, yval)
# def Q20():
#   q = """
  
#   20            {eqn1}
#                 {eqn2}
#       Ans: x = {x} ; y = {y}
#   """
#   a = random.randint(-14,-10)
#   x1 = random.randint(1,5)
#   y1 = random.randint(1,6)
#   solvedX = x1
#   solvedY = y1
  
#   b = random.randint(12,15)
#   x2 = random.randint(1,5)
#   y2 = random.randint(1,6)
#   solvedX2 = x2
#   solvedY2 = y2

#   if x1 == 1:
#     x1 = ""
#   if x2 == 1:
#     x2 = ""
#   if y1 == 1:
#     y1 = ""
#   if y2 == 1:
#     y2 = ""

#   ca = solve(str(solvedX) + '*x -' + str(solvedY)+'*y =' + str(a) + ';' + str(solvedX2) + '*x +'+str(solvedY2) + '*y = ' + str(b))
#   eqn1 = r'$' + str(x1) + '{x} -' + str(y1) + '{y}$ = ' + str(a)
#   eqn2 = r'$' + str(x2) + '{x} +' + str(y2) + '{y}$ = ' + str(b)
#   ans = {"q":q, "x1":x1, "y1":y1, "x2":x2, "y2":y2, "a":a, "b":b, "eqn1":eqn1, "eqn2":eqn2, "x":round(ca[0],2), "y":round(ca[1],2)}

#   fig = plt.figure()
#   ax = fig.add_axes([0, 0, 1, 1])
#   plt.axis('off')
#   fig.show()

#   ax.text(0.1, 0.5, ans['q'].format(**ans),
#       horizontalalignment='left',
#       verticalalignment='center',
#       fontsize=15, color='black',
#       transform=ax.transAxes)
#   # this is to convert the graph to the text format to send
#   image = BytesIO()
#   plt.savefig(image, format='png')
#   image.seek(0)
#   I = base64.encodebytes(image.getvalue())
#   return {"photo": I.decode()}
# Q20()

# def Q202():
#   q = """20.Factorise completely.
  
            
#                             {x}
#           A) {o1}
#           B) {o2}
#           C) {o3}
#           D) {o4}
#           E) {o5}  
  
#   answer:{answer}
#   """
#   b1=random.randint(2,5)
#   b2=random.randint(1,10)
#   b3=random.randint(1,5)
#   b4=random.randint(1,10)
#   a1=b1*b3
#   a2=b1*b4+b2*b3
#   a3=b2*b4
#   a4=2
#   if b3==1:
#     b3=""

#   answer="("+str(b1)+"x+"+str(b2)+")("+str(b3)+"x+"+str(b4)+")"
#   options=set()
#   options.add(answer)

#   while len(options)<5:
#     options.add("("+str(b1+random.randint(1,5))+"x+"+str(b2+random.randint(1,5))+")("+str(b3+random.randint(1,5))+"x+"+str(b4+random.randint(1,5))+")")
#   options=list(options)
#   shuffle(options)  

#   x=str(a1)+"C"+"$^{"+str(a4)+"}$"+"+"+str(a2)+"C+"+str(a3)
#   ans={"q":q,"x":x,"answer":answer,"o1":options[0],"o2":options[1],"o3":options[2],"o4":options[3],"o5":options[4]}

#   # ans = {'q':q , 'num1': num1, 'num2': num2 , 'num3': num3 , 'num4': num4, 'x':x , 'y':y ,  'result': result, 'result2':result2}
#   fig = plt.figure()
#   ax = fig.add_axes([0, 0, 1, 1])
#   plt.axis('off')
#   fig.show()

#   ax.text(0.1, 0.5, ans['q'].format(**ans),
#       horizontalalignment='left',
#       verticalalignment='center',
#       fontsize=15, color='black',
#       transform=ax.transAxes)
#   # this is to convert the graph to the text format to send
#   image = BytesIO()
#   plt.savefig(image, format='png')
#   image.seek(0)
#   I = base64.encodebytes(image.getvalue())
#   return {"photo": I.decode()}
# Q202()

# def Q21():
#   q = """
  
  
  
  
  
  
  
  
  
  
#   21. Calculate the total surface area of the cuboid.
#   """
#   font = {'family': 'serif',
#           'color':  'black',
#           'weight': 'normal',
#           'size': 14,
#           }
#   fig = plt.figure()
#   ax = fig.add_axes([0,0,1,1]) #add_axes(rect) where rect = [x0, y0, width, height]
#   plt.axis('off')
#   ax.set_ylim([0, 10])   # set the bounds to be 10, 10
#   ax.set_xlim([0, 10])

#   ax.plot([2,8,8,9,9,8],[2,2,5,7,4,2], 'k', linewidth=1)
#   ax.plot([8,2,2],[5,5,2], 'k', linewidth=1)
#   ax.plot([2,3.4,9],[5,7,7], 'k', linewidth=1)

#   ax.text(4.3,1.5,"{num}cm",fontdict=font)
#   ax.text(9,5,"{num2}cm",fontdict=font)
#   ax.text(9,5,"{num2}cm",fontdict=font)
#   ax.text(8.5,3,"str(num)+cm",fontdict=font)
#   ax.text(8.6,0.4,"NOT TO\nSCALE",fontdict=font)
  
#   num = random.randint(10,20)
#   num2 = random.randint(7,10)
#   num3 = random.randint(3,6)

#   ans = {'q':q, 'num':num, 'num2':num2, 'num3':num3}
#   ax.text(0.1, 0.3, ans['q'].format(**ans),
#         horizontalalignment='left',
#         verticalalignment='center',
#         fontsize=12, color='black',
#         transform=ax.transAxes)

#   #this is to convert the graph to the text format to send
#   #plt.show() #show the figure
#   image = BytesIO()
#   plt.savefig(image, format='png')
#   #plt.savefig('image.png')
#   image.seek(0)
#   I=base64.encodebytes(image.getvalue())

# Q21()

# #@title Q22(2019FebMarch)
# import math
# def Q22():
#   q = """
  
# 22   The number of passengers on a train 
#         {change} from {num1} to {num2}.
#         Calculate the percentage {change}.
#       A) {o1}%
#       B) {o2}%
#       C) {o3}%
#       D) {o4}%
#       E) {o5}%
#     CA : {ca}%
#                                                                                 ....................... % [3]
# """
#   op = ['increase','decrease']
#   change = random.choice(op)
#   num1 = 5
#   num2 = 5
#   ca = 0
#   hm = 0
#   while num1 == num2 :
#     if change == op[0]:
#       num1 = random.randint(50,100)
#       while num1 > num2:
#         num2 = random.randint(50,100)
#       hm = ((num2 - num1)/num1) * 100
#       ca = math.floor(hm)
#     elif change == op[1]:
#       num1 = random.randint(50,100)
#       while num1 < num2:
#         num2 = random.randint(50,100)
#       hm = ((num1 - num2)/num1) * 100
#       ca = math.floor(hm)
  
#   new = set()
#   while len(new) < 4:
#     r = random.randint(5,100)
#     if r != ca:
#       new.add(r)
#   newarr = []
#   for j in new:
#     newarr.append(j)
#   newarr.append(ca)
#   shuffle(newarr)

#   print(ca)

#   o1 = newarr[0]
#   o2 = newarr[1]
#   o3 = newarr[2]
#   o4 = newarr[3]
#   o5 = newarr[4]

#   ans = {'q':q , 'num1':num1 , 'num2':num2, 'change':change,'ca':ca, 'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5}
#   fig = plt.figure()
#   ax = fig.add_axes([0, 0, 1, 1])
#   plt.axis('off')
#   fig.show()

#   ax.text(0.1, 0.5, ans['q'].format(**ans),
#       horizontalalignment='left',
#       verticalalignment='center',
#       fontsize=15, color='black',
#       transform=ax.transAxes)
#   # this is to convert the graph to the text format to send
#   image = BytesIO()
#   plt.savefig(image, format='png')
#   image.seek(0)
#   I = base64.encodebytes(image.getvalue())
#   return {"photo": I.decode()}
# # send(Q22())

# def Q23():
#   c="""
  
  
#   23 The diagram shows a quadrilateral 
#         on a 1 cm2 grid.
#   (a) Write down the mathematical name 
#       of this quadrilateral.
    
#   (b) Work out the area of this quadrilateral.
#         Give the units of your answer                                                              
#     """

#   ans={"q":c}

#   fig = plt.figure()
#   ax = fig.add_axes([0,0,1,1])
#   plt.axis('on')

#   ax.text(0.05, 0.15, ans['q'].format(**ans),
#         horizontalalignment='left',
#         verticalalignment='center',
#         fontsize=10, color='black',
#         transform=ax.transAxes)
  
#   #start
#   fig2 = fig.add_subplot(1, 1, 1)

#   #buat grid
#   for x in range(10):
#     plt.hlines(x,0,10, lw=2, color='0.8', zorder=2,linestyles="solid")
#     plt.vlines(x,0,10, lw=2, color='0.8', zorder=2,linestyles="solid")
#   plt.vlines(0,0,10, lw=2, color='k', zorder=5,linestyles="solid")
#   plt.subplots_adjust(bottom=0.4,top=0.97,left=0.1,right=0.6)
#   #triangle tgh
#   plt.plot([1,9,7,3,1], [3,3,7,7,3],color="black")
   

#   ####################### scale x,y ###################
#   plt.ylim(0, 10)
#   plt.xlim(0, 10)
#   ax.text(0, 1, ans['q'].format(**ans), horizontalalignment='left',verticalalignment='center', transform=ax.transAxes)
#   image = BytesIO()
#   plt.savefig(image, format='png')
#   image.seek(0)
#   I=base64.encodebytes(image.getvalue())
#   return {"photo": I.decode(), "Type":Q_type.photo}
# Q23()

# #@title Q24(2019FebMarch)
# import inflect
# import random
# import numpy as np

# def Q24():
#   q = """
  
  
# 24  {wordNum} numbers have a mean of {mean} .
#       {wordMinusOne} of the numbers are {new}.
#       Work out the range of the {wordNum} numbers.
    
#                                                 ............................ [4]
#     CA : range {ca} , missing number : {missing}
                                                                                
#   """
#   tryje = inflect.engine()
#   num = random.randint(3, 6)
#   wordNum = tryje.number_to_words(num).capitalize()
#   numMinusOne = num -1
#   wordMinusOne = tryje.number_to_words(numMinusOne).capitalize()
#   new = []
#   total = 0
#   print("the number is : " , num)
#   for i in range (num):
#       a = random.randint(3,20)
#       new.append(a)
#       # if a not in new: #removeduplicate
#       #     new.append(a)
#   newarr = []
#   for j in new:
#     newarr.append(j)
#   print(new)
#   ca = newarr
#   total = sum(new)
#   mean = round((total/num),2)
  
#   missing = new.pop()
#   totalaftModify = sum(new)
  

#   hilang = set()
#   while len(hilang) < 4:
#     r = random.randint(3,20)
#     if r!=missing:
#       hilang.add(r)
#   baru = []
#   for m in hilang:
#     baru.append(m)

#   print(baru)
#   print("aft modify : ",new)
#   print("total : ",total," mean : ",mean," missing : ",missing, " total aft modify :",totalaftModify)

#   ans = {'q':q, 'wordNum':wordNum , 'mean':mean, 'wordMinusOne': wordMinusOne ,'new':new, 'ca':ca, 'missing':missing}

#   fig = plt.figure()
#   ax = fig.add_axes([0, 0, 1, 1])
#   plt.axis('off')
#   fig.show()

#   ax.text(0.1, 0.5, ans['q'].format(**ans),
#       horizontalalignment='left',
#       verticalalignment='center',
#       fontsize=15, color='black',
#       transform=ax.transAxes)
#   # this is to convert the graph to the text format to send
#   image = BytesIO()
#   plt.savefig(image, format='png')
#   image.seek(0)
#   I = base64.encodebytes(image.getvalue())
#   return {"photo": I.decode()}
# # send(Q24())

# #@title Q25(2019FebMarch)
# from fractions import Fraction
# def Q25():
#   q = """
  
  
# 25   Without using calcuator, 
#        work out {num} {num1} {op} {num2}
#        You must show all your working and 
#        give your answer as a mixed number 
#        in its simplest form.
          
         
#       CA : {ca} , {ca1}
#                                                                             ..........................[4]"""
#   num = random.randint(2,8)
#   bold = r'$\mathbf{'+ str("Without using calculator")+'}$'
#   ###############################
#   a = 1
#   b = 1
#   while a > b or b == a:
#     b = random.randint(1,8)
#   ############################
#   c = 1
#   d = 1
#   while c > d or c == d:
#      d= random.randint(1,8)
#   #############################
#   num1 = r'$\frac{'+ str(a) +'}{'+ str(b) +'}$'
#   op = u"\u00F7"
#   num2 = r'$\frac{'+ str(c) +'}{'+ str(d) +'}$'
#   #############################
#   awal = (b*num)+a
#   satu = awal*d
#   dua = (b * c)
   
  
#   deno = 0
#   tempat = []
#   alif = int(satu/dua)
#   ba = satu%dua
#   tha = dua
#   unser = str(alif) + r'$\frac{'+ str(ba) +'}{'+ str(tha) +'}$'
#   jwpn = r'$\frac{'+ str(satu) +'}{'+ str(dua) +'}$'
#   ca1 = jwpn
#   ca = 0
#   for m in range(2,100):
#     if satu % m == 0 and dua % m == 0:
#       tempat.append(m)
#       deno = int(dua/(max(tempat)))
#       ca = r'$\frac{'+ str(int(satu/(max(tempat)))) +'}{'+ str(deno) +'}$'
#       print(ca)
#     elif len(tempat) == 1:
#       nume = int(satu/(max(tempat)))
#       hm = r'$\frac{'+ str(nume) +'}{'+ str(deno) +'}$'
#       alif = int(nume/deno)
#       ba = nume%deno
#       tha = deno
#       ca = str(alif) + r'$\frac{'+ str(ba) +'}{'+ str(tha) +'}$'
#     else:
#       ca = unser

#   print(tempat)
#   # print(max(tempat))
#   # print(ca)
#   # print(satu)
#   # print(dua)

#   if deno == 1:
#     ca = str(int(satu/(max(tempat))))
  

#   ans = {'q':q , 'num':num , 'num1':num1, 'op':op, 'num2':num2, 'jwpn':jwpn , 'ca':ca, 'ca1':ca1}

#   fig = plt.figure()
#   ax = fig.add_axes([0, 0, 1, 1])
#   plt.axis('off')
#   fig.show()

#   ax.text(0.1, 0.5, ans['q'].format(**ans),
#       horizontalalignment='left',
#       verticalalignment='center',
#       fontsize=15, color='black',
#       transform=ax.transAxes)
#   # this is to convert the graph to the text format to send
#   image = BytesIO()
#   plt.savefig(image, format='png')
#   image.seek(0)
#   I = base64.encodebytes(image.getvalue())
#   return {"photo": I.decode()}
