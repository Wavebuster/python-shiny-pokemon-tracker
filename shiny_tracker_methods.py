import csv

#for file_location enter the file path of the data.csv file and for names enter the file path of the pokemon_names.txt file.
file_location = ''
names = ''


def list_shinies():
    results = ""
    with open(file_location) as data:
        data_reader = csv.reader(data, delimiter=',')
        print("Obtained shinies: ")
        for row in data_reader:
            if row[2] == 'y':
                results += row[0] + ', '
        print(results[:-2])

def percent_shinies():
    num_shiny = 0
    with open(file_location) as data:
        data_reader = csv.reader(data, delimiter=',')
        for row in data_reader:
            if row[2] == 'y':
                num_shiny += 1
        print(f"You have obtained {num_shiny} shinies for a total shiny dex completion percentage of: {num_shiny/898}")

def add_shiny():
    new_shiny = input("Please enter the name of the Pokemon whose shiny you obtained.\n").title()
    with open(file_location, 'r') as lines:
        reader = csv.reader(lines.readlines())
    with open(file_location, 'w') as data:
        writer = csv.writer(data, delimiter=',')
        for row in reader:
            if row[0] == new_shiny:
                writer.writerow([row[0], row[1], 'y'])
            else:
                writer.writerow(row)

def write_csv():
    with open(file_location, 'w') as file:
        data_writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        with open(names) as pkmn_names:
            i = 1
            for n in pkmn_names:
                data_writer.writerow([n, i, 'n'])
                i += 1
