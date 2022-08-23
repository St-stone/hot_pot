from replit import db
import flask
import datetime
from flask import Flask, render_template, request
app = flask.Flask(__name__)
#db["ach"] = {} #for every ach people have  
#db["user_ach"] = {} #for personal ach 
@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST' and "record" in flask.request.form:
    User = request.form.get('sname')
    PASS = request.form.get('spass')
    L = db["Users"].keys()
    ad = db["Users"]
    ach_key = db["ach"]
    ach = db["ach"]
		#print(User)
		#print(PASS)
    win = int(request.form.get('WIN'))
    ach1 = request.form.get('ach1')
    ach2 = request.form.get('ach2')
    ach3 = request.form.get('ach3')
    ach4 = request.form.get('ach4')
    ach5 = request.form.get('ach5')
    ach6 = request.form.get('ach6')
    ach7 = request.form.get('ach7')
    ach8 = request.form.get('ach8')
    ach9 = request.form.get('ach9')
    ach10 = request.form.get('ach10')
    ach11 = request.form.get('ach11')
    ach_list = [
      ach1,ach2,ach3,ach4,ach5,ach6,ach7,ach8,ach9,ach10,ach11
    ]
    if (str(User) in str(L)):
      if (ad[str(User)][0] != str(PASS)):
        return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/">密碼錯誤（點我返回）</a></body></html>'
      else:
        #score = flask.request.form['User_name']
        KEYS = db["rank"].keys()
        rank = db["rank"]
        flag = "f"
        for n in KEYS:
          if (str(n) == str(User)):
            flag = "t"
            if (win > int(rank[str(User)])):
              rank[str(User)] = win
        if (flag == "f"):
          rank[str(User)] = win
        db["rank"] = rank
        #ach here
        flag = "f"
        for n in ach_key:
          if (str(n) == str(User)):
            flag = "t"
            for i in range(11):
              if(str(ach_list[i])=="1" and (i+1)<10 and "a00"+str(i+1) not in str(ach[str(User)])):
                ach[str(User)].append("a00"+str(i+1))
              elif(str(ach_list[i])=="1" and (i+1)>=10 and "a0"+str(i+1) not in str(ach[str(User)])):
                ach[str(User)].append("a0"+str(i+1))
        if (flag == "f"):
          ach[str(User)] = []
          for i in range(11):
            if(str(ach_list[i])=="1" and (i+1)<10 and "a00"+str(i+1) not in str(ach[str(User)])):
              ach[str(User)].append("a00"+str(i+1))
            elif(str(ach_list[i])=="1" and (i+1)>=10 and "a0"+str(i+1) not in str(ach[str(User)])):
              ach[str(User)].append("a0"+str(i+1))
        db["ach"] = ach
        #print(score)

        return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/">上傳成功（點我返回）</a></body></html>'
    else:
      return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/">此帳號無法使用（點我返回）</a></body></html>'
  return flask.render_template('index.html')

@app.route('/creat', methods=['GET','POST'])
def creat():
  if request.method == 'POST' and "send" in flask.request.form:
    User = request.form.get('User_name')
    #key = request.form.get('key')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    L = db["Users"].keys()
    ad = db["Users"]
    if (str(User) in str(L)):
      return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/creat">此使用者名稱無法使用（點我返回）</a></body></html>'
    elif (str(password1) != str(password2)):
      return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/creat">密碼不一致（點我返回）</a></body></html>'
    elif (" " in str(password1) or " " in str(User) or "ㅤ" in str(password1) or "ㅤ" in str(User)):
      return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/creat">不得有任何白空白在帳號與密碼中（點我返回）</a></body></html>'
    elif(len(User)>15 or len(password1)>15):
      return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/creat">帳號與密碼長度不得超過15個字（點我返回）</a></body></html>'
    else:
      ad[str(User)] = [password1]
      db["Users"] = ad
    return '<a href="<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/">註冊成功（點我返回）</a></body></html>'
  return flask.render_template('creat.html')

