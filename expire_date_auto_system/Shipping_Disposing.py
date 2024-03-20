import socket
import pickle

from shared_module import milk, snack_food, gum, my_addr, today

def outmilk():
    if len(milk) > 0:
        milk.pop(0)
        my_list = [-1, 'milk', len(milk)]

        receiver_ip = my_addr  # 서버 ip로 변경해야함
        receiver_port = 10000

        sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sender_socket.connect((receiver_ip, receiver_port))

        data = pickle.dumps(my_list)
        sender_socket.sendall(data)

        sender_socket.close()


def outsnack():
    if len(snack_food) > 0:
        snack_food.pop(0)
        my_list = [-1, 'snack', len(snack_food)]

        receiver_ip = my_addr  # 서버 ip로 변경해야함
        receiver_port = 10000

        sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sender_socket.connect((receiver_ip, receiver_port))

        data = pickle.dumps(my_list)
        sender_socket.sendall(data)

        sender_socket.close()


def outgum():
    if len(gum) > 0:
        gum.pop(0)
        my_list = [-1, 'gum', len(gum)]

        receiver_ip = my_addr  # 서버 ip로 변경해야함
        receiver_port = 10000

        sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sender_socket.connect((receiver_ip, receiver_port))

        data = pickle.dumps(my_list)
        sender_socket.sendall(data)

        sender_socket.close()