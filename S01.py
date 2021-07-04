import os
import pickle
import smtplib
from time import sleep
from selenium import webdriver
from email.message import EmailMessage

##--------- browser driver control center ---------------------------- 
def local_salanium():
    chromedriver_path ='S:\project_work\Insta-Bot-master\chromedriver\chromedriver.exe' # Change this to your own chromedriver path!
    global browser
    browser = webdriver.Chrome(executable_path=chromedriver_path)
    browser.get('https://www.vedantu.com')

def heroku_salnum():
    op = webdriver.ChromeOptions()
    op.add_argument('--disable-gpu')
    op.add_argument('--no-sandbox')
    op.add_argument('--disable-dev-sh-usage')
    op.binary_location =os.environ.get('GOOGLE_CHROME_PATH')
    global browser
    browser = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=op)
    browser.get('https://www.vedantu.com')

##--------- browser driver control center ---------------------------- 

def cookies_save(name):
    pickle.dump(browser.get_cookies(),open(f'{name}.pkl','wb'))

def cookies_load(name):
    cookiess=pickle.load(open(f'{name}.pkl','rb'))
    for cooki in cookiess:
        browser.add_cookie(cooki)

def open_sedul():
    sleep(5)
    browser.get('https://www.vedantu.com/my-schedule?view=ALL')
    sleep(5)

def class_lists_fun():
    get_clas=True
    class_list=[]
    next='.nextSibling'
    global tody
    tody=browser.execute_script(f"val=document.getElementsByClassName('ms-fullWidth container')[0].innerText; return val")
    while get_clas==True:
        try:
            s=browser.execute_script(f"valu=document.getElementsByClassName('ms-fullWidth container')[0]{next}.innerText; return valu")
            if len(s)<20 :
                get_clas=False
            else:
                class_list.append(s)
                next=next + '.nextSibling'
        except:
            get_clas=False

    return class_list
    
def mail(body):
    msg = EmailMessage()
    msg['Subject'] = 'Today Vedantu Class Schedule'
    msg['From'] = 'sd.shivam.00@gmail.com'
    msg['To'] = 'sd.shivam.00@gmail.com'
    msg.set_content(body ,subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('sd.shivam.00@gmail.com', "wgukquumhisgyxyt") 
        smtp.send_message(msg)

def mail_html(classes):
    class_html=''' '''
    for lin in classes:
        line=lin.split('\n')
        class_html=class_html + f'''<tr><td>{line[0]}</td><td>{line[-3]}</td><td>{line[-2]}</td></tr>'''
    
    email_html=f'''<body style="padding: 10%;"> <div> <h3>Hi sir,</h3> <div style=" margin: 52px;margin-top: 5px; font-size: inherit; font-family: cursive; " > <div> A very plesant Good Morning Shivam sir </div> <br> <div> 💖 You are ☆Smart☆  ,  You are ☆Amazing☆ <br> 💖 You are ☆Beautiful☆  ,  You are ☆Enough☆ <br>💖 Don't let anyone make you think otherwise.</div> <br> <div>You have <span style=" color: skyblue; font-family: fantasy; font-size: 24px; ">{len(classes)}</span> Class today. </div> </div> <div> <table style="font-family: cursive; font-size: inherit; border: 3px solid whitesmoke; border-radius: 17px; padding: 17px;background-color: aliceblue; "> <tr > <th colspan="2"> <u> <i> {tody}</i></u></th> </tr> <tr > <th>Time</th> <th>Class</th> <th>Teacher</th> </tr> {class_html} </table> </div> </div> </body>'''
    return email_html


# local_salanium()
heroku_salnum()
cookies_load('shivam')
open_sedul()
classes_list= class_lists_fun()
mail_body=mail_html(classes_list)
mail(mail_body)

  