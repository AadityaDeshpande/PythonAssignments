# example of closuer
# data is attached to the function
def outer(msg):
    print("in outer")
    def inner():
        print("in inner with ",msg)
    return inner

inn = outer("msg")
inn()

del outer

inn()