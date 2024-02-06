#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    if user_string == '-1':
        return
    date = user_string.replace(',', '')
    date = date.split()
    months = {
        'January': '1',
        'February': '2',
        'March': '3',
        'April': '4',
        'May': '5',
        'June': '6',
        'July': '7',
        'August': '8',
        'September': '9',
        'October': '10',
        'November': '11',
        'December': '12'
    }
    month = date[0]
    month = months.get(month)
    day = date[1]
    year = date[2]
    print(month, day, year, sep='/')
    parse_date(input())

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    parse_date(input())