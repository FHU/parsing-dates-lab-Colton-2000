#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    while user_string != '-1':
        user_string = user_string.replace(',', '')
        user_string = user_string.split()
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
        month = user_string[0]
        month = months.get(month)
        if len(month) == 1:
            month = '0' + month
        day = user_string[1]
        if len(day) == 1:
            day = '0' + day
        year = user_string[2]
        date = month + '/' + day + '/' + year
        print(date)
        parse_date(input())

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    parse_date(input())