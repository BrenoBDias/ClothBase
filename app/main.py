import asciiDisplay as dp

menu_names = ["Main Menu", "Clients", "Products", "Projects"]
menus = {}
for menu in menu_names:

    print(menu)
    menus[menu] = dp.Menu(menu) 


menus["Main Menu"].append_option("Clients", menus["Clients"])
menus["Main Menu"].append_option("Products", menus["Products"])
menus["Main Menu"].append_option("Projects", menus["Projects"])

dp.logo()
menus["Main Menu"].start()

