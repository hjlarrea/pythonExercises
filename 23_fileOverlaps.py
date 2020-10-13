#Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list 
# of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
#
#(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real 
# thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

if __name__ == "__main__":

    with open('23_fileOverlaps_1.txt','r') as file1:
        f1Content = file1.readlines()

    with open('23_fileOverlaps_2.txt','r') as file2:
        f2Content = file2.readlines()

    for number in f2Content:
        if number in f1Content:
            print("Found {0} in file 1.".format(number.replace("\n","")))