import socket
import threading
import sqlite3

port = 5470
SERVER = "207.154.246.228"
print(SERVER)
ADDR = (SERVER, port)
HEADER = 8
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def retrieve_elo_from_database(steam_id_list):
    con = sqlite3.connect("db.sqlite3")
    cursor = con.cursor()
    elo_list = []
    for steam_id in steam_id_list:

        for row in cursor.execute("SELECT * from csgo_csgoplayer"):
            if row[7] == steam_id:
                elo_list.append(row[2])
                break
    
    con.close()
    return elo_list


def store_info_in_database(stats):
    con = sqlite3.connect("db.sqlite3")
    cursor = con.cursor()
    
    for player in stats:
        current_stats = cursor.execute(f"SELECT * from csgo_csgoplayer WHERE steam_id = '{player}'")

        played_matches = 1

        for row in current_stats:
            stats[player][1] += row[3]
            stats[player][2] += row[4]
            stats[player][3] += row[5]
            played_matches += row[6]

        cursor.execute(f"UPDATE csgo_csgoplayer SET elo = {stats[player][0]} WHERE steam_id = '{player}'")
        cursor.execute(f"UPDATE csgo_csgoplayer SET kills = {stats[player][1]} WHERE steam_id = '{player}'")
        cursor.execute(f"UPDATE csgo_csgoplayer SET assists = {stats[player][2]} WHERE steam_id = '{player}'")
        cursor.execute(f"UPDATE csgo_csgoplayer SET deaths = {stats[player][3]} WHERE steam_id = '{player}'")
        cursor.execute(f"UPDATE csgo_csgoplayer SET played_matches = {played_matches} WHERE steam_id = '{player}'")

    con.commit()
    con.close()

    return "Data stored!"


def parse_old_elo(elo_list):
    elo_string = ""

    for elo in elo_list:
        elo_string += f"{elo}/"

    elo_string = elo_string[:-1]

    return elo_string

def parse_new_stats(msg):
    new_stats = {}

    player_list = msg.split("/")
    for player in player_list:
        player_split = player.split("$")
        new_stats[player_split[0]] = player_split[1]

    for key in new_stats:
        new_stats[key] = new_stats[key].split(":")
        value_list = []
        for value in new_stats[key]:
            value_list.append(value)
        value_list = [int(x) for x in value_list]
        new_stats[key] = value_list
    
    return new_stats


def handle_client(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)

        print(msg)

        steam_id_list = msg.split("/")
        elo_list = retrieve_elo_from_database(steam_id_list)

        elo_string = parse_old_elo(elo_list)

        conn.send(elo_string.encode(FORMAT))

        msg2_length = conn.recv(HEADER)
        msg2_length = int(msg2_length)
        msg2 = conn.recv(msg2_length).decode(FORMAT)

        new_stats = parse_new_stats(msg2)
        print(new_stats)

        store_info_in_database(new_stats)

        connected = False


def start():
    server.listen()
    print("Server started...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start()
