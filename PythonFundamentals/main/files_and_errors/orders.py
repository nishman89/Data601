#
# try:
#     file = open("orders.txt")
#
# except FileNotFoundError as errmsg:
#     print("There has been an error! Panic! ")
#     print(errmsg)
#     print(type(errmsg))
#     raise

# class AlientInvasionException(BaseException):

def open_and_print_file(file: str):
    try:
        opened_file = open(file, "r")
        file_line_list = opened_file.readlines()
        print(type(file_line_list))
        for line in file_line_list:
            print(line)
    except FileNotFoundError as err:
        print("File or directory cannot be found")
    finally:
        print("This line is always executed whether an expcetion is thrown or now")


def open_using_with_and_print(file: str):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as err:#
        print("File or directory cannot be found")
        print(err)
    finally:
        print("\nExecution Compete")



def write_to_file(file: str, order_item: str):
    try:
        with open(file, "a") as file:
            file.write(order_item + "\n")
    except FileNotFoundError as err:#
        print("File or directory cannot be found")
        print(err)
    finally:
        print("\nExecution Compete")

write_to_file("orders.txt", "Joe Rogan")
open_and_print_file("orders.txt")
# open_using_with_and_print("orders.txt")