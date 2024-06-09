from menu import Menu

def main() -> None:
    a = Menu("Menu a")
    b = Menu("Menu b")
    a.append_opts(b, "opt 1a" , "opt 2a", "opt 3a")
    a.append_func("test",test, 2,3)
    b.append_opts(a, "opt 1b" , "opt 2b" ,"opt 3b")
    a.select()

def test(a,b):
    print(a,b)

main()
