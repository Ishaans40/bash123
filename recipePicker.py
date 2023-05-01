import telegram
import tkinter as tk
import datetime
import time
from datetime import datetime, timedelta
from tkinter import *
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw
import sys
import os
import telegram
import pandas as pd
from git import Repo
from tkinter import filedialog

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def gitcommit(billv) :
    repo = Repo('C:/BBSC/rec')
    repo.index.add(['srecord.txt'])
    commitmsz = str("Updated at " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " for " + str(billv))
    repo.index.commit(commitmsz)
    origin = repo.remote(name='origin')
    origin.push()

def cable_window():
    
    def filepick () :
        filepick.file_path = "null"
        filepick.file_path = filedialog.askopenfilename()

    bot = telegram.Bot(token='6115375551:AAEETzd2n4DXp2JvNgNeYZRUBpLCwQ5flGw')
    user_id = '5423490009'
    today = datetime.today()
    # new_window = tk.Tk()
    today_formatted = today.strftime("%Y-%m-%d")
    new_window = tk.Toplevel(root)
    new_window.title("Banerjee Broadband Satellite Communication (CABLE)")
    new_window.geometry("437x413")
    new_window.attributes('-topmost', True)
    new_window['background']='#d6d6d6'
    def bill():
        today = datetime.today()
        date = str(today)
        tdate = str(datetime.today().strftime("%Y-%m-%d"))
        ttime = str(datetime.now())
        ttime = ttime.split(" ")
        ttime = str(ttime[1])
        ttime = ttime.split(":")
        ttime = str(ttime[0] + ttime[1])
        tdate = tdate.split("-")
        tdate1 = tdate[0]
        tdate1 = [*tdate1]
        tdate1 = str (tdate1[2] + tdate1[3])
        billno = str (str(tdate1) + tdate[1] + tdate[2] +  ttime)
        mb = billno
        return(billno)

    new_window.attributes("-alpha", 1)
    date_entry = tk.Entry(new_window, highlightthickness=0, highlightbackground=new_window["bg"])
    p1 = PhotoImage(file = resource_path('C:\BBSC\ict.png'))
    new_window.iconphoto(False, p1)

    date = datetime.now().date()
    rd = str(date + timedelta(days=29))

    date_label = tk.Label(new_window, text="DATE :", bg='#d6d6d6')
    date_label.grid(row=0, column=0, padx=5, pady=5)
    date_entry = tk.Entry(new_window, bd=0)
    date_entry.insert(0, datetime.now().date()) 
    date_entry.grid(row=0, column=1, padx=5, pady=5)

    filepick_button = tk.Button(new_window, text="Choose excel file", command=filepick, borderwidth=0, background='white')
    filepick_button.grid(row=1, column=3, padx=5, pady=5)

    renew_date_label = tk.Label(new_window, text="Renew Date :", bg='#d6d6d6')
    renew_date_label.grid(row=0, column=2, padx=5, pady=5)
    renew_date_entry = tk.Entry(new_window, bd=0)
    renew_date_entry.insert(0, rd) 
    renew_date_entry.grid(row=0, column=3, padx=5, pady=5)

    name_label = tk.Label(new_window, text="NAME :", bg='#d6d6d6')
    name_label.grid(row=1, column=0, padx=5, pady=5)
    name_entry = tk.Entry(new_window, bd=0, width=20)
    name_entry.grid(row=1, column=1, padx=5, pady=5)  

    address_label = tk.Label(new_window, text="ADDRESS :", bg='#d6d6d6')
    address_label.grid(row=2, column=0, padx=5, pady=5)
    address_entry = tk.Entry(new_window, bd=0)
    address_entry.grid(row=2, column=1, padx=5, pady=5)

    phn_no_label = tk.Label(new_window, text="PHONE  :", bg='#d6d6d6')
    phn_no_label.grid(row=3, column=2, padx=5, pady=5)
    phn_no_entry = tk.Entry(new_window, bd=0)
    phn_no_entry.grid(row=3, column=3, padx=5, pady=5)

    vc_label = tk.Label(new_window, text="VC. No. :", bg='#d6d6d6')
    vc_label.grid(row=2, column=2, padx=5, pady=5)
    vc_entry = tk.Entry(new_window, bd=0)
    vc_entry.grid(row=2, column=3, padx=5, pady=5)


    bill_label = tk.Label(new_window, text="Bill No. :", bg='#d6d6d6')
    bill_label.grid(row=3, column=0, padx=5, pady=5)
    bill_entry = tk.Entry(new_window, bd=0)
    bill_entry.insert(0, str(bill())) 
    bill_entry.grid(row=3, column=1, padx=5, pady=5)

    fta_label = tk.Label(new_window, text="FTA :", bg='#d6d6d6')
    fta_label.grid(row=4, column=0, padx=5, pady=5)
    fta_entry = tk.Entry(new_window, bd=0)
    fta_entry.grid(row=4, column=1, padx=5, pady=5)

    pay_ch_label = tk.Label(new_window, text="Pay Ch :", bg='#d6d6d6')
    pay_ch_label.grid(row=5, column=0, padx=5, pady=5)
    pay_ch_entry = tk.Entry(new_window, bd=0)
    pay_ch_entry.grid(row=5, column=1, padx=5, pady=5)

    ncf_label = tk.Label(new_window, text="NCF :", bg='#d6d6d6')
    ncf_label.grid(row=7, column=0, padx=5, pady=5)
    ncf_entry = tk.Entry(new_window, bd=0)
    ncf_entry.grid(row=7, column=1, padx=5, pady=5)

    hardware_label = tk.Label(new_window, text="Hardware :", bg='#d6d6d6')
    hardware_label.grid(row=8, column=0, padx=5, pady=5)
    hardware_entry = tk.Entry(new_window, bd=0)
    hardware_entry.grid(row=8, column=1, padx=5, pady=5)

    p_due_label = tk.Label(new_window, text="P. Due :", bg='#d6d6d6')
    p_due_label.grid(row=9, column=0, padx=5, pady=5)
    p_due_entry = tk.Entry(new_window, bd=0)
    p_due_entry.grid(row=9, column=1, padx=5, pady=5)

    total_label = tk.Label(new_window, text="TOTAL :", bg='#d6d6d6')
    total_label.grid(row=10, column=0, padx=5, pady=5)
    total_entry = tk.Entry(new_window, bd=0)
    total_entry.grid(row=10, column=1, padx=5, pady=5)

    paid_label = tk.Label(new_window, text="PAID :", bg='#d6d6d6')
    paid_label.grid(row=11, column=0, padx=5, pady=5)
    paid_entry = tk.Entry(new_window, bd=0)
    paid_entry.grid(row=11, column=1, padx=5, pady=5)

    adv_label = tk.Label(new_window, text="ADVANCE :", bg='#d6d6d6')
    adv_label.grid(row=12, column=0, padx=5, pady=5)
    adv_entry = tk.Entry(new_window, bd=0)
    adv_entry.grid(row=12, column=1, padx=5, pady=5)

    total_due_label = tk.Label(new_window, text="TOTAL DUE :", bg='#d6d6d6')
    total_due_label.grid(row=13, column=0, padx=5, pady=5)
    total_due_entry = tk.Entry(new_window, bd=0)
    total_due_entry.grid(row=13, column=1, padx=5, pady=5)


    def calculate_total():
        try:
            fta = float(fta_entry.get())
        except :
            fta = 0
        try :
            ncf = float(ncf_entry.get())
        except :
            ncf = 0
        try:
            pay_ch = float(pay_ch_entry.get())
        except :
            pay_ch = 0
        try :
            hardware = float(hardware_entry.get())
        except :
            hardware = 0
        try :
            p_due = float(p_due_entry.get())
        except :
            p_due = 0

        total = str(fta + ncf + pay_ch +(0.18 * (fta + ncf + pay_ch)) + hardware + p_due)
        totala = total.split(".")
        totalb = str(totala[1])
        totalb = [*totalb]
        if float(totalb[0])>= 5 :
            totalb = str(float(totala[0]) + 1)
            totalb = totalb.replace('.0','')
        else :
            totalb = str(float(totala[0]))
            totalb = totalb.replace('.0','')
        calculate_total.totalb = str(totalb)
        totalm = total
        totalm = total.split('.')
        totalm = str(totalm[1])
        totalm = [*totalm]
        totalm = str( str(totalm[0]))
        totalmn = total.split('.')
        total = str(str(totalmn[0]) + "." +str(totalm))
        total = str(str(totalb) + "  (" + total + ")" )
        total_entry.delete(0, END)
        total_entry.insert(0, total)

    def clear ():
        date = datetime.now().date()
        rd = str(date + timedelta(days=29))
        date_entry.delete(0, END)
        date_entry.insert(0, date)
        renew_date_entry.delete(0, END)
        renew_date_entry.insert(0, rd)
        bill_entry.delete(0, END)
        bill_entry.insert(0, bill())
        name_entry.delete(0, END)
        address_entry.delete(0, END)
        phn_no_entry.delete(0, END)
        vc_entry.delete(0, END)
        fta_entry.delete(0, END)
        pay_ch_entry.delete(0, END)
        ncf_entry.delete(0, END)
        hardware_entry.delete(0, END)
        p_due_entry.delete(0, END)
        total_entry.delete(0, END)
        paid_entry.delete(0, END)
        adv_entry.delete(0, END)
        total_due_entry.delete(0, END)

    def reset () :
        clear()

    def calt():
        try:
            totalb = str(calculate_total.totalb)
        except :
            totalb = 0
        try :
            paid = float(paid_entry.get())
            
        except :
            paid = 0
        try :
            adv = float(adv_entry.get())
            
        except :
            adv = 0
        # print (paid)
        tamt = str(float(totalb) - (float(adv) + float(paid)))
        tamt = tamt.replace('.0','')
        total_due_entry.delete(0, END)
        total_due_entry.insert(0, tamt)

    calculate_button = tk.Button(new_window, text="CALCULATE", command=calculate_total, borderwidth=0, background='white')
    calculate_button.grid(row=10, column=2, padx=5, pady=5)

    calculatet_button = tk.Button(new_window, text="TOTAL", command=calt, borderwidth=0, background='white')
    calculatet_button.grid(row=13, column=2, padx=5, pady=5)



    reset_button = tk.Button(new_window, text="RESET", command=reset, borderwidth=0, background='white')
    reset_button.grid(row=10, column=3, padx=5, pady=5)

    def autodetect():
        import datetime
        yr = datetime.datetime.now().year
        mnth = datetime.datetime.now().month
        month_names = {
            1: 'jan',
            2: 'feb',
            3: 'mar',
            4: 'apr',
            5: 'may',
            6: 'jun',
            7: 'jul',
            8: 'aug',
            9: 'sep',
            10: 'oct',
            11: 'nov',
            12: 'dec'
        }
        mnth = month_names[mnth]
        try :
            if "null" == str(filepick.file_path) :
                dirn = str("C:\\Users\\ADMIN\\Desktop" + "\\update " + str(mnth) + " " + str (yr) + ".xlsx")
        except :
            dirn = str("C:\\Users\\ADMIN\\Desktop" + "\\update " + str(mnth) + " " + str (yr) + ".xlsx")
        else :
            dirn = str(filepick.file_path)
        try :
            df = pd.read_excel(resource_path(dirn))
            name = str(name_entry.get())
            if name == "" :
                name = str(phn_no_entry.get())
                name = name.replace(' ','')
            else :
                name = name.lower()
                name = name.replace(' ','')
            data = df.values.tolist()
            del data[:3]
            for i in data :
                ti = str(str(i).replace(" " , ""))
                ti = ti.lower()
                if name in ti :
                    indext = data.index(i)
                    tf = data[int(indext)]
                    name = str(tf[0])
                    addr = str(tf[2])
                    phn = str(tf[3])
                    vc = str(tf[1])
                    name_entry.delete(0, END)
                    name_entry.insert(0, name)
                    address_entry.delete(0, END)
                    address_entry.insert(0, addr)
                    phn_no_entry.delete(0, END)
                    phn_no_entry.insert(0, phn)
                    vc_entry.delete(0, END)
                    vc_entry.insert(0, vc)
                    break
                else :
                    address_entry.delete(0, END)
                    phn_no_entry.delete(0, END)
                    vc_entry.delete(0, END)
                    bill_entry.delete(0, END)
                    bill_entry.insert(0, bill())
        except Exception as e:
                with open(resource_path('C:\BBSC\error.txt'), 'a') as file:
                    file.write(str('\n' + str(e)))
                    file.close()

    def get():
        try:
            date = str(date_entry.get())
            if str (date) == '' :
                date = "NILL"
            else :
                pass
        except:
            date = "NILL"
        try:    
            renew_date = str(renew_date_entry.get())
            if str (renew_date) == '' :
                renew_date = "NILL"
            else :
                pass
        except:
            renew_date = "NILL"
        try:    
            name = str(name_entry.get())
            if str (name) == '' :
                name = "NILL"
            else :
                pass
        except:
            name = "NILL"
        try:    
            address =  str(address_entry.get())
            if str (address) == '' :
                address = "NILL"
            else :
                pass
        except:
            address = "NILL"
        try:    
            phn_no =  str(phn_no_entry.get())
            if str (phn_no) == '' :
                phn_no = "NILL"
            else :
                pass
        except:
            phn_no = "NILL"
        try:    
            vc =  str(vc_entry.get())
            if str (vc) == '' :
                vc = "NILL"
            else :
                pass
        except:
            vc = "NILL"
        try:    
            bill =  str(bill_entry.get())
            if str (bill) == '' :
                bill = "NILL"
            else :
                pass
        except:
            bill = "NILL"
        try:    
            fta = str(fta_entry.get())
            if str (fta) == '' :
                fta = "0"
            else :
                pass
        except:
            fta = "0"
        try:    
            pay_ch = str(pay_ch_entry.get())
            if str (pay_ch) == '' :
                pay_ch = "0"
            else :
                pass
        except:
            pay_ch = "0"
        try:    
            ncf = str(ncf_entry.get())
            if str (ncf) == '' :
                ncf = "0"
            else :
                pass
        except:
            ncf = "0"
        try:    
            hardware =  str(hardware_entry.get())
            if str (hardware) == '' :
                hardware = "0"
            else :
                pass
        except:
            hardware = "0"
        try:    
            p_due =  str(p_due_entry.get())
            if str (p_due) == '' :
                p_due = "0"
            else :
                pass
        except:
            p_due = "0"
        try:    
            total =  str(total_entry.get())
            if str (total) == '' :
                total = "0"
            else :
                pass
        except:
            total = "0"
        try:    
            paid =  str(paid_entry.get())
            if str (paid) == '' :
                paid = "0"
            else :
                pass
        except:
            paid = "0"
        try:    
            adv =  str(adv_entry.get())
            if str (adv) == '' :
                adv = "0"
            else :
                pass
        except:
            adv = "0"
        try:    
            total_due =  str(total_due_entry.get())
            if str (total_due) == '' :
                total_due = "0"
            else :
                pass
        except:
            total_due = "0"
        try :
            record = [date, renew_date ,name, address,phn_no, vc, bill, fta, pay_ch, ncf, hardware,p_due, total, paid, total_due]
            recordt = [str( " date" + " : " + date), str( "renew_date" + " : " + renew_date) ,str( "name" + " : " + name), str( "address" + " : " + address), str( "phn_no" + " : " + phn_no), str( "vc" + " : " + vc), str( "bill" + " : " + bill), str( "fta" + " : " + fta), str( "pay_ch" + " : " + pay_ch), str( "ncf" + " : " + ncf), str( "hardware" + " : " + hardware), str( "p_due" + " : " + p_due), str( "total" + " : " + total), str( "paid" + " : " + paid)  , str( "advance" + " : " + adv) ,str( "total_due" + " : " + total_due)]
            recordt = str(', '.join(recordt))
            recordt = recordt.replace(',' , '\n')
            recordt = str(recordt).replace("\n\n","\n")
            with open(resource_path('C:\BBSC\\rec\srecord.txt'), 'a') as file:
                file.write('\n\n' + str(recordt))
                file.close()
            image = Image.open(resource_path("C:\BBSC\sbill.png"))
            title_font = ImageFont.truetype(resource_path('C:\BBSC\sfont.otf'), 27)
            date = (record[0] + " - " + record[1])
            name = record[2]
            address = str(record[3])
            lines = []
            line_length = 0
            max_line_length = 20
            words = address.split()
            for word in words:
                if not lines or line_length + len(word) + 1 > max_line_length:
                    lines.append(word)
                    line_length = len(word)
                else:
                    lines[-1] += " " + word
                    line_length += len(word) + 1
            address_lines = "\n".join(lines)
            phn = record[4]
            vc = record[5]
            bill = record[6]
            fta = record[7]
            pay_ch = record[8]
            ncf = record[9]
            hardware = record[10]
            p_due = record[11]
            total = record[12]
            paid = record[13]
            total_due = record[14]
            gst = str(0.18 * (float(fta) + float(ncf) + float(pay_ch)))
            totalm = gst.split('.')
            totalm = str(totalm[1])
            totalm = [*totalm]
            totalm = str( str(totalm[0]))
            totalmn = gst.split('.')
            gst = str(str(totalmn[0]) + "." +str(totalm))
            image_editable = ImageDraw.Draw(image)
            image_editable.text((870,500), date, (0, 0, 0), font=title_font)
            image_editable.text((370,540), name, (0, 0, 0), font=title_font)
            image_editable.text((190,610), address_lines, (0, 0, 0), font=title_font)
            image_editable.text((190,578), phn, (0, 0, 0), font=title_font)
            image_editable.text((1040,578), vc, (0, 0, 0), font=title_font)
            image_editable.text((1061,540), bill, (0, 0, 0), font=title_font)
            image_editable.text((1141,857), fta, (0, 0, 0), font=title_font)
            image_editable.text((1141,920), pay_ch, (0, 0, 0), font=title_font)
            image_editable.text((1141,983), ncf, (0, 0, 0), font=title_font)
            image_editable.text((1141,1046), hardware, (0, 0, 0), font=title_font)
            image_editable.text((1141,1109), p_due, (0, 0, 0), font=title_font)
            image_editable.text((1141,1210), total, (0, 0, 0), font=title_font)
            image_editable.text((1141,1268), paid, (0, 0, 0), font=title_font)
            image_editable.text((1141,1326), total_due, (0, 0, 0), font=title_font)
            image_editable.text((417,1241), gst, (0, 0, 0), font=title_font)
            nameb = resource_path(str("C:\BBSC\pdf" + str(str(bill) + ".pdf")))
            rotated_image = image.rotate(-90, expand=True)
            main_image = Image.open(resource_path('C:\BBSC\mi.png'))
            embedded_image = rotated_image.resize((3220,2268))
            main_image.paste(embedded_image, (-170, -150))
            # main_image.save(nameb)
            imagef = main_image.convert("RGB")
            imagef.save(nameb, "PDF", resolution=100.0)
            os.startfile(resource_path(nameb))
            gitcommit(bill)
            bot.send_message(chat_id=user_id, text=str(str("Cable Bill\n\n") + str(recordt)))
            clear()
        except Exception as e:
                with open(resource_path('C:\BBSC\error.txt'), 'a') as file:
                    file.write(str('\n' + str(e)))
                    file.close()

    submit_button = tk.Button(new_window, text="SUBMIT", command=get, borderwidth=0, background='white')
    submit_button.grid(row=13, column=3, padx=5, pady=5)

    detect_button = tk.Button(new_window, text="SEARCH", command=autodetect, borderwidth=0, background='white')
    detect_button.grid(row=1, column=2, padx=5, pady=5)

    new_window.mainloop()

