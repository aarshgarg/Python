x=79
def func1():
    x=70
    def func2():
        global x
        x=76
    print("before the calling func2",x)
    func2()
    print("after calling func2",x)

func1()
print(x)