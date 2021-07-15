# Schedule Bot
S01 is a bot which send your daily vedantu schedule in your inbox.Now it's time to not miss any session.

Go to your google account then security then app and create a gmail app and copy the password.

### [🔬] Installation
1. Clone the repo
   ```sh
   git clone https://github.com/Sd-Shivam/S01.git
   ```
2. Install Django
   ```sh
   pip install -r requirements.txt
   ```
3. Update the basic setup
   ```sh
   #from the readme file give bello
   ```
 4. Run the Program
   ```sh
   Python S01.py
   ```  


## Basic Custom Details Update
```python
# add all this in 1st line

from selenium import webdriver
from email.message import EmailMessage

# Change to your preferance once only
name='Shivam'
Mail_subject='Today Vedantu Class Schedule'
From_mail='sd.shivam.00@gmail.com'
Reciver_mail='sd.shivam.00@gmail.com'
google_app_pass='wg***********yxyt' 
chromedriver_exe_path='S:\project_work\**\**\chromedriver\chromedriver.exe'
```
## If you using first Time setup
```python
# add all this in last line
# login once to store cookies for auto login

def run_server():
    local_salanium('https://www.vedantu.com/my-schedule?view=ALL')
    # heroku_salnum()
    # py_anywher()
    sleep(40)
    cookies_save(name)
    open_sedul()
    print('i am on duity sir.........')
    classes_list= class_lists_fun()
    mail_body=mail_html(classes_list)
    mail(mail_body)
    print('all done')



```
## If you logined once and have name.pkl file
```python
# replace to first time use code

def run_server():
    local_salanium('https://www.vedantu.com')
    # heroku_salnum()
    # py_anywher()
    cookies_load(name)
    open_sedul()
    print('i am on duity sir.........')
    classes_list= class_lists_fun()
    mail_body=mail_html(classes_list)
    mail(mail_body)
    print('all done')


```

## Add this to auto check 
```python
# add to auto check schedule everymorning
schedule.every().day.at("05:00").do(run_server)

while True:
 schedule.run_pending()
 time.sleep(1)
```

### Contribute

Feel free to contribute.

