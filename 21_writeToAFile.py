# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with 
# some different code, use the code from the solution), and instead of printing the results to a screen, 
# write the results to a txt file. In your code, just make up a name for the file you are saving to.
# 
# Extras:
# 
#     Ask the user to specify the name of the output file that will be saved.

# _19_decodeAWebPageTwo is a symbolic link to 19_decodeAWebPageTwo.py
from _19_decodeAWebPageTwo import printArticle

if __name__ == "__main__":
    uri = 'https://www.washingtonpost.com/wp-dyn/articles/A2623-2005Mar26.html'

    with open('21_article.txt', 'w') as open_file:
        open_file.write(printArticle(uri))