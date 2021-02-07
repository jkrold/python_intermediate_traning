import csv


def csv_writer(user_list):
    try:
        with open('./data.csv', 'w') as fd:
            writer = csv.writer(fd)
            for user_tuple in user_list:
                writer.writerow(user_tuple)
    except (IOError, Exception) as e:
        print(f'Exception while writing csv format: {e.args}')

def csv_read():
    users = []
    try:
        with open('./data.csv', 'r') as fd:
            reader = csv.reader(fd)
            for row in reader:
                if row:
                    users.append(row)
    except (IOError, Exception) as e:
        print(f'Exception while writing csv format: {e.args}')
    return users
