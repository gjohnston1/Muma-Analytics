Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> amount_of_stones = int(input())
# added this from someone's code from class when she went over it
if not 1 <= N <= 10000000:
        sys.exit()
#this is the end of the added code from hers
#Creates a boundary of the number allowed to be input, sys.exit closes the system when the number is input
if amount_of_stones%2==0:
        print ("Bob")
else:
        print ("Alice")
