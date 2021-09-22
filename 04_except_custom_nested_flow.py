data ={"today":"friday" ,"date":25}
def function():
    # print(data["month"])
    # f=open("main.py")
    # print(f.read())
    # print(next(f))
    # print(10 + "20")
    # print(10/0)
    x =[1,2,3]
    print(x[7])

try:
    print(1)
    print(1*"30")
    print(2)
    try:
        function()
    except (IndexError, StopIteration):
        print(3)
    else:
        print(4)
        raise Medicine_expired("test")
        print(5)
except (KeyError, ValueError):
    try:
        print(6)
        print(1+30)
        print(7)
    except:
        print(8)

else:
    print(9)
    try:
        try:
            print(1/10)
        except ValueError:
            print(10)
    except ZeroDivisionError:
        print(11)

finally:
    print(12)
    try:
        f = open("kkk.txt")
        print(13)
    except FileNotFoundError:
        print(14)




