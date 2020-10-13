#Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
#and print out the results to the screen. I have a .txt file for you, if you want to use it!
#
#Extra:
#
#    Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt 
#    file, and count how many of each “category” of each image there are. This text file is actually a list 
#    of files corresponding to the SUN database scene recognition database, and lists the file directory 
#    hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear 
#    which part represents the scene category. To do this, you’re going to have to remember a bit about 
#    string parsing in Python 3. I talked a little bit about it in this post.

if __name__ == "__main__":
    categories = dict()

    with open('./22_readFromFile.txt','r') as open_file:
        content = open_file.readlines()

    for line in content:
        category  = line.split('/')[2]
        categories[category] = 1 if category not in categories.keys() else categories[category] + 1

    print(categories)