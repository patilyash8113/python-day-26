# python-day-26
Day 21 of my Python journey
Today i learn about Dunder Menthos and error handling
1)dunder methods = Dunder method are those methods that start with _(underscore) it also called as magic methods
-These methods allow you to define object interact with built in python operator, functions, and language constructs. They provide a way to implement
operator overloading.
where it is used 
- customise object creation and initialization (__init__,__new__)
-Enables operator overloading (+,-,*,/)
-provide string representation of object (__str__,__repr__)

(2) Suppose we ask the user for two inputs and both inputs ask for Enter a number, and then we print it using f-string and sum, so all we know the answer is the sum of the two numbers.
But when i accidently enter a number as a string of my name "yash", it shows me an error, right?
So basically, what I do is I create a while loop and use a try and expect statement. Basically, try and except statements are used to handle errors, so i use except: and print("hey, this wrogn please enter again")
So from now on, whenever a user creates a mistake, it doesn't show an error directly, but indirectly it prints ("hey, this wrogn please enter again"). This is where our try and except statement comes....
