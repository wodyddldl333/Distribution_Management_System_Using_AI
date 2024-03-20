# Controller GUI
import socket
import pickle
import tkinter as tk
from tkinter import messagebox

from Shipping_Disposing import outsnack, outgum, outmilk
from Socket_Communication import scan_product
from shared_module import milk, snack_food, gum, my_addr, today

window = tk.Tk()
text_box = tk.Text(window, height=10, width=30)

def add_text():
    temp = scan_product()
    update_text()
    messagebox.showinfo("입고", "제품명 : " + temp[0] + "\n유통기한 : " + temp[1] + "\n 제품추가 완료")


def update_text():
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, 'The stock of milk : ' + str(len(milk)) + "\n")
    entered_text = "\n".join(milk)
    text_box.insert(tk.END, entered_text + "\n")
    text_box.insert(tk.END, "\n" + 'The stock of snack : ' + str(len(snack_food)) + "\n")
    entered_text = "\n".join(snack_food)
    text_box.insert(tk.END, entered_text + "\n")
    text_box.insert(tk.END, "\n" + 'The stock of gum : ' + str(len(gum)) + "\n")
    entered_text = "\n".join(gum)
    text_box.insert(tk.END, entered_text + "\n")


def delete_milk():
    outmilk()
    text_box.delete("1.0", tk.END)
    update_text()


def delete_snack():
    outsnack()
    text_box.delete("1.0", tk.END)
    update_text()


def delete_gum():
    outgum()
    text_box.delete("1.0", tk.END)
    update_text()


def trash():
    global milk, snack_food, gum
    lom = len(milk);
    los = len(snack_food);
    logu = len(gum)
    milk = [i for i in milk if int(i) > today]
    snack_food = [i for i in snack_food if int(i) > today]
    gum = [i for i in gum if int(i) > today]
    my_list = [-2, lom, lom - len(milk), los, los - len(snack_food), logu, logu - len(gum)]
    receiver_ip = my_addr  # 서버 ip로 변경해야함
    receiver_port = 10000

    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sender_socket.connect((receiver_ip, receiver_port))

    data = pickle.dumps(my_list)
    sender_socket.sendall(data)

    sender_socket.close()
    print(my_list)
    # 로봇팔 정렬되어있으니깐 2개
    update_text()


def open_new_window():
    new_window = tk.Toplevel(window)
    new_window.title("Admin Mode")
    new_window.geometry("1200x800")

def openGUI():
    window.geometry("1024x600")
    # 텍스트 박스
    text_box.place(x=85, y=50)
    text_box.configure(font=("Arial", 20))

    text_box.insert(tk.END, 'The stock of milk : ' + str(len(milk)) + "\n")
    entered_text = "\n".join(milk)
    text_box.insert(tk.END, entered_text + "\n")
    text_box.insert(tk.END, "\n" + 'The stock of snack : ' + str(len(snack_food)) + "\n")
    entered_text = "\n".join(snack_food)
    text_box.insert(tk.END, entered_text + "\n")
    text_box.insert(tk.END, "\n" + 'The stock of gum : ' + str(len(gum)) + "\n")
    entered_text = "\n".join(gum)
    text_box.insert(tk.END, entered_text + "\n")

    add_button = tk.Button(window, text="Stocking(Scan)", height=2, width=15, command=add_text)
    add_button.place(x=700, y=50)

    label = tk.Label(window, text="Shipping")
    label.place(x=750, y=110)

    milk_button = tk.Button(window, text="Milk(Shipping)", command=delete_milk, height=2, width=15)
    milk_button.place(x=700, y=135)

    snack_button = tk.Button(window, text="Snack(Shipping)", command=delete_snack, height=2, width=15)
    snack_button.place(x=700, y=200)

    gum_button = tk.Button(window, text="Gum(Shipping)", command=delete_gum, height=2, width=15)
    gum_button.place(x=700, y=265)

    trash_button = tk.Button(window, text="Disposing", height=2, width=15, command=trash)
    trash_button.place(x=700, y=350)

    # 메뉴바 생성
    menubar = tk.Menu(window)

    # 파일 메뉴
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="관리자모드", command=open_new_window)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="Mode", menu=file_menu)

    # 윈도우에 메뉴바 설정
    window.config(menu=menubar)

    # 메인 루프 시작
    window.mainloop()