@app.route('/beta/', methods=['GET', 'POST'])
def beta():
  return flask.render_template('beta.html')

@app.route('/pre/', methods=['GET', 'POST'])
def pre():
  return flask.render_template('pre.html')

@app.route('/check/', methods=['GET', 'POST'])
def check():
  return flask.render_template('check.html')

@app.route('/person_ach/', methods=['GET', 'POST'])
def person_ach():
  return flask.render_template('person_ach.html')

@app.route('/rank/', methods=['GET', 'POST'])
def rank():
  ach = db["user_ach"]
  KEYS = db["rank"].keys()
  DATA = db["rank"]
	#print(KEYS)
  L = db["Users"].keys()
  for i in L:
    fl = 0
    for j in ach.keys():
      if(str(i)==str(j)):
        fl = 1
    if(fl == 0):
      ach[str(i)] = "無"
  for i in KEYS:
    DATA[str(i)] = int(DATA[str(i)])
  print(KEYS)
  sorted_counts = sorted(DATA.items(), key=lambda x: x[1], reverse=True)
  print(sorted_counts)
  q = []
  for s in sorted_counts:
    q.append([s[0],s[1],ach[s[0]]])
  return flask.render_template('rank.html',keys=KEYS,data=DATA,sorted_counts=sorted_counts,ach=q)

@app.route('/log_in/', methods=['GET', 'POST'])
def log_in():
  page = flask.make_response(flask.render_template('log_in.html'))
  expire_date = datetime.datetime.now()
  expire_date = expire_date + datetime.timedelta(days=1)
  ach_list = ["a001","a002","a003","a004","a005","a006","a007","a008","a009","a010","a011"];
  ach_name = [
    "冰冰姐殺手",
    "YAGOO我婆",
    "わためは悪くないよねぇ",
    "どうも、湊あくあです",
    "はあちゃまちゃま",
    "はあと...？",
    "我愛墨西哥粽",
    "我愛冰冰姐",
    "我全都要",
    "墨西哥粽狂熱粉",
    "墨西哥粽小達人"
  ];
  if('Username' in request.cookies and request.cookies.get('Username') != "" and str(request.cookies.get('Username')) in str(db["ach"])):
    have_user = request.cookies.get('Username')
    my_ach = db["ach"][have_user]
    for i in my_ach:
      page.set_cookie(i, "1", expires=expire_date)
  else:
    for i in ach_list:
      page.set_cookie(i, "0", expires=expire_date)
  if request.method == 'POST' and "send" in flask.request.form:
    User = request.form.get('User_name')
    PASS = request.form.get('password1')
    L = db["Users"].keys()
    ad = db["Users"]
    if (str(User) in str(L)):
      if (ad[str(User)][0] != str(PASS)):
        return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/log_in/">密碼錯誤（點我返回）</a></body></html>'
      else:
        page.set_cookie("Username", str(User), expires=expire_date)
    else:
      return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/log_in/">此帳號無法使用（點我返回）</a></body></html>'
  if request.method == 'POST' and "ach_s" in flask.request.form:
    Ach = db["ach"]
    Hach = int(request.form.get('ach'))
    have_user = request.cookies.get('Username')
    if (str(have_user) in str(Ach.keys())):
      User_cookie = Ach[str(have_user)]
      if(str(ach_list[Hach]) in str(User_cookie)):
        a = db["user_ach"]
        a[str(have_user)] = ach_name[Hach]
        db["user_ach"] = a
        return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/log_in/">更新成功（點我返回）</a></body></html>'
      else:
        return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/log_in/">查詢錯誤，您並未擁有此成就（點我返回）</a></body></html>'
    else:
      return '<html><head><meta charset="utf-8"><link href="/static/style.css" rel="stylesheet" type="text/css" /></head><body><a href="https://hotpot.guaichi.repl.co/log_in/">查詢錯誤，您並未擁有此成就（點我返回）</a></body></html>'
  if request.method == 'POST' and "log_out" in flask.request.form:
    page.set_cookie("Username", "", expires=0)
  return page


app.run('0.0.0.0')