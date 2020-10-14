#This exercise is Part 4 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, 
# and Part 3.
#
#In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.
#
#In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays 
# in! Because it would take a long time for you to input the months of various scientists, you can use my scientist 
# birthday JSON file. Just parse out the months (if you don’t know how, I suggest looking at the previous exercise 
# or its solution) and draw your histogram.
#
#If you are using a purely web-based interface for coding, this exercise won’t work for you, since it requires 
# installing the bokeh Python package. Now might be a good time to install Python on your own computer.

if __name__ == "__main__":
    import json
    from bokeh.plotting import figure,show,output_file

    monthsOfTheYear = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

    with open('./34_birthdayJson.json','r') as f:
        birthdays = json.load(f)

    months={}

    for name in birthdays.keys():
        month = birthdays[name].split('/')[1]
        months[monthsOfTheYear[month]] = 1 if monthsOfTheYear[month] not in months.keys() else months[monthsOfTheYear[month]]+1
    
    output_file('36_birthdayPlots.html')

    p = figure(x_range=list(monthsOfTheYear.values()))
    p.vbar(x=list(months.keys()),top=list(months.values()),width=1)

    show(p)