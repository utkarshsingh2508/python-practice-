class Book:
    def __init__(self,title,author,list_of_reviews):
        self.title = title
        self.author = author
        self.list_of_reviews = list_of_reviews

    def new_review(self,new_review):
        self.list_of_reviews.append(new_review)

    def count_reviews(self):
        count = 0
        for i in self.list_of_reviews:
            count += 1
        print(count)
    
    def display_reviews(self):
        for i in self.list_of_reviews:
            print(i)

b1 = Book("Atomic habit","James clear",["Good","Best","Excellent"])
b2 = Book("Road","Nitin gadkari",["Worst","Bad","Poor"])
b3 = Book("Math","Golu",["Good","Very good","Excellent"])


b1.new_review("Very good")
b1.count_reviews()
b1.display_reviews()
print(b1.title,b1.author,b1.list_of_reviews)
