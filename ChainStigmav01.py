import tkinter as tk
import time
import json
import requests
from threading import Thread
import hashlib
import hmac

# Config
if 1==1:

    start_asset1 = "BTC"
    start_asset2 = "USDT"
    
    # Color
    c_red = "#ffc0cb"
    c_green = "#d9ffd9"

# Tkinter start
root = tk.Tk()
# This program is based on Frosti2020
root.title ("ChainStigma Binance Trader")
#root.geometry ("1110x615+350+100")
root.geometry ("1110x615")
root.resizable(0, 0)

# Main Assets
if 1==1:
    
    coord_x = 10
    coord_y = 20

    # Background
    bg_main_asset = tk.Label (root, relief="ridge", bg="#559900")
    bg_main_asset.place (x=coord_x, y=coord_y, width=200, height=65)

    def asset_load():

        try:
            save_file = open ("chain_binance.txt").read()

            t_save.delete ("1.0", "end")
            t_save.insert ("1.0", save_file)
            
        except Exception as e:
            t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <LOAD FILE FAIL>\nEXCEPTION: " + str(e) + "\n\n")
            return


        if l_next.cget ("text") == "0":
            
            l_next.configure (text="1")

            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("1.0", "1.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("2.0", "2.end"))

        elif l_next.cget ("text") == "1":
            
            l_next.configure (text="2")

            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("3.0", "3.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("4.0", "4.end"))

        elif l_next.cget ("text") == "2":
            
            l_next.configure (text="3") 
        
            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("5.0", "5.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("6.0", "6.end"))
        
        elif l_next.cget ("text") == "3":
            
            l_next.configure (text="4") 
        
            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("7.0", "7.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("8.0", "8.end"))
        
        elif l_next.cget ("text") == "4":
            
            l_next.configure (text="5") 
        
            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("9.0", "9.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("10.0", "10.end"))
        
        elif l_next.cget ("text") == "5":
            
            l_next.configure (text="1") 
        
            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("1.0", "1.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("2.0", "2.end"))

    def asset_save():
        
        try:
            save_file = open ("chain_binance.txt").read()

            t_save.delete ("1.0", "end")
            t_save.insert ("1.0", save_file)
        
        except:
            t_save.delete ("1.0", "end")
            
            for i in range (1, 13):
                t_save.insert ( str(i) + ".0", "\n")

        if l_next.cget ("text") == "0":
            t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <STATE 0 SAVE NOT POSSIBLE>\n\n")
        elif l_next.cget ("text") == "1":
            t_save.delete ("1.0", "3.0")
            t_save.insert ("1.0", e_main_asset1.get() + "\n")
            t_save.insert ("2.0", e_main_asset2.get() + "\n")
        elif l_next.cget ("text") == "2":
            t_save.delete ("3.0", "5.0")
            t_save.insert ("3.0", e_main_asset1.get() + "\n")
            t_save.insert ("4.0", e_main_asset2.get() + "\n")
        elif l_next.cget ("text") == "3":
            t_save.delete ("5.0", "7.0")
            t_save.insert ("5.0", e_main_asset1.get() + "\n")
            t_save.insert ("6.0", e_main_asset2.get() + "\n")
        elif l_next.cget ("text") == "4":
            t_save.delete ("7.0", "9.0")
            t_save.insert ("7.0", e_main_asset1.get() + "\n")
            t_save.insert ("8.0", e_main_asset2.get() + "\n")
        elif l_next.cget ("text") == "5":
            t_save.delete ("9.0", "11.0")
            t_save.insert ("9.0", e_main_asset1.get() + "\n")
            t_save.insert ("10.0", e_main_asset2.get() + "\n")

        # Save
        new_save = open ("chain_binance.txt" , "w")
        new_save.write (t_save.get("1.0", "13.0"))
        new_save.close()

    e_main_asset1 = tk.Entry(root, font=('Courier New', 14, 'bold'))
    e_main_asset1.place (x=coord_x + 25, y=coord_y + 35, width=75, height=20)
    e_main_asset1.insert (0, start_asset1)

    e_main_asset2 = tk.Entry(root, font=('Courier New', 14, 'bold'))
    e_main_asset2.place (x=coord_x + 110, y=coord_y + 35, width=75, height=20)
    e_main_asset2.insert (0, start_asset2)

    b_main_asset_load = tk.Button (root, font=('Courier New', 10, 'bold'), text="NEXT", command=asset_load)
    b_main_asset_load.place (x=coord_x + 25, y=coord_y + 10, width=60, height=20)

    b_main_asset_save = tk.Button (root, font=('Courier New', 10, 'bold'), text="SAVE", command=asset_save)
    b_main_asset_save.place (x=coord_x + 125, y=coord_y + 10, width=60, height=20)

    l_next = tk.Label(root, text="0", font=('Courier New', 16, 'bold'),relief="ridge", bg="#66CCFF")
    l_next.place (x=coord_x + 92, y=coord_y + 5, width=26, height=26)


# This block instead of here is to be moved under the trailing stop box. In this place is to be added real
# Real time information about the stop loss and take profit and price
#if 1==1:

#    coord_x = 250
#    coord_y = 20
    
    # Background
#    bg_main_loop = tk.Label (root, relief="ridge", bg="#559900")
#    bg_main_loop.place (x=coord_x, y=coord_y, width=200, height=65)

#    class thread_start_price(Thread):
#        def run(self):
#            global running
#            global running_cancel
#            t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S")  + "  Auto Started\n")
#            while (running == True):
#                url_price = "https://api.binance.com/api/v1/ticker/price?symbol=" + e_main_asset1.get().upper() + e_main_asset2.get().upper()
#                    
#                if (running_cancel == True):
#                    t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S")  + "  Auto Stopped\n")
#                    loop_price.delete (0, "end")
#                    break

#                try:
#                    r = requests.get(url=url_price, timeout=4)

#                    the_price = r.json() ["price"]
                
                # Cut Zero and point at end of price
#                    while the_price[-1] == "0":
#                        the_price = the_price[:-1]
#                    if the_price[-1] == ".":
#                        the_price = the_price[:-1]

#                    loop_price.delete (0, "end")
#                    loop_price.insert (0, the_price)

                # Confirmation
#                    b_main_loop_start.configure (bg="green")
#                    time.sleep (0.2)
#                    b_main_loop_start.configure (bg="#FFCC99")

#                    time.sleep(10)

#                except Exception as e:
#                    t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <GET PRICE FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")
#                    break

#    def get_price_start():
#        global running
#        global running_cancel
#        running = True
#        running_cancel = False
#        price_start = thread_start_price()
#        price_start.start()
    
#    def get_price_stop():
#        global running
#        global running_cancel
#        running = False
#        running_cancel = True

#    b_main_loop_start = tk.Button (root, font=('Courier New', 10, 'bold'), text="START", command=get_price_start)
#    b_main_loop_start.place (x=coord_x + 25, y=coord_y + 10, width=60, height=20)

#    b_main_loop_stop = tk.Button (root, font=('Courier New', 10, 'bold'), text="STOP", command=get_price_stop)
#    b_main_loop_stop.place (x=coord_x + 115, y=coord_y + 10, width=60, height=20)

#    loop_price = tk.Entry(root, font=('Courier New', 14, 'bold'))
#    loop_price.place(x=coord_x + 25, y=coord_y + 32, width=150, height=25)

# Price
if 1==1:

    coord_x = 10
    coord_y = 90
    
    # Background
    bg_price = tk.Label (root,relief="ridge", bg="#FFCC99")
    bg_price.place (x=coord_x, y=coord_y, width=230, height=85)

    class thread_get_price(Thread):
        def run(self):

            url_price = "https://api.binance.com/api/v1/ticker/price?symbol=" + e_main_asset1.get().upper() + e_main_asset2.get().upper()
            
            try:
                r = requests.get(url=url_price, timeout=4)

                the_price = r.json() ["price"]
                
                # Cut Zero and point at end of price
                while the_price[-1] == "0":
                    the_price = the_price[:-1]
                if the_price[-1] == ".":
                    the_price = the_price[:-1]

                # Set price
                e_price.delete (0, "end")
                e_price.insert (0, the_price)
                l_price_time.configure (text=time.strftime("%d.%m.%y %H:%M:%S"))

                # Pass price to buy frame
                e_trade_price_buy.delete(0, "end")
                e_trade_price_buy.insert (0, e_price.get())

                # Pass price to sell frame
                e_trade_price_sell.delete(0, "end")
                e_trade_price_sell.insert (0, e_price.get())

                # Confirmation
                bg_price.configure (bg="green")
                time.sleep (0.2)
                bg_price.configure (bg="#FFCC99")

            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <GET PRICE FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def get_price():
        tgp = thread_get_price()
        tgp.start()
        
    def set_price_buy():
        e_trade_price_buy.delete(0, "end")
        e_trade_price_buy.insert (0, e_price.get())
    def set_price_sell():
        e_trade_price_sell.delete(0, "end")
        e_trade_price_sell.insert (0, e_price.get())

    b_price = tk.Button(root, text="Price", command=get_price)
    b_price.place(x=coord_x + 10, y=coord_y + 10, width=50, height=50)

    e_price = tk.Entry(root, font=('Courier New', 14, 'bold'))
    e_price.place(x=coord_x + 70, y=coord_y + 25, width=150, height=25)

    l_price_time = tk.Label(root, text="00.00.00 00:00:00", font=('Courier New', 12, 'bold'), bg="#FFCC99", fg="#6f00ff")
    l_price_time.place (x=coord_x + 10, y=coord_y + 63, height=18)

# Asset1 Funds
if 1==1:

    coord_x = 250
    coord_y = 90
    
    # Background
    bg_asset1 = tk.Label (root,relief="ridge", bg="#99CC99")
    bg_asset1.place (x=coord_x, y=coord_y, width=300, height=85)
    
    def all_funds():
        global check_funds
        check_funds = 1

        ts = thread_assets()
        ts.start()
    
    class thread_assets(Thread):
        def run(self):

            # Time sync
            if e_timesync.get() == "":
                tts = thread_timesync()
                tts.start()
                tts.join()

            t_str = "%.0f" % (time.time() * 1000 + float(e_timesync.get()))

            base_url = "https://api.binance.com/api/v3/account?"
            query = "timestamp=" + t_str

            signature = hmac.new(e_sk.get().encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
            sign_end = "&signature=" + signature

            url_rdy = base_url + query + sign_end
            header = {'X-MBX-APIKEY' : e_ak.get()}

            try:
                r = requests.get (url_rdy, headers=header)

                balance_list = r.json() ["balances"]

                for i in range (0, len(balance_list)):
                    
                    if balance_list[i] ["asset"] == e_main_asset1.get().upper():
                        
                        # Cut Zero and point at end of funds
                        if float(balance_list[i]["free"]) >= 1:
                            free = str(float(balance_list[i]["free"]))
                        elif float(balance_list[i]["free"]) == 0:
                            free = "0.0"
                        else:
                            free = "%.8f" % float(balance_list[i]["free"])
                            
                            while free[-1] == "0":
                                free = free[:-1]

                        if float(balance_list[i]["locked"]) >= 1:
                            locked = str(float(balance_list[i]["locked"]))
                        elif float(balance_list[i]["locked"]) == 0:
                            locked = "0.0"
                        else:
                            locked = "%.8f" % float(balance_list[i]["locked"])
                            
                            while locked[-1] == "0":
                                locked = locked[:-1]

                        l_funds_asset1.configure (text=balance_list[i]["asset"])
                        e_funds_asset1_free.delete(0, "end")
                        e_funds_asset1_free.insert(0, free)
                        e_funds_asset1_locked.delete(0, "end")
                        e_funds_asset1_locked.insert(0, locked)

                    if balance_list[i] ["asset"] == e_main_asset2.get().upper():

                        # Cut Zero and point at end of funds
                        if float(balance_list[i]["free"]) >= 1:
                            free = str(float(balance_list[i]["free"]))
                        elif float(balance_list[i]["free"]) == 0:
                            free = "0.0"
                        else:
                            free = "%.8f" % float(balance_list[i]["free"])
                            
                            while free[-1] == "0":
                                free = free[:-1]

                        if float(balance_list[i]["locked"]) >= 1:
                            locked = str(float(balance_list[i]["locked"]))
                        elif float(balance_list[i]["locked"]) == 0:
                            locked = "0.0"
                        else:
                            locked = "%.8f" % float(balance_list[i]["locked"])
                            
                            while locked[-1] == "0":
                                locked = locked[:-1]

                        l_funds_asset2.configure (text=balance_list[i]["asset"])
                        e_funds_asset2_free.delete(0, "end")
                        e_funds_asset2_free.insert(0, free)
                        e_funds_asset2_locked.delete(0, "end")
                        e_funds_asset2_locked.insert(0, locked)

                    # Check All Funds
                    global check_funds
                    if check_funds == 1:

                        if float(balance_list[i] ["free"]) > 0 or float(balance_list[i] ["locked"]) > 0:

                            # Cut Zero and point at end of funds
                            if float(balance_list[i]["free"]) >= 1:
                                free = str(float(balance_list[i]["free"]))
                            elif float(balance_list[i]["free"]) == 0:
                                free = "0.0"
                            else:
                                free = "%.8f" % float(balance_list[i]["free"])
                                
                                while free[-1] == "0":
                                    free = free[:-1]

                            if float(balance_list[i]["locked"]) >= 1:
                                locked = str(float(balance_list[i]["locked"]))
                            elif float(balance_list[i]["locked"]) == 0:
                                locked = "0.0"
                            else:
                                locked = "%.8f" % float(balance_list[i]["locked"])
                                
                                while locked[-1] == "0":
                                    locked = locked[:-1]

                            t_log.insert ("1.0", balance_list[i]["asset"] + "\n"
                                                + free + "\n"
                                                + locked + "\n\n", "bg_funds")

                if check_funds == 1:
                    t_log.insert ("1.0", "ALL FUNDS:\n")
                    t_log.insert ("1.0", time.strftime(" <%d.%m.%y %H:%M:%S>") + "\n\n", "bg_time")
                   

                check_funds = 0

                # Confirmation
                bg_asset1.configure (bg="green")
                bg_asset2.configure (bg="green")
                time.sleep (0.2)
                bg_asset1.configure (bg="#99CC99")
                bg_asset2.configure (bg="#99CC99")

            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <GET FUNDS FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def amount_assets():
        global check_funds
        check_funds = 0
        
        ts = thread_assets()
        ts.start()
    
    b_funds_asset1 = tk.Button(root, text="Funds", command=amount_assets)
    b_funds_asset1.place(x=coord_x + 10, y=coord_y + 10, width=60, height=20)

    b_funds_allfunds = tk.Button(root, text="All Funds", command=all_funds)
    b_funds_allfunds.place(x=coord_x + 210, y=coord_y + 10, width=80, height=20)

    l_funds_asset1_free = tk.Label(root, text="Free", font=('Courier New', 10, 'bold'), bg="#99CC99")
    l_funds_asset1_free.place (x=coord_x + 10, y=coord_y + 35, height=20)

    l_funds_asset1_locked = tk.Label(root, text="Locked", font=('Courier New', 10, 'bold'), bg="#99CC99")
    l_funds_asset1_locked.place (x=coord_x + 10, y=coord_y + 55, height=20)

    l_funds_asset1 = tk.Label(root, text=start_asset1, font=('Courier New', 14, 'bold'), bg="#99CC99")
    l_funds_asset1.place(x=coord_x + 90, y=coord_y + 10, height=20)

    e_funds_asset1_free = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_funds_asset1_free.place (x=coord_x + 90, y=coord_y + 35, width=200, height=18)

    e_funds_asset1_locked = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_funds_asset1_locked.place (x=coord_x + 90, y=coord_y + 55, width=200, height=18)

# Asset2 Funds
if 1==1:

    coord_x = 560
    coord_y = 90
    
    # Background
    bg_asset2 = tk.Label (root,relief="ridge", bg="#99CC99")
    bg_asset2.place (x=coord_x, y=coord_y, width=300, height=85)
    
    b_funds_asset2 = tk.Button(root, text="Funds", command=amount_assets)
    b_funds_asset2.place(x=coord_x + 10, y=coord_y + 10, width=60, height=20)

    l_funds_asset2_free = tk.Label(root, text="Free", font=('Courier New', 10, 'bold'), bg="#99CC99")
    l_funds_asset2_free.place (x=coord_x + 10, y=coord_y + 35, height=20)

    l_funds_asset2_locked = tk.Label(root, text="Locked", font=('Courier New', 10, 'bold'), bg="#99CC99")
    l_funds_asset2_locked.place (x=coord_x + 10, y=coord_y + 55, height=20)

    l_funds_asset2 = tk.Label(root, text=start_asset2, font=('Courier New', 14, 'bold'), bg="#99CC99")
    l_funds_asset2.place(x=coord_x + 90, y=coord_y + 10, height=20)

    e_funds_asset2_free = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_funds_asset2_free.place (x=coord_x + 90, y=coord_y + 35, width=200, height=18)

    e_funds_asset2_locked = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_funds_asset2_locked.place (x=coord_x + 90, y=coord_y + 55, width=200, height=18)

# % buy/sell order
if 1==1:

    coord_x = 10
    coord_y = 185
    
    # Background
    bg_cal1 = tk.Label (root,relief="ridge", bg="#A9E2F3")
    bg_cal1.place (x=coord_x, y=coord_y, width=230, height=80)

    def set_buy():
        if e_setbuy.get() == "":
            return
        neg_one = -1
        setbuy_result = "%.10f" % (float(e_price.get()) / 100 * (float(e_setbuy.get()) * neg_one) + float(e_price.get()))

        # Max lenght 12 Char
        while len(setbuy_result) > 12:
            setbuy_result = setbuy_result[:-1]

        # Cut Zero and point at end of price
        while setbuy_result[-1] == "0" and setbuy_result.find(".") > -1:
            
            setbuy_result = setbuy_result[:-1]

        if setbuy_result[-1] == ".":
            setbuy_result = setbuy_result[:-1]
        
        e_trade_price_buy.delete(0, "end")
        e_trade_price_buy.insert (0, setbuy_result)
        
    def set_sell():
        if e_setsel.get() == "":
            return

        setsel_result = "%.10f" % (float(e_price.get()) / 100 * float(e_setsel.get()) + float(e_price.get()))

        # Max lenght 12 Char
        while len(setsel_result) > 12:
            setsel_result = setsel_result[:-1]

        # Cut Zero and point at end of price
        while setsel_result[-1] == "0" and setsel_result.find(".") > -1:
            
            setsel_result = setsel_result[:-1]

        if setsel_result[-1] == ".":
            setsel_result = setsel_result[:-1]
        
        e_trade_price_sell.delete(0, "end")
        e_trade_price_sell.insert (0, setsel_result)


    label_percent = "%" + " for buy/sell order:"
    l_calper_free = tk.Label(root, text=label_percent, font=('Courier New', 10, 'bold'), bg="#A9E2F3")
    l_calper_free.place (x=coord_x + 10, y=coord_y + 2, height=20)

    b_setbuy_price = tk.Button(root, text="Set to buy -", command=set_buy)
    b_setbuy_price.place(x=coord_x + 10, y=coord_y + 25, width=70, height=20)    

    b_setsel_price = tk.Button(root, text="Set to sell +", command=set_sell)
    b_setsel_price.place(x=coord_x + 10, y=coord_y + 50, width=70, height=20)    

    e_setbuy = tk.Entry(root, font=('Courier New', 12, 'bold'))
    e_setbuy.place(x=coord_x + 90, y=coord_y + 25, width=100, height=20)

    e_setsel = tk.Entry(root, font=('Courier New', 12, 'bold'))
    e_setsel.place(x=coord_x + 90, y=coord_y + 50, width=100, height=20)

# trailing stop / take profit
if 1==1:

    coord_x = 10
    coord_y = 275
    CheckTrail = 0

    # Background
    bg_cal2 = tk.Label (root,relief="ridge", bg="#A9E2F3")
    bg_cal2.place (x=coord_x, y=coord_y, width=230, height=160)

    def cal2_price():
        e_cal2_value1.delete (0, "end")
        e_cal2_value1.insert (0, e_price.get())

    def cal2_diff():

        if e_cal2_value1.get() == "" or e_cal2_value2.get() == "":
            return

        cal2_result = "%.2f" % (float(e_cal2_value2.get()) / (float(e_cal2_value1.get()) / 100) - 100)
        
        # Cut Zero and point at end of price
        while cal2_result[-1] == "0" and cal2_result.find(".") > -1:
            cal2_result = cal2_result[:-1]

            if cal2_result[-1] == ".":
                cal2_result = cal2_result[:-1]

        # Color the result
        if cal2_result.find('-') == -1:
            
            cal2_result = ("+" + cal2_result + " %")
            l_cal2_result.configure (fg="green")
        
        else:
            
            cal2_result = (cal2_result + " %")
            l_cal2_result.configure (fg="#CD0000")

        # really?
        if len(cal2_result) > 11:
            cal2_result = "really?"

        l_cal2_result.configure (text=cal2_result)

    l_trailing = tk.Label(root, text="Trailing stop loss?", font=('Courier New', 10, 'bold'), bg="#A9E2F3")
    l_trailing.place(x=coord_x + 10, y=coord_y + 10, height=20)

    b_trailing = tk.Checkbutton(root, variable=CheckTrail, onvalue=1, offvalue=0, bg="#A9E2F3")
    b_trailing.place(x=coord_x + 180, y=coord_y + 10, height=20)

    label_limit = "limit  " + "%:" 
    l_limit = tk.Label(root, text=label_limit, font=('Courier New', 10, 'bold'), bg="#A9E2F3")
    l_limit.place(x=coord_x + 10, y=coord_y + 32, height=20)

    e_limit = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_limit.place(x=coord_x + 90, y=coord_y + 32, width=100, height=18)

    label_stop = "stop   " + "%:" 
    l_stop = tk.Label(root, text=label_stop, font=('Courier New', 10, 'bold'), bg="#A9E2F3")
    l_stop.place(x=coord_x + 10, y=coord_y + 55,height=20)

    e_stop = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_stop.place(x=coord_x + 90, y=coord_y + 55, width=100, height=18)

    label_profit = "profit " + "%:" 
    l_profit = tk.Label(root, text=label_profit, font=('Courier New', 10, 'bold'), bg="#A9E2F3")
    l_profit.place(x=coord_x + 10, y=coord_y + 77,height=20)

    e_profit = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_profit.place(x=coord_x + 90, y=coord_y + 77, width=100, height=18)

# Trade buy
if 1==1:

    coord_x = 250
    coord_y = 185

    # Background
    bg_trade_buy = tk.Label (root,relief="ridge", bg=c_green)
    bg_trade_buy.place (x=coord_x, y=coord_y, width=300, height=105)

    def order_buy():

        if e_trade_price_buy.get() == "" or e_trade_amount_buy.get() == "":
            return
        
        global the_side, the_price, the_amount
        the_side = "BUY"
        the_price = e_trade_price_buy.get()
        the_amount = e_trade_amount_buy.get()

        tt = thread_trades()
        tt.start()

    b_trade_buy = tk.Button(root, text="BUY", command=order_buy)
    b_trade_buy.place(x=coord_x + 90 , y=coord_y + 10, width=200, height=20)

    l_trade_price_buy = tk.Label(root, text="Price", font=('Courier New', 10, 'bold'), bg=c_green)
    l_trade_price_buy.place (x=coord_x + 10, y=coord_y + 35, height=18)
    
    l_trade_amount_buy = tk.Label(root, text="Amount", font=('Courier New', 10, 'bold'), bg=c_green)
    l_trade_amount_buy.place (x=coord_x + 10, y=coord_y + 55, height=18)

    l_trade_id_buy = tk.Label(root, text="ID", font=('Courier New', 10, 'bold'), bg=c_green)
    l_trade_id_buy.place (x=coord_x + 10, y=coord_y + 75, height=18)

    e_trade_price_buy = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_price_buy.place (x=coord_x + 90, y=coord_y + 35, width=200, height=18)

    e_trade_amount_buy = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_amount_buy.place (x=coord_x + 90, y=coord_y + 55, width=200, height=18)

    e_trade_id_buy = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_id_buy.place (x=coord_x + 90, y=coord_y + 75, width=200, height=18)

# Trade sell
if 1==1:

    coord_x = 560
    coord_y = 185

    # Background
    bg_trade_sell = tk.Label (root,relief="ridge", bg=c_red)
    bg_trade_sell.place (x=coord_x, y=coord_y, width=300, height=105)

    def order_sell():

        if e_trade_price_sell.get() == "" or e_trade_amount_sell.get() == "":
            return
        
        global the_side, the_price, the_amount
        the_side = "SELL"
        the_price = e_trade_price_sell.get()
        the_amount = e_trade_amount_sell.get()

        tt = thread_trades()
        tt.start()

    class thread_trades(Thread):
        def run(self):

            global the_side, the_price, the_amount
           
            # Time sync
            if e_timesync.get() == "":
                tts = thread_timesync()
                tts.start()
                tts.join()

            t_str = "%.0f" % (time.time() * 1000 + float(e_timesync.get()))

            base_url = "https://api.binance.com/api/v3/order?"

            symbol = "symbol=" + e_main_asset1.get().upper() + e_main_asset2.get().upper()
            side = "&side=" + the_side
            the_type = "&type=LIMIT"
            timeinforce = "&timeInForce=GTC"
            amount = "&quantity=" + the_amount
            price = "&price=" + the_price
            zeit = "&timestamp=" + t_str
            query = symbol + side + the_type + timeinforce + amount + price + zeit

            signature = hmac.new(e_sk.get().encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
            sign_end = "&signature=" + signature

            url_rdy = base_url + query + sign_end
            header = {'X-MBX-APIKEY' : e_ak.get()}

            try:
                r = requests.post (url_rdy, headers=header, timeout=4)

                # BG for order
                if r.json() ["side"] == "BUY":
                    bg_use = "bg_green"
                else:
                    bg_use = "bg_red"

                t_log.insert ("1.0",   "ORDER " + the_side + ":\n"
                                        + "ID    : " + str(r.json() ["orderId"]) + "\n"
                                        + "PRICE : "  + str(float(r.json() ["price"])) + "\n"
                                        + "AMOUNT: " + str(float(r.json() ["origQty"])) + "\n"
                                        + "FILLED: " + str(float(r.json() ["executedQty"])) + "\n\n", bg_use)

                t_log.insert ("1.0", time.strftime(" <%d.%m.%y %H:%M:%S>") + "\n\n", "bg_time")

                if the_side == "BUY":
                    e_trade_price_buy.delete (0, "end")
                    e_trade_amount_buy.delete (0, "end")
                    e_trade_id_buy.delete (0, "end")
                    e_trade_id_buy.insert (0, r.json() ["orderId"])
                else:
                    e_trade_price_sell.delete (0, "end")
                    e_trade_amount_sell.delete (0, "end")
                    e_trade_id_sell.delete (0, "end")
                    e_trade_id_sell.insert (0, r.json() ["orderId"])

                # Confirmation
                if the_side == "BUY":
                    bg_trade_buy.configure (bg="green")
                    time.sleep (0.2)
                    bg_trade_buy.configure (bg=c_green)
                else:
                    bg_trade_sell.configure (bg="green")
                    time.sleep (0.2)
                    bg_trade_sell.configure (bg=c_red)
            
            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <ORDER " + the_side + " FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")
    
    b_trade_sell = tk.Button(root, text="SELL", command=order_sell)
    b_trade_sell.place(x=coord_x + 90 , y=coord_y + 10, width=200, height=20)

    l_trade_price_sell = tk.Label(root, text="Price", font=('Courier New', 10, 'bold'), bg=c_red)
    l_trade_price_sell.place (x=coord_x + 10, y=coord_y + 35, height=18)
    
    l_trade_amount_sell = tk.Label(root, text="Amount", font=('Courier New', 10, 'bold'), bg=c_red)
    l_trade_amount_sell.place (x=coord_x + 10, y=coord_y + 55, height=18)

    l_trade_id_sell = tk.Label(root, text="ID", font=('Courier New', 10, 'bold'), bg=c_red)
    l_trade_id_sell.place (x=coord_x + 10, y=coord_y + 75, height=18)

    e_trade_price_sell = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_price_sell.place (x=coord_x + 90, y=coord_y + 35, width=200, height=18)

    e_trade_amount_sell = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_amount_sell.place (x=coord_x + 90, y=coord_y + 55, width=200, height=18)

    e_trade_id_sell = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_id_sell.place (x=coord_x + 90, y=coord_y + 75, width=200, height=18)

# Order ID Info
if 1==1:

    coord_x = 250
    coord_y = 300

    # Background
    bg_idinfo = tk.Label (root,relief="ridge", bg="#F5DA81")
    bg_idinfo.place (x=coord_x, y=coord_y, width=300, height=145)

    class thread_id_info(Thread):
        def run(self):

            if e_idinfo.get() == "":
                return

            # Time sync
            if e_timesync.get() == "":
                tts = thread_timesync()
                tts.start()
                tts.join()

            t_str = "%.0f" % (time.time() * 1000 + float(e_timesync.get()))

            base_url = "https://api.binance.com/api/v3/order?"

            symbol = "symbol=" + e_main_asset1.get().upper() + e_main_asset2.get().upper()
            orderid = "&orderId=" + e_idinfo.get()
            q_time = "&timestamp=" + t_str
            query = symbol + orderid + q_time

            signature = hmac.new(e_sk.get().encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
            sign_end = "&signature=" + signature

            url_rdy = base_url + query + sign_end
            header = {'X-MBX-APIKEY' : e_ak.get()}

            try:
                r = requests.get (url_rdy, headers=header, timeout=4)
                
                l_idinfo_side.configure (text=r.json() ["side"])
                l_idinfo_price.configure (text=str(float(r.json() ["price"])))
                l_idinfo_amount.configure (text=str(float(r.json() ["origQty"])))
                l_idinfo_filled.configure (text=str(float(r.json() ["executedQty"])))
                l_idinfo_status.configure (text=r.json() ["status"])
                
                # Confirmation
                bg_idinfo.configure (bg="green")
                time.sleep (0.2)
                bg_idinfo.configure (bg="#F5DA81")

            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <GET ID-INFO FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def id_info():
        tii = thread_id_info()
        tii.start()

    def id_info_add():

        e_idinfo.delete (0, "end")
        try:
            e_idinfo.insert (0, e_trade_id_buy.selection_get())
        except:
            try:
                e_idinfo.insert (0, e_trade_id_sell.selection_get())
            except:
                try:
                    e_idinfo.insert (0, t_log.selection_get())
                except:
                    pass

    b_idinfo = tk.Button(root, text="ID-Info", command=id_info)
    b_idinfo.place(x=coord_x + 10 , y=coord_y + 10, width=60, height=18)

    b_idinfo_buy = tk.Button(root, text="ADD", command=id_info_add)
    b_idinfo_buy.place(x=coord_x + 90 , y=coord_y + 10, width=40, height=18)

    e_idinfo = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_idinfo.place (x=coord_x + 135, y=coord_y + 10, width=155, height=18)

    l_idinfo_name_side = tk.Label(root, text="Side", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_name_side.place (x=coord_x + 10, y=coord_y + 35, height=18)

    l_idinfo_name_price = tk.Label(root, text="Price", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_name_price.place (x=coord_x + 10, y=coord_y + 55, height=18)
    
    l_idinfo_name_amount = tk.Label(root, text="Amount", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_name_amount.place (x=coord_x + 10, y=coord_y + 75, height=18)

    l_idinfo_name_filled = tk.Label(root, text="Filled", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_name_filled.place (x=coord_x + 10, y=coord_y + 95, height=18)

    l_idinfo_name_status = tk.Label(root, text="Status", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_name_status.place (x=coord_x + 10, y=coord_y + 115, height=18)

    l_idinfo_side = tk.Label(root, text="BUY / SELL", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_side.place (x=coord_x + 90, y=coord_y + 35, height=18)

    l_idinfo_price = tk.Label(root, text="0000.00", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_price.place (x=coord_x + 90, y=coord_y + 55, height=18)
    
    l_idinfo_amount = tk.Label(root, text="0000.00000000", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_amount.place (x=coord_x + 90, y=coord_y + 75, height=18)

    l_idinfo_filled = tk.Label(root, text="0000.00000000", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_filled.place (x=coord_x + 90, y=coord_y + 95, height=18)

    l_idinfo_status = tk.Label(root, text="FILLED / CANCEL", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_status.place (x=coord_x + 90, y=coord_y + 115, height=18)

# Cancel Order 
if 1==1:

    coord_x = 560
    coord_y = 300

    # Background
    bg_order_cancel = tk.Label (root,relief="ridge", bg="#e7d7cc")
    bg_order_cancel.place (x=coord_x, y=coord_y, width=300, height=40)

    class thread_order_cancel(Thread):
        def run(self):

            if e_order_cancel.get() == "":
                return

            # Time sync
            if e_timesync.get() == "":
                tts = thread_timesync()
                tts.start()
                tts.join()
            
            t_str = "%.0f" % (time.time() * 1000 + float(e_timesync.get()))

            base_url = "https://api.binance.com/api/v3/order?"
            symbol = "symbol=" + e_main_asset1.get().upper() + e_main_asset2.get().upper()
            orderid = "&orderId=" + e_order_cancel.get()
            q_time = "&timestamp=" + t_str
            query = symbol + orderid + q_time

            signature = hmac.new(e_sk.get().encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
            sign_end = "&signature=" + signature

            url_rdy = base_url + query + sign_end
            header = {'X-MBX-APIKEY' : e_ak.get()}

            try:
                r = requests.delete (url_rdy, headers=header)

                t_log.insert ("1.0",   "ORDER CANCELED:\n"
                                        + "ID    : " + str(r.json() ["orderId"]) + "\n"
                                        + "SIDE  : "  + r.json() ["side"] + "\n"
                                        + "PRICE : "  + str(float(r.json() ["price"])) + "\n"
                                        + "AMOUNT: " + str(float(r.json() ["origQty"])) + "\n"
                                        + "FILLED: " + str(float(r.json() ["executedQty"])) + "\n\n", "bg_cancel")


                t_log.insert ("1.0", time.strftime(" <%d.%m.%y %H:%M:%S>") + "\n\n", "bg_time")
                e_order_cancel.delete (0, "end")

                # Confirmation
                bg_order_cancel.configure (bg="green")
                time.sleep (0.2)
                bg_order_cancel.configure (bg="#e7d7cc")
            
            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <ORDER CANCEL FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def order_cancel():
        toc = thread_order_cancel()
        toc.start()

    def order_cancel_add():

        e_order_cancel.delete (0, "end")
        try:
            e_order_cancel.insert (0, e_trade_id_buy.selection_get())
        except:
            try:
                e_order_cancel.insert (0, e_trade_id_sell.selection_get())
            except:
                try:
                    e_order_cancel.insert (0, t_log.selection_get())
                except:
                    pass

    b_order_cancel = tk.Button(root, text="ID-Cancel", command=order_cancel)
    b_order_cancel.place(x=coord_x + 10 , y=coord_y + 10, width=70, height=18)

    b_order_cancel_buy = tk.Button(root, text="ADD", command=order_cancel_add)
    b_order_cancel_buy.place(x=coord_x + 90 , y=coord_y + 10, width=40, height=18)

    e_order_cancel = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_order_cancel.place (x=coord_x + 135, y=coord_y + 10, width=155, height=18)

# Show all Order from Pair
if 1==1:

    coord_x = 560
    coord_y = 350

    # Background
    bg_allorder = tk.Label (root,relief="ridge", bg="#F5DA81")
    bg_allorder.place (x=coord_x, y=coord_y, width=300, height=40)

    class thread_all_order(Thread):
        def run(self):

            # Time sync
            if e_timesync.get() == "":
                tts = thread_timesync()
                tts.start()
                tts.join()
            
            t_str = "%.0f" % (time.time() * 1000 + float(e_timesync.get()))

            base_url = "https://api.binance.com/api/v3/openOrders?"

            symbol = "symbol=" + e_main_asset1.get().upper() + e_main_asset2.get().upper()
            q_time = "&timestamp=" + t_str
            query = symbol + q_time

            signature = hmac.new(e_sk.get().encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
            sign_end = "&signature=" + signature

            url_rdy = base_url + query + sign_end
            header = {'X-MBX-APIKEY' : e_ak.get()}

            try:
                r = requests.get (url_rdy, headers=header)

                if len(r.json()) > 0: 

                    # Order count
                    l_allorder_count.configure (text=len(r.json()))   

                    for i in range (0, len(r.json())):
                        
                        # BG for order
                        if r.json() [i] ["side"] == "BUY":
                            bg_use = "bg_green"
                        else:
                            bg_use = "bg_red"

                        t_log.insert ("1.0",   "ID    : " + str(r.json() [i] ["orderId"]) + "\n"
                                             + "SIDE  : "  + r.json() [i] ["side"] + "\n"
                                             + "PRICE : "  + str(float(r.json() [i] ["price"])) + "\n"
                                             + "AMOUNT: " + str(float(r.json() [i] ["origQty"])) + "\n"
                                             + "FILLED: " + str(float(r.json() [i] ["executedQty"])) + "\n\n", bg_use)

                else:

                    # Order count
                    l_allorder_count.configure (text="00")   
                    t_log.insert ("1.0", "NO OPEN ORDER:\n" + e_main_asset1.get().upper() + "/" + e_main_asset2.get().upper() + "\n\n")

                t_log.insert ("1.0", "ALL OPEN ORDER:\n" +  e_main_asset1.get().upper() + "/" + e_main_asset2.get().upper() + "\n")
                t_log.insert ("1.0", time.strftime(" <%d.%m.%y %H:%M:%S>") + "\n\n", "bg_time")
            
                # Confirmation
                bg_allorder.configure (bg="green")
                time.sleep (0.2)
                bg_allorder.configure (bg="#F5DA81")

            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <GET ALL ORDER FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def all_order():
        tao = thread_all_order()
        tao.start()

    b_allorder = tk.Button (root, text="Show all open order from pair", command=all_order)
    b_allorder.place(x=coord_x + 10 , y=coord_y + 10, width=240, height=20)

    l_allorder_count = tk.Label (root, text="00", font=('Courier New', 16, 'bold'), bg="#F5DA81")
    l_allorder_count.place(x=coord_x + 255 , y=coord_y + 10, width=40, height=20)

# Time Sync
if 1==1:

    coord_x = 560
    coord_y = 400

    # Background
    bg_timesync = tk.Label (root,relief="ridge", bg="#F5DA81")
    bg_timesync.place (x=coord_x, y=coord_y, width=300, height=45)

    class thread_timesync(Thread):
        def run(self):

            try:

                r = requests.get ("https://api.binance.com/api/v1/time", timeout=4)
                
                pc_time = int(time.time() * 1000)
                servertime = int(r.json() ["serverTime"])
                diff = servertime - pc_time

                e_timesync.delete (0, "end")
                e_timesync.insert (0, diff)

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S")  + "  <TIME SYNC>\nservertime: " + str(servertime) + "\npc time:    " + str(pc_time) + "\ndiff:       " + str(diff) + "\n\n" )
                
            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <TIME SYNC FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def timesync():

        tts = thread_timesync()
        tts.start()

    b_timesync = tk.Button(root, text="Time Sync", command=timesync)
    b_timesync.place(x=coord_x + 10 , y=coord_y + 10, width=100, height=23)

    e_timesync = tk.Entry (root, font=('Courier New', 10, 'bold'))
    e_timesync.place (x=coord_x + 120, y=coord_y + 10, width=170, height=23)

# Buttons
if 1==1:

    coord_x = 10
    coord_y = 630

    def scanning():
        if running:
             t_log.insert ("1.0", "scanning")
        
        tk.after(1000, scanning)
        
    def start():
        global running
        running == True
        t_log.insert ("1.0", "scanning")

    def stop():
        global running
        running == False

    b_start = tk.Button (root, font=('Courier New', 10, 'bold'), text="START", command=start)
    b_start.place (x=coord_x, y=coord_y, height=18)
    
    b_cancel = tk.Button (root, font=('Courier New', 10, 'bold'), text="CANCEL", command=stop)
    b_cancel.place (x=coord_x + 100, y=coord_y, height=18)

# Log Textfield
if 1==1:

    coord_x = 870
    coord_y = 20

    # Background
    bg_logfield = tk.Label (root,relief="ridge", bg="#000000")
    bg_logfield.place (x=coord_x, y=coord_y, width=230, height=585)

    t_log = tk.Text (root,  font=('Courier New', 10, 'bold'))
    t_log.place(x=873, y=23, width=224, height=579)

    #BG tags for logfield
    t_log.tag_config ("bg_time", background="#d0d0d0" )
    t_log.tag_config ("bg_green", background="#d9ffd9" )
    t_log.tag_config ("bg_red", background="#ffc0cb" )
    t_log.tag_config ("bg_funds", background="#99CC99" )
    t_log.tag_config ("bg_cancel", background="#e7d7cc" )

    #Temp Textfield for load chain_binance.txt
    t_save = tk.Text (root)

# Request Textfield
if 1==1:

    t_request = tk.Text (root,  font=('Courier New', 9, 'bold'), bg="#d0d0d0")
    t_request.place(x=10, y=455, width=850, height=150)

# Keys
if 1==1:

    coord_x = 10
    coord_y = 630

    def show_keys():

        if b_keys.cget ("text") == ".":
            root.geometry ("1110x815")
            b_keys.configure (text="")
        else:
            root.geometry ("1110x615")
            b_keys.configure (text=".")

    def keys_load():

        try:
            save_file = open ("chain_binance.txt").read()

            t_save.delete ("1.0", "end")
            t_save.insert ("1.0", save_file)

            if t_save.get ("11.0", "11.end") == "" or t_save.get ("12.0", "12.end") == "":
                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <NO DATA SAVED>" + "\n\n")
                return
            
        except Exception as e:
            t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <LOAD FILE FAIL>\nEXCEPTION: " + str(e) + "\n\n")
            return

        e_ak.delete (0, "end")
        e_ak.insert (0, t_save.get ("11.0", "11.end"))
        e_sk.delete (0, "end")
        e_sk.insert (0, t_save.get ("12.0", "12.end"))

    def keys_save():
    
        try:
            save_file = open ("chain_binance.txt").read()

            t_save.delete ("1.0", "end")
            t_save.insert ("1.0", save_file)
        
        except:
            t_save.delete ("1.0", "end")
            
            for i in range (1, 13):
                t_save.insert ( str(i) + ".0", "\n")

        t_save.delete ("11.0", "12.end")
        t_save.insert ("11.0", e_ak.get())
        t_save.insert ("12.0", e_sk.get())

        new_save = open ("chain_binance.txt" , "w")
        new_save.write (t_save.get("1.0", "13.0"))
        new_save.close()

    b_keys = tk.Button(root, text=".", command=show_keys)
    b_keys.place (x=0 , y=605, width=10, height=10)

    l_akey = tk.Label(root, text="A-Key:", font=('Courier New', 10, 'bold'))
    l_akey.place (x=coord_x, y=coord_y, height=20)

    l_skey = tk.Label(root, text="S-Key:", font=('Courier New', 10, 'bold'))
    l_skey.place (x=coord_x, y=coord_y + 25, height=20)

    e_ak = tk.Entry (root, font=('Courier New', 10, 'bold'))
    e_ak.place (x=coord_x + 70 , y=coord_y, width=800, height=20)

    e_sk = tk.Entry (root, font=('Courier New', 10, 'bold'))
    e_sk.place (x=coord_x + 70 , y=coord_y + 25, width=800, height=20)

    b_keys_save = tk.Button(root, text="SAVE", bg="#d0d0d0", command=keys_save)
    b_keys_save.place (x=coord_x + 880 , y=coord_y, width=50, height=18)

    b_keys_load = tk.Button(root, text="LOAD", bg="#d0d0d0", command=keys_load)
    b_keys_load.place (x=coord_x + 880 , y=coord_y + 25, width=50, height=18)

# Load Keys when saved
if 1==1:
    keys_load()

root.mainloop()
end_thread_time = 0