def walk(path):
    result = ""
    i = 0
    if path == "":
        return "Paused"
    while i < len(path):
        directions = { "left" : 0, "right" : 0, "up" : 0, "down" : 0}
        if i < len(path) and path[i] == "<":
            while i < len(path) and path[i] == "<" :
                directions["left"] += 1
                i += 1
            if directions['left'] == 1:
                result += f"Take {directions['left']} step left"
            else:
                result += f"Take {directions['left']} steps left"
        if i < len(path) and path[i] == "^":
            while i < len(path) and path[i] == "^":
                directions["up"] += 1
                i += 1
            if directions['up'] == 1:
                result += f"Take {directions['up']} step up"
            else:
                result += f"Take {directions['up']} steps up"
        if i < len(path) and path[i] == ">":
            while i < len(path) and path[i] == ">":
                directions["right"] += 1
                i += 1
            if directions['right'] == 1:
                result += f"Take {directions['right']} step right"
            else:
                result += f"Take {directions['right']} steps right"
        if i < len(path) and path[i] == "v":
            while i < len(path) and path[i] == "v":
                directions["down"] += 1
                i += 1
            if directions['down'] == 1:
                result += f"Take {directions['down']} step down"
            else:
                result += f"Take {directions['down']} steps down"
    y = 0
    for x in range(len(result)):
        y +=1
        if y < len(result) and "T" == result[y] and y != 0:
            result = result[:y] + "\n" + result[y:]
            if result[y+1] == "T":
                y+=2
    return result
print(walk("v"))