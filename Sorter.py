from tkinter.constants import N


Dictionarie = {'0':0,
               '1':1,
               '2':2,
               '3':3,
               '4':4,
               '5':5,
               '6':6,
               '7':7,
               '8':8,
               '9':9,
               'A':10,
               'B':11,
               'C':12,
               'D':13,
               'E':14,
               'F':15,
               'G':16,
               'H':17,
               'I':18,
               'J':19,
               'K':20,
               'L':21,
               'M':22,
               'N':23,
               'O':24,
               'P':25,
               'Q':26,
               'R':27,
               'S':28,
               'T':29,
               'U':30,
               'V':31,
               'W':32,
               'X':33,
               'Y':34,
               'Z':35,
               '.':36,
               ' ':-1,
               '/':-2}

ListSort = []#['AB','N','K','C']
ListNum = []

print("\nWelcome to Sorter\nWrite the list to use\nTo exit press '/'\n")
read = True
while read:
    obj = input("List Data: ")
    if obj == '/':
        read = False
    else:
        ListSort.append(obj)

for val in ListSort:
    Numer = []
    for ch in val:
        Numer.append(Dictionarie[ch.upper()])
    ListNum.append(Numer)

sortedList = []

endSort = False
i = 0
c = 0
noRepeated = True
Sorted = []
SortedNumber = []
while not(endSort):
    place = 0
    n = 0
    while n<len(SortedNumber):
        if ListNum[i][c]==SortedNumber[n][c]:
            noRepeated = False
        if ListNum[i][c]>SortedNumber[n][c]:
            place = n+1
        n = n+1
    #print("{},{}".format(str(ListNum[i][c]),str(place)))
    if place == 0:
        Sorted = [ListSort[i]]+Sorted
        SortedNumber = [ListNum[i]]+SortedNumber
    elif place == len(SortedNumber):
        Sorted = Sorted+[ListSort[i]]
        SortedNumber = SortedNumber+[ListNum[i]]
    else:
        Sorted = Sorted[:place]+[ListSort[i]]+Sorted[place:]
        SortedNumber = SortedNumber[:place]+[ListNum[i]]+SortedNumber[place:]
    i = i+1
    if i == len(ListNum):
        i = 0
        c = c+1
        endSort = True

print("\nThe sorted list is: {}".format(Sorted))
