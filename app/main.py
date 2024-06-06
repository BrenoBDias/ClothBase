import asciiDisplay as dp

menu_names = ["Main Menu", "Clients", "Products", "Projects"]
menus = {}
for menu in menu_names:

    print(menu)
    menus[menu] = dp.Menu(menu) 

dp.logo()
menus["Main Menu"].start()

