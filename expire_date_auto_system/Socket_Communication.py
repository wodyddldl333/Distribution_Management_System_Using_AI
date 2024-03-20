import socket
import pickle
import shutil

from ProductMangement import Product_Info
from yolo_module import detect_expiry_date
from shared_module import milk, snack_food, gum, my_addr, today

def scan_product():
    detect_expiry_date()
    product = Product_Info()

    if 'milk' in product.info:
        milk.append(product.expirydate)
        milk.sort()
        my_list = ['milk', milk.index(product.expirydate), len(milk)]
    elif 'snack' in product.info:
        snack_food.append(product.expirydate)
        snack_food.sort()
        my_list = ['milk', snack_food.index(product.expirydate), len(snack_food)]
    else:
        gum.append(product.expirydate)
        gum.sort()
        my_list = ['milk', gum.index(product.expirydate), len(gum)]

    receiver_ip = my_addr  # 서버 ip로 변경해야함
    receiver_port = 10000

    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sender_socket.connect((receiver_ip, receiver_port))

    data = pickle.dumps(my_list)
    sender_socket.sendall(data)

    sender_socket.close()

    # rm detection images
    shutil.rmtree('runs/detect')

    return [my_list[0], product.expirydate]