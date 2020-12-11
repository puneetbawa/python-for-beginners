global a
a = 10
def func():
    global a
    a=20
func()
print(a)
