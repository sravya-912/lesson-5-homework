class books:

    attr1="The Inheritance Games-Jennifer Lynn Bard"
    attr2="Haryy Potter and The Order of the Phoenix"
    attr3="The Hobbit-J.R.R Tolkien"


    def fun(books):
        print("The first book is", books.attr1)
        print("The second book is", books.attr2)
        print("The third book is", books.attr3)

books= books()

print (books.attr1)
books.fun()