import json
import time
from typing import Optional

# --------------------------------------------------------------
#  file and  manager of file content
File = "shoping.json"


def load_file():
    try:
        with open(File, "r+", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def save_file(Data):
    try:
        with open(File, "w+", encoding="utf-8") as f:
            json.dump(Data, f, indent=4)
    except (json.JSONDecodeError, FileNotFoundError):
        return


# ----------------------------------------------------------------
#          heading
def headings(
    title: str,
    width: int = 70,
    border_char: str = "=",
    title_char: Optional[str] = None,
):
    title_char = border_char or title_char
    padded = border_char * width
    print(padded)
    print(f"{title}".center(width, title_char))
    print(padded)


# ---------------------------------------------------------------
#  function of visual asci art


def ascii_art():
    art = ["""
           __________________________
           """]

    print(art[0])


# ---------------------------------------------------------------------
#              --function of creation of list or items--             #


def items_create():
    headings(" Create New items ")
    Data = load_file()
    Name_dict = input("enter the name of your shopping: ").strip()
    if not Name_dict:
        print("the name of shopping basket cannot be empty!")
        return
    if Name_dict in Data:
        print("This shopping basket is allredy exist !")
        prt = {"y -->": "yes", "n -->": "no"}
        for i, j in prt.items():
            print(i, j)
        Andr_itm = input("do you want to create a new items basket: ").strip()
        if Andr_itm == "y":
            items_create()
        else:
            main_func()
    try:
        nbr_elm = int(input("How much items you Need today: "))
    except ValueError:
        print(" Invalid entry!")
    list_art = []
    for num in range(nbr_elm):
        elmt_var = input(f"Enter the Name of article {num + 1}: ").strip()
        if elmt_var == "":
            print("The name of article cannot be empty ")
        try:
            qties_var = int(input(f"Enter the quantities of -- {elmt_var}: "))

            price = float(input("enter the unity price of items ($$): "))
            gbl_price = price * qties_var
        except ValueError:
            print("Error: invalid entry")
            return

        date_dict = time.asctime()
        art = {
            "Name": elmt_var,
            "qties": qties_var,
            "unity price": price,
            "Total price": gbl_price,
        }
        list_art.append(art)

    date_dict = time.asctime()
    Data.update(
        {
            Name_dict: {
                "date": date_dict,
                "Article": list_art,
            }
        }
    )
    save_file(Data)
    print("the items was create successfully! \n")


def option_lst_itm():

    prt = {1: ".items", 2: ".leave"}

    for i, j in prt.items():
        print(i, j)

    option = int(input("enter the choice: "))
    if option == 1:
        items_create()

    elif option == 2:
        pass
    if not option or option not in [1, 2]:
        return


# --------------------------------------------------------------------------
#              --function of modify and remove dictionnary --             #


def items_Modif():
    Data = load_file()
    if not Data:
        print("basket is empty!")
        return
    all_items()
    Name_dict = input("Enter the Name of your basket: ").strip()

    if not Name_dict or Name_dict not in Data:
        print("this shopping items no exist in Database")
        return

    if Name_dict in Data:
        Data[Name_dict] = {}
        try:
            nbr_elm = int(input("How much items you Need today: "))
        except ValueError:
            print(" Invalid entry!")
        list_art = []
        for num in range(nbr_elm):
            elmt_var = input(f"Enter the Name of your new article-{num + 1}: ").strip()
            if elmt_var == "":
                print("The name of article cannot be empty ")
            try:
                qties_var = int(input(f"Enter the quantities of -- {elmt_var}: "))

                price = float(input("enter the unity price of items ($$): "))
                gbl_price = price * qties_var
            except ValueError:
                print("Error: invalid entry!")
                return

            art = {
                "Name": elmt_var,
                "qties": qties_var,
                "unity price": price,
                "Total price": gbl_price,
            }
            list_art.append(art)

            date_dict = time.asctime()
            Data.update(
                {
                    Name_dict: {
                        "date": date_dict,
                        "Article": list_art,
                    }
                }
            )

        time.sleep(1)
        save_file(Data)
        print("items are modified successfully !")


def modif_shop_elmt():
    pass


def modify_shoping():

    prt = {1: ".Modify an items", 2: ".leave"}

    for i, j in prt.items():
        print(i, j)

    try:
        qst = int(input("Enter your option (1/2): "))
    except ValueError:
        print("Invalid entry !")

    if qst == 1:
        items_Modif()
    elif qst == 2:
        modif_shop_elmt()
    elif qst == 3:
        pass
    else:
        print("This option Not exist!")
        return


def remove_shopping():
    Data = load_file()

    prt = {1: "element of the list/items", 2: "list or items", 3: "clear all repertory"}
    for i, j in prt.items():
        print(i, j)

    option = input("enter your option: ").strip()

    match option:
        case "1":
            name = input("enter the name of your list or items: ").strip()

            if not name or name not in Data:
                print("this name not exist in database!")
                return

            Data[name] = "items/list not exist"
        case "2":

            name = input("enter the name of your list or items: ").strip()

            if not name or name not in Data:
                print("this name not exist in database!")
                return

            del Data[name]

        case "3":
            Data.clear()
        case _:
            return
    save_file(Data)


# --------------------------------------------------------------------------
#              --function to dsplay list or items --             #


def display_menu():
    Data = load_file()
    if not Data:
        print("the shopping basket is empty")
        return {}
    prt = {
        1: ".Display all items",
        2: ".Display an specifical items",
        3: ".return to menu",
    }
    for i, j in prt.items():
        print(i, j)
    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print("invalid entry")
        return
    if not option or option not in [1, 2, 3]:
        raise ValueError
    if option == 1:
        all_items()
    elif option == 2:
        all_items()
        Name = input("enter the name of the items: ").strip()
        specific_details_item(Name)
    elif option == 3:
        main_func()


def all_items():
    Data = load_file()
    if not Data:
        print("Any basket for that moment 😔")
        return
    print("\n" + "=" * 60)
    print("   your shopping Baskets".center(60))
    print("=" * 60)
    for i, (Name, items) in enumerate(Data.items(), 1):
        article = items.get("Article", [])

        content = article.get("qties")
        print(content)
        date_str = items.get("date", "date unknow")
        print(f"{i:2d} . {Name :<25}  ({date_str})")
        print(f"--> {len(article)}   items  total of article:{content}")
        print("-" * 60)
        break


def specific_details_item(Name):
    Data = load_file()
    if Name not in Data:
        print(f"the basket {Name} is not found")
        return

    content = Data[Name]
    article = content.get("Article", [])
    date_str = content.get("date", "date unknow")
    total = content.get("qties", 0)
    print(f"{Name}  ({date_str})")
    print(f"--> {len(article)} items total of article:{total:>8,}")

    if not article:
        print("the basket is empty!")
        return
    else:
        for art in article:
            name_art = art.get("Name", "?")
            qties_art = art.get("qties", 0)
            unity_price = art.get("unity price", 0)
            total_price = art.get("Total price", unity_price * qties_art)
            print(
                f"{name_art}.... x{qties_art} ....unity price: {unity_price:2}CFA  --->  Total price {total_price} CFA"
            )
            ascii_art()

        print("=" * 60)
        print(f"{"Total of items in basket".upper()}  {len(art)}")
        print("=" * 60)


def main_func():

    load_file()
    headings("Welcome to sopping basket application")
    while True:
        prt = {
            1: ".create  items",
            2: ".modify the items",
            3: ".display items",
            4: ".remove items",
            5: ".quit/leave",
        }
        for i, j in prt.items():
            print(i, j)
        choice = int(input("Enter the the choice: "))
        if not choice or choice not in [1, 2, 3, 4, 5]:
            pass
        if choice == 1:
            option_lst_itm()
            ascii_art()
        elif choice == 2:
            modify_shoping()
            ascii_art()
        elif choice == 3:
            display_menu()
            ascii_art()
        elif choice == 4:
            remove_shopping()
            ascii_art()
        elif choice == 5:
            print("good bye!")
            ascii_art()
            break


main_func()