def wifi_window () :
    def filepick () :
        filepick.file_path = "null"
        filepick.file_path = filedialog.askopenfilename()
    bot = telegram.Bot(token='6115375551:AAEETzd2n4DXp2JvNgNeYZRUBpLCwQ5flGw')
    user_id = '5423490009'
    today = datetime.today()
    today_formatted = today.strftime("%Y-%m-%d")
    new_window = tk.Toplevel(root)
    new_window.title("Banerjee Broadband Satellite Communication (WiFi)")
    new_window.geometry("485x446")
    new_window.attributes('-topmost', True)
    new_window['background']='#d6d6d6'

    def bill():
        today = datetime.today()
        date = str(today)
        tdate = str(datetime.today().strftime("%Y-%m-%d"))
        ttime = str(datetime.now())
        ttime = ttime.split(" ")
        ttime = str(ttime[1])
        ttime = ttime.split(":")
        ttime = str(ttime[0] + ttime[1])
        tdate = tdate.split("-")
        tdate1 = tdate[0]
        tdate1 = [*tdate1]
        tdate1 = str (tdate1[2] + tdate1[3])
        billno = str (str(tdate1) + tdate[1] + tdate[2] +  ttime)
        mb = billno
        return(billno)

    new_window.attributes("-alpha", 1)
    date_entry = tk.Entry(new_window, highlightthickness=0, highlightbackground=new_window["bg"])
    p1 = PhotoImage(file = resource_path('C:\BBSC\ict.png'))
    new_window.iconphoto(False, p1)

    date = datetime.now().date()
    rd = str(date + timedelta(days=29))

    date_label = tk.Label(new_window, text="DATE :", bg='#d6d6d6')
    date_label.grid(row=0, column=0, padx=5, pady=5)
    date_entry = tk.Entry(new_window, bd=0)
    date_entry.insert(0, datetime.now().date()) 
    date_entry.grid(row=0, column=1, padx=5, pady=5)

    renew_date_label = tk.Label(new_window, text="Renew Date :", bg='#d6d6d6')
    renew_date_label.grid(row=0, column=2, padx=5, pady=5)
    renew_date_entry = tk.Entry(new_window, bd=0)
    renew_date_entry.insert(0, rd) 
    renew_date_entry.grid(row=0, column=3, padx=5, pady=5)

    filepick_button = tk.Button(new_window, text="Choose excel file", command=filepick, borderwidth=0, background='white')
    filepick_button.grid(row=1, column=3, padx=5, pady=5)

    name_label = tk.Label(new_window, text="NAME :", bg='#d6d6d6')
    name_label.grid(row=1, column=0, padx=5, pady=5)
    name_entry = tk.Entry(new_window, bd=0, width=20)
    name_entry.grid(row=1, column=1, padx=5, pady=5)  

    address_label = tk.Label(new_window, text="ADDRESS :", bg='#d6d6d6')
    address_label.grid(row=2, column=0, padx=5, pady=5)
    address_entry = tk.Entry(new_window, bd=0)
    address_entry.grid(row=2, column=1, padx=5, pady=5)

    phn_no_label = tk.Label(new_window, text="PHONE  :", bg='#d6d6d6')
    phn_no_label.grid(row=3, column=2, padx=5, pady=5)
    phn_no_entry = tk.Entry(new_window, bd=0)
    phn_no_entry.grid(row=3, column=3, padx=5, pady=5)

    vc_label = tk.Label(new_window, text="VC. No. :", bg='#d6d6d6')
    vc_label.grid(row=2, column=2, padx=5, pady=5)
    vc_entry = tk.Entry(new_window, bd=0)
    vc_entry.grid(row=2, column=3, padx=5, pady=5)


    bill_label = tk.Label(new_window, text="Bill No. :", bg='#d6d6d6')
    bill_label.grid(row=3, column=0, padx=5, pady=5)
    bill_entry = tk.Entry(new_window, bd=0)
    bill_entry.insert(0, str(bill())) 
    bill_entry.grid(row=3, column=1, padx=5, pady=5)

    fta_label = tk.Label(new_window, text="FTA :", bg='#d6d6d6')
    fta_label.grid(row=4, column=0, padx=5, pady=5)
    fta_entry = tk.Entry(new_window, bd=0)
    fta_entry.grid(row=4, column=1, padx=5, pady=5)

    pay_ch_label = tk.Label(new_window, text="Pay Ch :", bg='#d6d6d6')
    pay_ch_label.grid(row=5, column=0, padx=5, pady=5)
    pay_ch_entry = tk.Entry(new_window, bd=0)
    pay_ch_entry.grid(row=5, column=1, padx=5, pady=5)

    ncf_label = tk.Label(new_window, text="NCF :", bg='#d6d6d6')
    ncf_label.grid(row=7, column=0, padx=5, pady=5)
    ncf_entry = tk.Entry(new_window, bd=0)
    ncf_entry.grid(row=7, column=1, padx=5, pady=5)

    hardware_label = tk.Label(new_window, text="Hardware :", bg='#d6d6d6')
    hardware_label.grid(row=8, column=0, padx=5, pady=5)
    hardware_entry = tk.Entry(new_window, bd=0)
    hardware_entry.grid(row=8, column=1, padx=5, pady=5)

    p_due_label = tk.Label(new_window, text="P. Due :", bg='#d6d6d6')
    p_due_label.grid(row=9, column=0, padx=5, pady=5)
    p_due_entry = tk.Entry(new_window, bd=0)
    p_due_entry.grid(row=9, column=1, padx=5, pady=5)

    mnth_of_label = tk.Label(new_window, text="Month of :", bg='#d6d6d6')
    mnth_of_label.grid(row=10, column=0, padx=5, pady=5)
    mnth_of_entry = tk.Entry(new_window, bd=0)
    mnth_of_entry.grid(row=10, column=1, padx=5, pady=5)
    
    mnth_of_mnth_entry = tk.Entry(new_window, bd=0)
    mnth_of_mnth_entry.grid(row=10, column=2, padx=5, pady=5)

    total_label = tk.Label(new_window, text="TOTAL :", bg='#d6d6d6')
    total_label.grid(row=11, column=0, padx=5, pady=5)
    total_entry = tk.Entry(new_window, bd=0)
    total_entry.grid(row=11, column=1, padx=5, pady=5)

    paid_label = tk.Label(new_window, text="PAID :", bg='#d6d6d6')
    paid_label.grid(row=12, column=0, padx=5, pady=5)
    paid_entry = tk.Entry(new_window, bd=0)
    paid_entry.grid(row=12, column=1, padx=5, pady=5)

    adv_label = tk.Label(new_window, text="ADVANCE :", bg='#d6d6d6')
    adv_label.grid(row=13, column=0, padx=5, pady=5)
    adv_entry = tk.Entry(new_window, bd=0)
    adv_entry.grid(row=13, column=1, padx=5, pady=5)

    total_due_label = tk.Label(new_window, text="TOTAL DUE :", bg='#d6d6d6')
    total_due_label.grid(row=14, column=0, padx=5, pady=5)
    total_due_entry = tk.Entry(new_window, bd=0)
    total_due_entry.grid(row=14, column=1, padx=5, pady=5)


    def calculate_total():
        try:
            fta = float(fta_entry.get())
        except :
            fta = 0
        try :
            ncf = float(ncf_entry.get())
        except :
            ncf = 0
        try:
            pay_ch = float(pay_ch_entry.get())
        except :
            pay_ch = 0
        try :
            hardware = float(hardware_entry.get())
        except :
            hardware = 0
        try :
            p_due = float(p_due_entry.get())
        except :
            p_due = 0
        try :
            mnth_of = float(mnth_of_entry.get())
        except :
            mnth_of = 0
        

        total = str(fta + ncf + pay_ch +(0.18 * (fta + ncf + pay_ch)) + hardware + p_due + mnth_of)
        totala = total.split(".")
        totalb = str(totala[1])
        totalb = [*totalb]
        if float(totalb[0])>= 5 :
            totalb = str(float(totala[0]) + 1)
            totalb = totalb.replace('.0','')
        else :
            totalb = str(float(totala[0]))
            totalb = totalb.replace('.0','')
        calculate_total.totalb = str(totalb)
        totalm = total
        totalm = total.split('.')
        totalm = str(totalm[1])
        totalm = [*totalm]
        totalm = str( str(totalm[0]))
        totalmn = total.split('.')
        total = str(str(totalmn[0]) + "." +str(totalm))
        total = str(str(totalb) + "  (" + total + ")" )
        total_entry.delete(0, END)
        total_entry.insert(0, total)

    def clear ():
        date = datetime.now().date()
        rd = str(date + timedelta(days=29))
        date_entry.delete(0, END)
        date_entry.insert(0, date)
        renew_date_entry.delete(0, END)
        renew_date_entry.insert(0, rd)
        bill_entry.delete(0, END)
        bill_entry.insert(0, bill())
        name_entry.delete(0, END)
        address_entry.delete(0, END)
        phn_no_entry.delete(0, END)
        vc_entry.delete(0, END)
        fta_entry.delete(0, END)
        pay_ch_entry.delete(0, END)
        ncf_entry.delete(0, END)
        hardware_entry.delete(0, END)
        p_due_entry.delete(0, END)
        total_entry.delete(0, END)
        paid_entry.delete(0, END)
        adv_entry.delete(0, END)
        total_due_entry.delete(0, END)
        mnth_of_entry.delete(0, END)
        mnth_of_mnth_entry.delete(0, END)

    def reset () :
        clear()

    def calt():
        try:
            totalb = str(calculate_total.totalb)
        except :
            totalb = 0
        try :
            adv = float(adv_entry.get())
            
        except :
            adv = 0
        try :
            paid = float(paid_entry.get())
            
        except :
            paid = 0
        # print (paid)
        tamt = str(float(totalb) - (float(adv) + float(paid)))
        tamt = tamt.replace('.0','')
        total_due_entry.delete(0, END)
        total_due_entry.insert(0, tamt)

    calculate_button = tk.Button(new_window, text="CALCULATE", command=calculate_total, borderwidth=0, background='white')
    calculate_button.grid(row=11, column=2, padx=5, pady=5)

    calculatet_button = tk.Button(new_window, text="TOTAL", command=calt, borderwidth=0, background='white')
    calculatet_button.grid(row=14, column=2, padx=5, pady=5)

    reset_button = tk.Button(new_window, text="RESET", command=reset, borderwidth=0, background='white')
    reset_button.grid(row=11, column=3, padx=5, pady=5)

    def autodetect():
        import datetime
        yr = datetime.datetime.now().year
        mnth = datetime.datetime.now().month
        month_names = {
            1: 'jan',
            2: 'feb',
            3: 'mar',
            4: 'apr',
            5: 'may',
            6: 'jun',
            7: 'jul',
            8: 'aug',
            9: 'sep',
            10: 'oct',
            11: 'nov',
            12: 'dec'
        }
        mnth = month_names[mnth]
        try :
            if "null" == str(filepick.file_path) :
                dirn = str("C:\\Users\\ADMIN\\Desktop" + "\\update " + str(mnth) + " " + str (yr) + ".xlsx")
        except :
            dirn = str("C:\\Users\\ADMIN\\Desktop" + "\\update " + str(mnth) + " " + str (yr) + ".xlsx")
        else :
            dirn = str(filepick.file_path)
        try :
            df = pd.read_excel(resource_path(dirn))
            name = str(name_entry.get())
            if name == "" :
                name = str(phn_no_entry.get())
                name = name.replace(' ','')
            else :
                name = name.lower()
                name = name.replace(' ','')
            data = df.values.tolist()
            del data[:3]
            for i in data :
                ti = str(str(i).replace(" " , ""))
                ti = ti.lower()
                if name in ti :
                    indext = data.index(i)
                    tf = data[int(indext)]
                    name = str(tf[0])
                    addr = str(tf[2])
                    phn = str(tf[3])
                    vc = str(tf[1])
                    name_entry.delete(0, END)
                    name_entry.insert(0, name)
                    address_entry.delete(0, END)
                    address_entry.insert(0, addr)
                    phn_no_entry.delete(0, END)
                    phn_no_entry.insert(0, phn)
                    vc_entry.delete(0, END)
                    vc_entry.insert(0, vc)
                    break
                else :
                    address_entry.delete(0, END)
                    phn_no_entry.delete(0, END)
                    vc_entry.delete(0, END)
                    bill_entry.delete(0, END)
                    bill_entry.insert(0, bill())
        except Exception as e:
                with open(resource_path('C:\BBSC\error.txt'), 'a') as file:
                    file.write(str('\n' + str(e)))
                    file.close()

    def get():
        try:
            date = str(date_entry.get())
            if str (date) == '' :
                date = "NILL"
            else :
                pass
        except:
            date = "NILL"
        try:    
            renew_date = str(renew_date_entry.get())
            if str (renew_date) == '' :
                renew_date = "NILL"
            else :
                pass
        except:
            renew_date = "NILL"
        try:    
            name = str(name_entry.get())
            if str (name) == '' :
                name = "NILL"
            else :
                pass
        except:
            name = "NILL"
        try:    
            address =  str(address_entry.get())
            if str (address) == '' :
                address = "NILL"
            else :
                pass
        except:
            address = "NILL"
        try:    
            phn_no =  str(phn_no_entry.get())
            if str (phn_no) == '' :
                phn_no = "NILL"
            else :
                pass
        except:
            phn_no = "NILL"
        try:    
            vc =  str(vc_entry.get())
            if str (vc) == '' :
                vc = "NILL"
            else :
                pass
        except:
            vc = "NILL"
        try:    
            bill =  str(bill_entry.get())
            if str (bill) == '' :
                bill = "NILL"
            else :
                pass
        except:
            bill = "NILL"
        try:    
            fta = str(fta_entry.get())
            if str (fta) == '' :
                fta = "0"
            else :
                pass
        except:
            fta = "0"
        try:    
            pay_ch = str(pay_ch_entry.get())
            if str (pay_ch) == '' :
                pay_ch = "0"
            else :
                pass
        except:
            pay_ch = "0"
        try:    
            ncf = str(ncf_entry.get())
            if str (ncf) == '' :
                ncf = "0"
            else :
                pass
        except:
            ncf = "0"
        try:    
            hardware =  str(hardware_entry.get())
            if str (hardware) == '' :
                hardware = "0"
            else :
                pass
        except:
            hardware = "0"
        try:    
            p_due =  str(p_due_entry.get())
            if str (p_due) == '' :
                p_due = "0"
            else :
                pass
        except:
            p_due = "0"
        try:    
            mnth_of =  str(mnth_of_entry.get())
            if str (mnth_of) == '' :
                mnth_of = "0"
            else :
                pass
        except:
            mnth_of = "0"
        try:    
            mnth_of_mnth =  str(mnth_of_mnth_entry.get())
            if str (mnth_of_mnth) == '' :
                mnth_of_mnth = "NILL"
            else :
                pass
        except:
            mnth_of_mnth = "NILL"
        try:    
            total =  str(total_entry.get())
            if str (total) == '' :
                total = "0"
            else :
                pass
        except:
            total = "0"
        try:    
            paid =  str(paid_entry.get())
            if str (paid) == '' :
                paid = "0"
            else :
                pass
        except:
            paid = "0"
        try:    
            adv =  str(adv_entry.get())
            if str (adv) == '' :
                adv = "0"
            else :
                pass
        except:
            adv = "0"
        try:    
            total_due =  str(total_due_entry.get())
            if str (total_due) == '' :
                total_due = "0"
            else :
                pass
        except:
            total_due = "0"
        try :
            record = [date, renew_date ,name, address,phn_no, vc, bill, fta, pay_ch, ncf, hardware,p_due,mnth_of ,mnth_of_mnth, total, paid, total_due]
            recordt = [str( " date" + " : " + date), str( "renew_date" + " : " + renew_date) ,str( "name" + " : " + name), str( "address" + " : " + address), str( "phn_no" + " : " + phn_no), str( "vc" + " : " + vc), str( "bill" + " : " + bill), str( "fta" + " : " + fta), str( "pay_ch" + " : " + pay_ch), str( "ncf" + " : " + ncf), str( "hardware" + " : " + hardware), str( "p_due" + " : " + p_due) , str( "mnth_of" + " : " +  str(mnth_of_mnth) + "  " + mnth_of), str( "total" + " : " + total) , str( "advance" + " : " + adv) ,str( "total_due" + " : " + total_due)]
            recordt = str(', '.join(recordt))
            recordt = recordt.replace(',' , '\n')
            recordt = str(recordt).replace("\n\n","\n")
            with open(resource_path('C:\BBSC\\rec\srecord.txt'), 'a') as file:
                file.write('\n\n' + str(recordt))
                file.close()
            image = Image.open(resource_path("C:\BBSC\sbill2.png"))
            title_font = ImageFont.truetype(resource_path('C:\BBSC\sfont.otf'), 27)
            date = (record[0] + " - " + record[1])
            name = record[2]
            address = str(record[3])
            lines = []
            line_length = 0
            max_line_length = 20
            words = address.split()
            for word in words:
                if not lines or line_length + len(word) + 1 > max_line_length:
                    lines.append(word)
                    line_length = len(word)
                else:
                    lines[-1] += " " + word
                    line_length += len(word) + 1
            address_lines = "\n".join(lines)
            phn = record[4]
            vc = record[5]
            bill = record[6]
            fta = record[7]
            pay_ch = record[8]
            ncf = record[9]
            hardware = record[10]
            p_due = record[11]
            total = record[14]
            paid = record[15]
            total_due = record[16]
            gst = str(0.18 * (float(fta) + float(ncf) + float(pay_ch)))
            totalm = gst.split('.')
            totalm = str(totalm[1])
            totalm = [*totalm]
            totalm = str( str(totalm[0]))
            totalmn = gst.split('.')
            gst = str(str(totalmn[0]) + "." +str(totalm))
            image_editable = ImageDraw.Draw(image)
            image_editable.text((870,500), date, (0, 0, 0), font=title_font)
            image_editable.text((370,540), name, (0, 0, 0), font=title_font)
            image_editable.text((190,610), address_lines, (0, 0, 0), font=title_font)
            image_editable.text((190,578), phn, (0, 0, 0), font=title_font)
            image_editable.text((1040,578), vc, (0, 0, 0), font=title_font)
            image_editable.text((1061,540), bill, (0, 0, 0), font=title_font)
            image_editable.text((1141,857), fta, (0, 0, 0), font=title_font)
            image_editable.text((1141,920), pay_ch, (0, 0, 0), font=title_font)
            image_editable.text((1141,983), ncf, (0, 0, 0), font=title_font)
            image_editable.text((1141,1046), hardware, (0, 0, 0), font=title_font)
            image_editable.text((1141,1109), p_due, (0, 0, 0), font=title_font)

            image_editable.text((740,1109), str(mnth_of_mnth), (0, 0, 0), font=title_font)

            image_editable.text((1141,1142), str(mnth_of), (0, 0, 0), font=title_font)
            image_editable.text((1141,1210), total, (0, 0, 0), font=title_font)
            image_editable.text((1141,1268), paid, (0, 0, 0), font=title_font)
            image_editable.text((1141,1326), total_due, (0, 0, 0), font=title_font)
            image_editable.text((417,1241), gst, (0, 0, 0), font=title_font)
            nameb = resource_path(str("C:\BBSC\pdf" + str(str(bill) + ".pdf")))
            rotated_image = image.rotate(-90, expand=True)
            main_image = Image.open(resource_path('C:\BBSC\mi.png'))
            embedded_image = rotated_image.resize((3220,2268))
            main_image.paste(embedded_image, (-170, -150))
            imagef = main_image.convert("RGB")
            imagef.save(nameb, "PDF", resolution=100.0)
            os.startfile(resource_path(nameb))
            gitcommit(bill)
            bot.send_message(chat_id=user_id, text=str(str("WiFi Bill\n\n") + str(recordt)))
            clear()
        except Exception as e:
                with open(resource_path('C:\BBSC\error.txt'), 'a') as file:
                    file.write(str('\n' + str(e)))
                    file.close()

    submit_button = tk.Button(new_window, text="SUBMIT", command=get, borderwidth=0, background='white')
    submit_button.grid(row=14, column=3, padx=5, pady=5)

    detect_button = tk.Button(new_window, text="SEARCH", command=autodetect, borderwidth=0, background='white')
    detect_button.grid(row=1, column=2, padx=5, pady=5)

root = tk.Tk()
root.title("BBSC HOME")
root.geometry("300x70")
root['background']='#ffffff'
p2 = PhotoImage(file = resource_path('C:\BBSC\ict.png'))
root.iconphoto(False, p2)

cable_button = tk.Button(root, text="Cable Billing", command=cable_window, borderwidth=0, background='white')
cable_button.grid(row=0, column=0, padx=5, pady=5)

wifi_button = tk.Button(root, text="Wi-Fi Billing", command=wifi_window, borderwidth=0, background='white')
wifi_button.grid(row=1, column=0, padx=120, pady=5)

root.mainloop()