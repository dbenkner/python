from movie import Movie
import csv

print("Welcome to file processing")

print("File Processing")
# read()
print("read() hobbies.txt")
with open('hobbies.txt') as hobbies_file:
    contents = hobbies_file.read()
print(f"read() : {contents}")

print("readline() hobbies.txt")
with open('hobbies.txt') as hobbies_file:
    contents = hobbies_file.readline()
print(f"readline() : {contents}")

# readline() whole file
print("readline() hobbies.txt entire file")
with open('hobbies.txt') as hobbies_file:
    contents = hobbies_file.readline()
    while(contents):
        print(contents)
        contents = hobbies_file.readline()
# readlines()
print("readlines() hobbies.txt")
with open('hobbies.txt') as hobbies_file:
    contents = hobbies_file.readlines()
print(f"readlines() : {contents}")
#writing to a file
#define list of olympic athletes
print("\nWrite to the olympic-athlete file...")
olympic_athletes = ["Simone Biles", "Michael Phelps", "Michael Johnson", "Chloe Kim"]
#define a file to write to (without the 'with' keyword)
olympic_file = open("olympic-athletes.txt", "w")
#loop through list and write to file
for athlete in olympic_athletes:
    olympic_file.write(f"{athlete}\n")
#close file
olympic_file.close()
print("Done. Check the file.")

#processing CSV Files
print("CSVs")
print("Write to a movies.csv file")
#define some movies
movie_1 = Movie(1, "Star Wars Episode IV: A New Hope", 1977, "PG", "George Lucas")
movie_2 = Movie(2, "Coco", 2017, "PG", "Lee Unkrich, Adrian Molina")
movie_3 = Movie(3, "Black Panther", 2018, "PG-13", "Ryan Coogler")
#put them in a list
movies = [movie_1, movie_2, movie_3]

#import csv and use it to write the movies to a file using with keyword
import csv
with open("movies.csv", "w", newline="") as movie_file:
    writer = csv.writer(movie_file)
    for movie in movies:
        writer.writerow([movie.id, movie.title, movie.year, movie.rating, movie.director])
print("done")
# read the csv 
print("\nRead the movie csv and print to console...")
with open("movies.csv", newline="") as movie_file:
    reader = csv.reader(movie_file)
    for movie in reader:
        print(f"Movie: {movie[1]} ({movie[2]}), rated {movie[3]}, directed by {movie[4]}")
print("done")
# writing csv from a list of lists
print("\nWrite a movies csv from a list of lists")
movies_list = [["Star Wars Episode IV: A New Hope", 1976],
    ["Sixteen Candles", 1984],
    ["Rogue One", 2016],
    ["Happy Gilmore", 1996],
    ["Wedding Crashers", 2005]]
# write list to a csv
with open("movies-list.csv", "w", newline="") as movie_file:
    writer = csv.writer(movie_file)
    writer.writerows(movies_list)

#p.219 csv.reader()
with open("movies-list.csv", newline="") as movie_file:
    reader = csv.reader(movie_file)
    for movie in reader:
        print(f"{movie[0]} ({movie[1]})")
print("done")
print("Goodbye")