def koniec():
    quit()

pesel_number = input("enter PESEL number: ")

error = 0

if str.isnumeric(pesel_number) == False:
    print("not a number")
    error = 1
    koniec()
else:
    sum_of_characters = 0
    peselStr = pesel_number
    for i in range(len(pesel_number)):
        sum_of_characters = sum_of_characters + int(peselStr[i])
    if sum_of_characters == 0:
        print("all zeros")
        error = 1
        koniec()

if len(pesel_number) != 11:
    print("not 11 digits")
    error = 1

#decode year and month of birth
year_of_birth = int(peselStr[0:2])
month_of_birth = int(peselStr[2:4])
day_of_birth = int(peselStr[4:6])
serial_number = peselStr[6:10]
control_sum = int(peselStr[10])

if int(int(peselStr[2])) == 0 or int(peselStr[2]) == 1:
    year_of_birth = year_of_birth + 1900
if int(peselStr[2]) == 2 or int(peselStr[2]) == 3:
    year_of_birth = year_of_birth + 2000
    month_of_birth = month_of_birth - 20
if int(peselStr[2]) == 4 or int(peselStr[2]) == 5:
    year_of_birth = year_of_birth + 2100
    month_of_birth = month_of_birth - 40
if int(peselStr[2]) == 6 or int(peselStr[2]) == 7:
    year_of_birth = year_of_birth + 2200
    month_of_birth = month_of_birth - 60
if int(peselStr[2]) == 8 or int(peselStr[2]) == 9:
    year_of_birth = year_of_birth + 1800
    month_of_birth = month_of_birth - 80

#checking month and day of day_of_birth
lap_year = False
if(year_of_birth%4==0 and year_of_birth%100!=0) or year_of_birth%400==0:
    lap_year = True
    print("Rok jest przestępny.")
else:
    lap_year = False
    print("Rok nie jest przestępny.")

if month_of_birth > 12:
    print("Month of birth does not exist ", month_of_birth)
    error = 1
if month_of_birth in [1,3,5,7,8,10,12] and day_of_birth > 31:
    print("Day of birth does not exist ", day_of_birth)
    error = 1
if month_of_birth in [4,6,9,11] and day_of_birth > 30:
    print("Day of birth does not exist ", day_of_birth)
    error = 1
if month_of_birth == 2 and lap_year== True and day_of_birth >29:
    print("Day of birth does not exist ", day_of_birth)
    error = 1
if month_of_birth == 2 and lap_year== False and day_of_birth >28:
    print("Day of birth does not exist ", day_of_birth)
    error = 1

#decoding gender
gender = "unknown"
if int(peselStr[9])%2 == 0:
    gender = "female"
else:
    gender = "male"

#calculating control sum
wagi = [1,3,7,9,1,3,7,9,1,3]
sum = 0

for i in range(0,10):
    sum = sum + int(peselStr[i]) * wagi[i]
checksum = 10 - sum%10

if checksum == 10:
    checksum = 0
if checksum != control_sum:
    print("check sum error")
    error = 1

#printing result
print("data urodzenia: ", year_of_birth," ", month_of_birth, " ", day_of_birth)
print("numer seryjny: ", serial_number, "płeć: ", gender)
print("suma odczytana: ", control_sum, "suma obliczona: ", checksum)
print("błąd: ", error)

koniec()
