#Nirav Prajapati
class library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lenddict={}
    def Displaybook(self):
        print("welcome to our library")
        print("we have following book\n")
        for book in self.booklist:
            print(book)
    def Lendbook(self,book,user):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
        else:
            print(f"book is already taken by {self.lenddict[book]} ")
    def Addbook(self,book):
        self.booklist.append(book)
        print("book is succesfuly added")
    def Returnbook(self,book):
        self.lenddict.pop(book)
        print("Your book is succesfuly returned")
if __name__=='__main__':
    nirav=library(['reach dad poor dad','Python','c++','Harry potter' ],"Nirav eduhub")
    try:
        while(True):
            print(f"Welcome to the {nirav.name} library: ")
            print("1. Display Books")
            print("2. Lend a Book")
            print("3. Add a Book")
            print("4. Return a Book")
            print("-----------------------------------------------")
            user_choice = input("enter your choice : \n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            if user_choice not in ['1','2','3','4']:
                print("Please enter a valid option")
                continue

            else:
                user_choice = int(user_choice)
            if user_choice==1:
                nirav.Displaybook()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif user_choice==2:
                book=input("enter the name of the book you want to lend : ")
                user=input("enter your name : ")
                nirav.Lendbook(book,user)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif user_choice==3:
                book=input("enter the name of the book you want to add : ")
                nirav.Addbook(book)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif user_choice==4:
                book=input("enter the name of the book you want to return : ")
                nirav.Returnbook(book)
                print("your book is succesfuly returned")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                print("invaild input")
                print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print("Press q to quit and c to continue :  ")
            user_choice2 = ""
            while(user_choice2!="c" and user_choice2!="q"):
                user_choice2 = input()
             
                if user_choice2 == "q":
                    exit()

                elif user_choice2 == "c":
                    continue
    except Exception as e:
        print("invaild input")
