import csv

def csv_reader(file: str):
    with open(file, "r", newline='') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")
        csv_list = list(csvreader)
        # print(csv_list)

        for n in range(1, len(csv_list) -1 ):
            print(csv_list[n])
        iter_csv = iter(csvreader)
        next(iter_csv)
        # for row in csvreader:
        #     print(row[-1])


def transform_user_details(csv_file_name: str) -> list:
    new_user_data = []
    with open(csv_file_name, "r", newline='') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")

        for user in csvreader:
            transformation = []
            transformation.append(f"{user[0]} {user[1]} {user[2]}")
            transformation.append(user[-1])
            new_user_data.append(transformation)

    new_user_data[0][0] = "Full Name"
    return  new_user_data

def create_new_user_data_csv(old_user_data_file="user_details.csv", new_file_name="new_user_details.csv"):
    new_user_data = transform_user_details(old_user_data_file)
    new_file = open(new_file_name,'w',newline='')
    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(new_user_data)

create_new_user_data_csv()
print(transform_user_details("user_details.csv"))