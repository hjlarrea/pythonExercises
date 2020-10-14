#In the previous exercise we saved information about famous scientists’ names and birthdays 
# to disk. In this exercise, load that JSON file from disk, extract the months of all the 
# birthdays, and count how many scientists have a birthday in each month.
#
#Your program should output something like:
#
#{
#	"May": 3,
#	"November": 2,
#	"December": 1
#}

if __name__ == "__main__":
    import json

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
    
    print(months)