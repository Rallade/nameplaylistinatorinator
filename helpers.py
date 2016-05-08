import json

def json_to_dict(jsonData):
    return json.loads(jsonData)

def adjectives_to_int(adjectives_list):
    i = 0
    int_list = []
    for adjective in adjectives_list:
        int_list.append(i)
        i += 1
    return int_list

if __name__ == "__main__":
    pass
