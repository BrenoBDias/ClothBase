from ascii import Menu
import app


a = Menu("Main")
app.seila()


b = Menu("Main", orign = a)

a.append_opts(b)



a.select()


