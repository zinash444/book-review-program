# books that are availabe 
books = ['Crime and punishment', 'Fiker eske Mekaber', 'The everything store',]
reviews = []

while True: 
    print("\nBooks Available: ")
    for book in books:
        print("-" + book)

    print("\nEnter 'q' for quit.")

#ask for username
    name = input("Your username: ")
    if name == 'q':
        break


# ask for book 
    book = input("Which books are you reviewing? ")
    if book == 'q': 
        break 

# ask for review
    review = input("Write your review: ")
    if review == 'q':
        break

# create a dictionary containing : name, book, review 

    review = {
        'name': name,
        'book': book,
        'review': review
    }

#append dictionary to reviews - (add)
    reviews.append(review)

  # after loop : 
print("\n---- Books Reviews ----") # this program just end the loop (limit)

# show all reviews 

for review in reviews:
    print("Name: " + review['name'])
    print("Book: " + review['book'])
    print("Review: " + review['review'])

# What i learing from this program is how they interact to each other
# dictionaries, loops, if, while True , ending a loop
# print command is also very essential for python programs to excute 
# also how to use them.
# last but no least i have invalid sytax error and unexpected indent 
#error. this is my review for this program.
