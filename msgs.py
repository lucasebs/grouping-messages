import json
from datetime import datetime, timedelta

with open("U1ZQR43RB.json", "r") as read_file:
    data = json.load(read_file)

users = {}

def dict_text_per_time(ts, message):
    m = []
    m.append(message)
    aux_dict = {}
    aux_dict[ts] = m
    return aux_dict

for i in range(len(data)):
    if 'user' in data[i].keys():
        ts = data[i]['ts']
        message = data[i]['text']
        user = data[i]['user']
        if message != "":
            if user not in users.keys():
                users[user] = dict_text_per_time(ts,message)
            else:
                dt = datetime.fromtimestamp(int(float(ts)))
                last_ts_str = list(users[user].keys())[-1]
                last_ts_int = int(float(last_ts_str))
                last_dt = datetime.fromtimestamp(last_ts_int)
                if dt > (last_dt + timedelta(minutes=2)):                    
                    users[user].update(dict_text_per_time(ts,message))
                else:
                    users[user][last_ts_str].append(message)
                      
for user in users.keys():
    with open("outputs/"+user+".json", "w") as write_file:
        json.dump(users[user],write_file)
