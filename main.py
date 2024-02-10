import re

list = list()
def hohuman(x:str,y:str):
    if (x == "" and y != ""):
        print(f"1111{y}")
        return y
    elif (y == "" and x != ""):
        print(f"2222{x}")
        return x
    elif (x == "1" and y == "1"):
        print("3")
    else:
        x = "1" + x
        y = "1" + y 
        print(x)
        print(y)
        if len(x) == 2 and len(y) == 2:
            print("41")
            print(f"{y[1:]}{x[len(x) - 1]}+{x[1:]}{y[len(y) - 1]}")
            return  y[1:] + x[len(x) - 1] + "+" + x[1:] + y[len(y) - 1]
        elif len(x) == 2 and len(y) != 2:
            print("42")
            print(f"{y[1:]}{x[len(x) - 1]}+({x[1:]},{y[1:-1]}){y[len(y) - 1]}")
            return y[1:] + x[len(x) - 1] + "+" +"(" + hohuman(x[1:],y[1:-1]) +")"+ y[len(y) - 1]
        elif len(y) == 2:
            print("43")
            print(f"({x[1:-1]},{y[1:]}){x[len(x) - 1]}+{x[1:]}{y[len(y) - 1]}")
            return "(" + hohuman(x[1:-1],y[1:]) +")"+ x[len(x) - 1] +"+" + x[1:] + y[len(y) - 1]
        print("4")
        print(f"({x[1:-1]},{y[1:]}){x[len(x) - 1]}+({x[1:]},{y[1:-1]}){y[len(y) - 1]}")
        return "(" + hohuman(x[1:-1],y[1:]) + ")" + x[len(x) - 1] + "+" + "(" + hohuman(x[1:],y[1:-1]) + ")" + y[len(y) - 1]

def bunpai(text:str,cout:int,sp:int,li:list):
    if cout == sp:
        print("========================================================="*10)
        return text
    elif cout == 1:
        return bunpai(re.sub(r'\(([a-z]{2})' + r'\+([a-z]{2})\)' + r'([a-z]{1})', r'\1'+ r'\3+\2' + r'\3',text),cout + 1,sp,li)
    else:
        print("-------------")
        print(text,cout)
        return bunpai(re.sub(r'\(([nm]+)' + r'\+([nm]+)'*cout + r'\)' + r'([nm]{1})', "+".join(li[ int((cout**2 + cout - 2)/2) : int((cout**2 + 3*cout)/2)]),text),cout + 1,sp,li)



if __name__ == "__main__":
    jisuu = 120
    rrrrr = []
    for num in range(3,jisuu):
        for k in range(1,num):
            if k != num:
                print(k)
                print(rf"\{k}" + rf"\{num}")
                rrrrr.append(rf"\{k}" + rf"\{num}")
    print(bunpai(hohuman("nnnnn","mmmmm"),1,120,rrrrr))

