import time
from discord.ext import commands
BOT_TOKEN = "NjI3MDk5ODk3MjIwNDMxODcy.XY3v5Q.Q19bNJrTqvFa1eDTPEmfJjvd4HE"

club_CHI = "MYP chill out club"
club_IMP = "Imperial Assault campaign club"

sp_NULL = "No class"
sp_NUCL = "No club"
sp_HMRM = "Homeroom"

sp_AMRE = "Morning recess"
sp_LNCH = "Lunch"
sp_LNRE = "Lunch recess"
sp_PMRE = "Afternoon recess"

id_CHI = ("chi", "myp chill out club", "myp chill out", "chill", "chill out", "chill out club", "chill club", "myp chill club")
id_IMP = ("imp", "imperial assault", "star wars imperial assault", "star wars: imperial assault")

CurrentPeriod =  "customerror"
NextPeriod = "customerror"


def SetNextPeriod(grade):
    if grade == "9":
        with open("9MonFT.txt", "r") as file:
            MonTT = eval(file.readline())
        with open("9TueFT.txt", "r") as file:
            TueTT = eval(file.readline())
        with open("9WedFT.txt", "r") as file:
            WedTT = eval(file.readline())
        with open("9ThuFT.txt", "r") as file:
            ThuTT = eval(file.readline())
        with open("9FriFT.txt", "r") as file:
            FriTT = eval(file.readline())
    elif grade == "8":
        with open("8MonFT.txt", "r") as file:
            MonTT = eval(file.readline())
        with open("8TueFT.txt", "r") as file:
            TueTT = eval(file.readline())
        with open("8WedFT.txt", "r") as file:
            WedTT = eval(file.readline())
        with open("8ThuFT.txt", "r") as file:
            ThuTT = eval(file.readline())
        with open("8FriFT.txt", "r") as file:
            FriTT = eval(file.readline())
    elif grade == "7":
        with open("7MonFT.txt", "r") as file:
            MonTT = eval(file.readline())
        with open("7TueFT.txt", "r") as file:
            TueTT = eval(file.readline())
        with open("7WedFT.txt", "r") as file:
            WedTT = eval(file.readline())
        with open("7ThuFT.txt", "r") as file:
            ThuTT = eval(file.readline())
        with open("7FriFT.txt", "r") as file:
            FriTT = eval(file.readline())

    global NextPeriod
    #   Monday
    if time.localtime()[6] == 0:

        #  0:00 to 8:00
        if 0 <= time.localtime()[3] <= 8:
            NextPeriod = MonTT[0]

        #  9:00 to 10:00
        elif time.localtime()[3] == 9:
            NextPeriod = MonTT[1]

        #  10:00 to 11:30
        elif time.localtime()[3] == 10 or (time.localtime()[3] == 11 and time.localtime()[4] < 30):
            NextPeriod = MonTT[2]

        #  11:00 to 12:30
        elif (time.localtime()[3] == 11 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 13 and time.localtime()[4] < 30) or time.localtime()[3] == 12:
            NextPeriod = MonTT[3]

        #  1:30 to 2:30
        elif (time.localtime()[3] == 13 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 14 and time.localtime()[4] < 45):
            NextPeriod = MonTT[4]

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            NextPeriod = sp_HMRM
        #  3:45 to 4:15
        elif (time.localtime()[3] == 15 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 16 and time.localtime()[4] < 15):
            if MonTT[5] == sp_NUCL:
                NextPeriod = TueTT[0]
            else:
                NextPeriod = MonTT[5]
        else:
            NextPeriod = TueTT[0]

    #   Tuesday
    elif time.localtime()[6] == 1:

        #  0:00 to 8:00
        if 0 <= time.localtime()[3] <= 8:
            NextPeriod = TueTT[0]

        #  9:00 to 10:00
        elif time.localtime()[3] == 9:
            NextPeriod = TueTT[1]

        #  10:00 to 11:30
        elif time.localtime()[3] == 10 or (time.localtime()[3] == 11 and time.localtime()[4] < 30):
            NextPeriod = TueTT[2]

        #  11:00 to 12:30
        elif (time.localtime()[3] == 11 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 13 and time.localtime()[4] < 30) or time.localtime()[3] == 12:
            NextPeriod = TueTT[3]

        #  1:30 to 2:30
        elif (time.localtime()[3] == 13 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 14 and time.localtime()[4] < 45):
            NextPeriod = TueTT[4]

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            NextPeriod = sp_HMRM
        #  3:45 to 4:15
        elif (time.localtime()[3] == 15 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 16 and time.localtime()[4] < 15):
            if TueTT[5] == sp_NUCL:
                NextPeriod = WedTT[0]
            else:
                NextPeriod = WedTT[4]
        else:
            NextPeriod = WedTT[0]

    #   Wednesday
    elif time.localtime()[6] == 2:
        #  0:00 to 8:00
        if 0 <= time.localtime()[3] <= 8:
            NextPeriod = WedTT[0]

        #  9:00 to 10:00
        elif time.localtime()[3] == 9:
            NextPeriod = WedTT[1]

        #  10:00 to 11:30
        elif time.localtime()[3] == 10 or (time.localtime()[3] == 11 and time.localtime()[4] < 30):
            NextPeriod = WedTT[2]

        #  11:00 to 12:30
        elif (time.localtime()[3] == 11 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 13 and time.localtime()[4] < 30) or time.localtime()[3] == 12:
            NextPeriod = WedTT[3]
        #  12:30 to 2:30
        elif (time.localtime()[3] == 12 and time.localtime()[4] >= 30) or (time.localtime()[3] == 14 and time.localtime()[4] < 30) or time.localtime()[3] == 13:
            if WedTT[4] == sp_NUCL:
                NextPeriod = ThuTT[0]
            else:
                NextPeriod = WedTT[5]
        else:
            NextPeriod = ThuTT[0]

    #   Thursday
    elif time.localtime()[6] == 3:

        #  0:00 to 8:00
        if 0 <= time.localtime()[3] <= 8:
            NextPeriod = ThuTT[0]

        #  9:00 to 10:00
        elif time.localtime()[3] == 9:
            NextPeriod = ThuTT[1]

        #  10:00 to 11:30
        elif time.localtime()[3] == 10 or (time.localtime()[3] == 11 and time.localtime()[4] < 30):
            NextPeriod = ThuTT[2]

        #  11:00 to 12:30
        elif (time.localtime()[3] == 11 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 13 and time.localtime()[4] < 30) or time.localtime()[3] == 12:
            NextPeriod = ThuTT[3]

        #  1:30 to 2:30
        elif (time.localtime()[3] == 13 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 14 and time.localtime()[4] < 45):
            NextPeriod = ThuTT[4]

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            NextPeriod = sp_HMRM
        #  3:45 to 4:15
        elif (time.localtime()[3] == 15 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 16 and time.localtime()[4] < 15):
            if ThuTT[5] == sp_NUCL:
                NextPeriod = FriTT[0]
            else:
                NextPeriod = ThuTT[5]
        else:
            NextPeriod = FriTT[0]

    #   Friday
    elif time.localtime()[6] == 4:

        #  0:00 to 8:00
        if 0 <= time.localtime()[3] <= 8:
            NextPeriod = FriTT[0]

        #  9:00 to 10:00
        elif time.localtime()[3] == 9:
            NextPeriod = FriTT[1]

        #  10:00 to 11:30
        elif time.localtime()[3] == 10 or (time.localtime()[3] == 11 and time.localtime()[4] < 30):
            NextPeriod = FriTT[2]

        #  11:00 to 12:30
        elif (time.localtime()[3] == 11 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 13 and time.localtime()[4] < 30) or time.localtime()[3] == 12:
            NextPeriod = FriTT[3]

        #  1:30 to 2:30
        elif (time.localtime()[3] == 13 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 14 and time.localtime()[4] < 45):
            NextPeriod = FriTT[4]

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            NextPeriod = sp_HMRM
        #  3:45 to 4:15
        elif (time.localtime()[3] == 15 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 16 and time.localtime()[4] < 15):
            if FriTT[5] == sp_NUCL:
                NextPeriod = MonTT[0]
            else:
                NextPeriod = FriTT[5]
        else:
            NextPeriod = MonTT[0]
    else:
        NextPeriod = MonTT[0]
    return NextPeriod


def SetCurrentPeriod(grade):
    if grade == "9":
        with open("9MonFT.txt", "r") as file:
            MonTT = eval(file.readline())
        with open("9TueFT.txt", "r") as file:
            TueTT = eval(file.readline())
        with open("9WedFT.txt", "r") as file:
            WedTT = eval(file.readline())
        with open("9ThuFT.txt", "r") as file:
            ThuTT = eval(file.readline())
        with open("9FriFT.txt", "r") as file:
            FriTT = eval(file.readline())
    elif grade == "8":
        with open("8MonFT.txt", "r") as file:
            MonTT = eval(file.readline())
        with open("8TueFT.txt", "r") as file:
            TueTT = eval(file.readline())
        with open("8WedFT.txt", "r") as file:
            WedTT = eval(file.readline())
        with open("8ThuFT.txt", "r") as file:
            ThuTT = eval(file.readline())
        with open("8FriFT.txt", "r") as file:
            FriTT = eval(file.readline())
    elif grade == "7":
        with open("7MonFT.txt", "r") as file:
            MonTT = eval(file.readline())
        with open("7TueFT.txt", "r") as file:
            TueTT = eval(file.readline())
        with open("7WedFT.txt", "r") as file:
            WedTT = eval(file.readline())
        with open("7ThuFT.txt", "r") as file:
            ThuTT = eval(file.readline())
        with open("7FriFT.txt", "r") as file:
            FriTT = eval(file.readline())

    global CurrentPeriod
    #   Monday
    if time.localtime()[6] == 0:

        #  00:00 to 09:00
        if time.localtime()[3] < 9:
            CurrentPeriod = sp_NULL

        #  09:00 to 10:00
        elif time.localtime()[3] == 9:
            CurrentPeriod = MonTT[0]

        #  10:00 to 11:00
        elif time.localtime()[3] == 10:
            CurrentPeriod = MonTT[1]

        #  11:00 to 11:30
        elif time.localtime()[3] == 11 and time.localtime()[4] < 30:
            CurrentPeriod = sp_AMRE

        #  11:30 to 12:30
        elif (time.localtime()[3] == 11 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 12 and time.localtime()[4] < 30):
            CurrentPeriod = MonTT[2]

        #  12:30 to 1:00
        elif time.localtime()[3] == 12 and time.localtime()[4] >= 30:
            CurrentPeriod = sp_LNCH

        #  1:00 to 1:30
        elif time.localtime()[3] == 13 and time.localtime()[4] < 30:
            CurrentPeriod = sp_LNRE

        #  1:30 to 2:30
        elif (time.localtime()[3] == 13 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 14 and time.localtime()[4] < 45):
            CurrentPeriod = MonTT[3]

        #  2:30 to 2:45
        elif time.localtime()[3] == 14 and 30 <= time.localtime()[4] > 45:
            CurrentPeriod = sp_PMRE

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            CurrentPeriod = MonTT[4]

        #  3:45 to 4:00
        elif time.localtime()[3] == 15 and time.localtime()[4] >= 45:
            CurrentPeriod = sp_HMRM

        #  4:15 to 5:00
        elif time.localtime()[3] == 16 and time.localtime()[4] >= 15:
            CurrentPeriod = MonTT[5]

        #  Else
        else:
            CurrentPeriod = sp_NULL

    #   Tuesday
    elif time.localtime()[6] == 1:

        #  00:00 to 09:00
        if time.localtime()[3] < 9:
            CurrentPeriod = sp_NULL

        #  09:00 to 10:00
        elif time.localtime()[3] == 9:
            CurrentPeriod = TueTT[0]

        #  10:00 to 11:00
        elif time.localtime()[3] == 10:
            CurrentPeriod = TueTT[1]

        #  11:00 to 11:30
        elif time.localtime()[3] == 11 and time.localtime()[4] < 30:
            CurrentPeriod = sp_AMRE

        #  11:30 to 12:30
        elif (time.localtime()[3] == 11 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 12 and time.localtime()[4] < 30):
            CurrentPeriod = TueTT[2]

        #  12:30 to 1:00
        elif time.localtime()[3] == 12 and time.localtime()[4] >= 30:
            CurrentPeriod = sp_LNCH

        #  1:00 to 1:30
        elif time.localtime()[3] == 13 and time.localtime()[4] < 30:
            CurrentPeriod = sp_LNRE

        #  1:30 to 2:30
        elif (time.localtime()[3] == 13 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 14 and time.localtime()[4] < 45):
            CurrentPeriod = TueTT[3]

        #  2:30 to 2:45
        elif time.localtime()[3] == 14 and 30 <= time.localtime()[4] > 45:
            CurrentPeriod = sp_PMRE

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            CurrentPeriod = TueTT[4]

        #  3:45 to 4:00
        elif time.localtime()[3] == 15 and time.localtime()[4] >= 45:
            CurrentPeriod = sp_HMRM

        #  4:15 to 5:00
        elif time.localtime()[3] == 16 and time.localtime()[4] >= 15:
            CurrentPeriod = TueTT[5]

        #  Else
        else:
            CurrentPeriod = sp_NULL

    #   Wednesday
    elif time.localtime()[6] == 2:

        #  00:00 to 09:00
        if time.localtime()[3] < 9:
            CurrentPeriod = sp_NULL

        #  09:00 to 10:00
        elif time.localtime()[3] == 9:
            CurrentPeriod = WedTT[0]

        #  10:00 to 11:00
        elif time.localtime()[3] == 10:
            CurrentPeriod = WedTT[1]

        #  11:00 to 11:30
        elif time.localtime()[3] == 11 and time.localtime()[4] < 30:
            CurrentPeriod = sp_AMRE

        #  11:30 to 12:30
        elif (time.localtime()[3] == 11 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 12 and time.localtime()[4] < 30):
            CurrentPeriod = WedTT[2]

        #  12:30 to 1:00
        elif time.localtime()[3] == 12 and time.localtime()[4] >= 30:
            CurrentPeriod = sp_LNCH

        #  1:00 to 1:30
        elif time.localtime()[3] == 13 and time.localtime()[4] < 30:
            CurrentPeriod = sp_LNRE

        #  1:30 to 2:30
        elif (time.localtime()[3] == 13 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 14 and time.localtime()[4] < 45):
            CurrentPeriod = WedTT[3]

        #  2:30 to 2:45
        elif time.localtime()[3] == 14 and 30 <= time.localtime()[4] > 45:
            CurrentPeriod = sp_PMRE

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            CurrentPeriod = WedTT[4]

        #  3:45 to 4:00
        elif time.localtime()[3] == 15 and time.localtime()[4] >= 45:
            CurrentPeriod = sp_HMRM

        #  4:15 to 5:00
        elif time.localtime()[3] == 16 and time.localtime()[4] >= 15:
            CurrentPeriod = WedTT[5]

        #  Else
        else:
            CurrentPeriod = sp_NULL

    #   Thursday
    elif time.localtime()[6] == 3:

        #  00:00 to 09:00
        if time.localtime()[3] < 9:
            CurrentPeriod = sp_NULL

        #  09:00 to 10:00
        elif time.localtime()[3] == 9:
            CurrentPeriod = ThuTT[0]

        #  10:00 to 11:00
        elif time.localtime()[3] == 10:
            CurrentPeriod = ThuTT[1]

        #  11:00 to 11:30
        elif time.localtime()[3] == 11 and time.localtime()[4] < 30:
            CurrentPeriod = sp_AMRE

        #  11:30 to 12:30
        elif (time.localtime()[3] == 11 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 12 and time.localtime()[4] < 30):
            CurrentPeriod = ThuTT[2]

        #  12:30 to 1:00
        elif time.localtime()[3] == 12 and time.localtime()[4] >= 30:
            CurrentPeriod = sp_LNCH

        #  1:00 to 1:30
        elif time.localtime()[3] == 13 and time.localtime()[4] < 30:
            CurrentPeriod = sp_LNRE

        #  1:30 to 2:30
        elif (time.localtime()[3] == 13 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 14 and time.localtime()[4] < 45):
            CurrentPeriod = ThuTT[3]

        #  2:30 to 2:45
        elif time.localtime()[3] == 14 and 30 <= time.localtime()[4] > 45:
            CurrentPeriod = sp_PMRE

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            CurrentPeriod = ThuTT[4]

        #  3:45 to 4:00
        elif time.localtime()[3] == 15 and time.localtime()[4] >= 45:
            CurrentPeriod = sp_HMRM

        #  4:15 to 5:00
        elif time.localtime()[3] == 16 and time.localtime()[4] >= 15:
            CurrentPeriod = ThuTT[5]

        #  Else
        else:
            CurrentPeriod = sp_NULL

    #   Friday
    elif time.localtime()[6] == 4:

        #  00:00 to 09:00
        if time.localtime()[3] < 9:
            CurrentPeriod = sp_NULL

        #  09:00 to 10:00
        elif time.localtime()[3] == 9:
            CurrentPeriod = FriTT[0]

        #  10:00 to 11:00
        elif time.localtime()[3] == 10:
            CurrentPeriod = FriTT[1]

        #  11:00 to 11:30
        elif time.localtime()[3] == 11 and time.localtime()[4] < 30:
            CurrentPeriod = sp_AMRE

        #  11:30 to 12:30
        elif (time.localtime()[3] == 11 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 12 and time.localtime()[4] < 30):
            CurrentPeriod = FriTT[2]

        #  12:30 to 1:00
        elif time.localtime()[3] == 12 and time.localtime()[4] >= 30:
            CurrentPeriod = sp_LNCH

        #  1:00 to 1:30
        elif time.localtime()[3] == 13 and time.localtime()[4] < 30:
            CurrentPeriod = sp_LNRE

        #  1:30 to 2:30
        elif (time.localtime()[3] == 13 and time.localtime()[4] >= 30) or (
                time.localtime()[3] == 14 and time.localtime()[4] < 45):
            CurrentPeriod = FriTT[3]

        #  2:30 to 2:45
        elif time.localtime()[3] == 14 and 30 <= time.localtime()[4] > 45:
            CurrentPeriod = sp_PMRE

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            CurrentPeriod = FriTT[4]

        #  3:45 to 4:00
        elif time.localtime()[3] == 15 and time.localtime()[4] >= 45:
            CurrentPeriod = sp_HMRM

        #  4:15 to 5:00
        elif time.localtime()[3] == 16 and time.localtime()[4] >= 15:
            CurrentPeriod = FriTT[5]

        #  Else
        else:
            CurrentPeriod = sp_NULL

    #   Other
    else:
        CurrentPeriod = sp_NULL

    return CurrentPeriod




def ViewPeriod():
    with open("9MonFT.txt", "r") as file:
        MonTT = eval(file.readline())
    with open("9TueFT.txt", "r") as file:
        TueTT = eval(file.readline())
    with open("9WedFT.txt", "r") as file:
        WedTT = eval(file.readline())
    with open("9ThuFT.txt", "r") as file:
        ThuTT = eval(file.readline())
    with open("9FriFT.txt", "r") as file:
        FriTT = eval(file.readline())

    PDayToView = str.lower(input("\nInput day to view a period of:  "))
    if PDayToView == "monday" or PDayToView == "mon":
        PeriodToView = str.lower(input("Select the period to view:  "))
        if PeriodToView == "1" or PeriodToView == "2" or PeriodToView == "3" or PeriodToView == "4" or PeriodToView == "5":
            print("\nPeriod " + str(PeriodToView) + " of Monday is: " + MonTT[int(PeriodToView) - 1])
        elif PeriodToView == "club" or "6":
            if MonTT[5] == sp_NUCL:
                print("\nThere is no club on Monday")
            else:
                print("\nMonday's club is: " + MonTT[5])
    elif PDayToView == "tuesday" or PDayToView == "tue":
        PeriodToView = str.lower(input("Select the period to view:  "))
        if PeriodToView == "1" or PeriodToView == "2" or PeriodToView == "3" or PeriodToView == "4" or PeriodToView == "5":
            print("\nPeriod " + str(PeriodToView) + " of Tuesday is: " + TueTT[int(PeriodToView) - 1])
        elif PeriodToView == "club" or "6":
            if TueTT[5] == sp_NUCL:
                print("\nThere is no club on Tuesday")
            else:
                print("\nTuesday's club is: " + TueTT[5])
    elif PDayToView == "wednesday" or PDayToView == "wed":
        PeriodToView = str.lower(input("Select the period to view:  "))
        if PeriodToView == "1" or PeriodToView == "2" or PeriodToView == "3" or PeriodToView == "4":
            print("\nPeriod " + str(PeriodToView) + " of Wednesday is: " + WedTT[int(PeriodToView) - 1])
        elif PeriodToView == "club" or "5":
            if WedTT[4] == sp_NUCL:
                print("\nThere is no club on Wednesdau")
            else:
                print("\nWednesday's club is: " + WedTT[4])
    elif PDayToView == "thursday" or PDayToView == "thu":
        PeriodToView = str.lower(input("Select the period to view:  "))
        if PeriodToView == "1" or PeriodToView == "2" or PeriodToView == "3" or PeriodToView == "4" or PeriodToView == "5":
            print("\nPeriod " + str(PeriodToView) + " of Thursday is: " + ThuTT[int(PeriodToView) - 1])
        elif PeriodToView == "club" or "6":
            if ThuTT[5] == sp_NUCL:
                print("\nThere is no club on Thursday")
            else:
                print("\nThursday's club is: " + ThuTT[5])
    elif PDayToView == "friday" or PDayToView == "fri":
        PeriodToView = str.lower(input("Select the period to view:  "))
        if PeriodToView == "1" or PeriodToView == "2" or PeriodToView == "3" or PeriodToView == "4" or PeriodToView == "5":
            print("\nPeriod " + str(PeriodToView) + " of Friday is: " + FriTT[int(PeriodToView) - 1])
        elif PeriodToView == "club" or "6":
            if FriTT[5] == sp_NUCL:
                print("\nThere is no club on Friday")
            else:
                print("\nFriday's club is: " + FriTT[5])
    elif PDayToView == "saturday" or PDayToView == "sat" or PDayToView == "sunday" or PDayToView == "sun":
        print("There is no school during the weekend.")
    else:
        print("Invalid input")


def Time():
    if len(str(time.localtime()[3])) == 1:
        if len(str(time.localtime()[4])) == 1:
            return "0" + str(time.localtime()[3]) + ":0" + str(time.localtime()[4])
        else:
            return "0" + str(time.localtime()[3]) + ":" + str(time.localtime()[4])
    else:
        if len(str(time.localtime()[4])) == 1:
            return str(time.localtime()[3]) + ":0" + str(time.localtime()[4])
        else:
            return str(time.localtime()[3]) + ":" + str(time.localtime()[4])
def Day():
    if time.localtime()[6] == 0:
        return "Monday"
    elif time.localtime()[6] == 1:
        return "Tuesday"
    elif time.localtime()[6] == 2:
        return "Wednesday"
    elif time.localtime()[6] == 3:
        return "Thursday"
    elif time.localtime()[6] == 4:
        return "Friday"
    elif time.localtime()[6] == 5:
        return "Saturday"
    elif time.localtime()[6] == 6:
        return "Sunday"
def Date():
    if len(str(time.localtime()[2])) == 2 and str(time.localtime()[2])[0] == "1":
        return str(time.localtime()[2]) + "th"
    elif len(str(time.localtime()[2])) == 2:
        if str(time.localtime()[2])[1] == "1":
            return str(time.localtime()[2]) + "st"
        elif str(time.localtime()[2])[1] == "2":
            return str(time.localtime()[2]) + "nd"
        elif str(time.localtime()[2])[1] == "3":
            return str(time.localtime()[2]) + "rd"
        else:
            return str(time.localtime()[2]) + "th"
    elif len(str(time.localtime()[2])) == 1:
        if str(time.localtime()[2]) == "1":
            return str(time.localtime()[2]) + "st"
        elif str(time.localtime()[2]) == "2":
            return str(time.localtime()[2]) + "nd"
        elif str(time.localtime()[2]) == "3":
            return str(time.localtime()[2]) + "rd"
        else:
            return str(time.localtime()[2]) + "th"
def Month():
    if str(time.localtime()[1]) == "1":
        return "January"
    elif str(time.localtime()[1]) == "2":
        return "February"
    elif str(time.localtime()[1]) == "3":
        return "March"
    elif str(time.localtime()[1]) == "4":
        return "April"
    elif str(time.localtime()[1]) == "5":
        return "May"
    elif str(time.localtime()[1]) == "6":
        return "June"
    elif str(time.localtime()[1]) == "7":
        return "July"
    elif str(time.localtime()[1]) == "8":
        return "August"
    elif str(time.localtime()[1]) == "9":
        return "September"
    elif str(time.localtime()[1]) == "10":
        return "October"
    elif str(time.localtime()[1]) == "11":
        return "November"
    elif str(time.localtime()[1]) == "12":
        return "December"


client = commands.Bot(command_prefix=".")

with open("users9.txt", "r") as file:
    userdata9 = file.read()
with open("users8.txt", "r") as file:
    userdata8 = file.read()
with open("users7.txt", "r") as file:
    userdata7 = file.read()


@client.event
async def on_ready():
    print("TimeTableBot is now running")


@client.command(pass_context=True)
async def tt(ctx, modeinp="11381138", inp1="11381138", inp2="11381138"):
    with open("users9.txt", "r") as file:
        userdata9 = file.read()
    with open("users8.txt", "r") as file:
        userdata8 = file.read()
    with open("users7.txt", "r") as file:
        userdata7 = file.read()


    mode = str.lower(modeinp)
    if str(ctx.message.author.id) in userdata9 or str(ctx.message.author.id) in userdata8 or str(ctx.message.author.id) in userdata7:
        with open("users9.txt", "r") as file:
            userdata9 = file.read()
        with open("users8.txt", "r") as file:
            userdata8 = file.read()
        with open("users7.txt", "r") as file:
            userdata7 = file.read()
        if mode == "11381138":
            if str(ctx.message.author.id) in userdata9:
                await ctx.send(ctx.message.author.mention + "  (G9)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()))
                if SetCurrentPeriod("9") == sp_NULL or SetCurrentPeriod("9") == sp_NUCL:
                    await ctx.send("There is nothing scheduled for the current period")
                else:
                    await ctx.send("The current period is " + SetCurrentPeriod("9"))
                await ctx.send("The next sceduled period is " + SetNextPeriod("9"))
            elif str(ctx.message.author.id) in userdata8:
                await ctx.send(ctx.message.author.mention + "  (G8)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()))
                if SetCurrentPeriod("8") == sp_NULL or SetCurrentPeriod("8") == sp_NUCL:
                    await ctx.send("There is nothing scheduled for the current period")
                else:
                    await ctx.send("The current period is " + SetCurrentPeriod("8"))
                await ctx.send("The next sceduled period is " + SetNextPeriod("8"))
            elif str(ctx.message.author.id) in userdata7:
                await ctx.send(ctx.message.author.mention + "  (G7)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()))
                if SetCurrentPeriod("7") == sp_NULL or SetCurrentPeriod("7") == sp_NUCL:
                    await ctx.send("There is nothing scheduled for the current period")
                else:
                    await ctx.send("The current period is " + SetCurrentPeriod("7"))
                await ctx.send("The next sceduled period is " + SetNextPeriod("7"))
        
        elif mode == "help" or mode == "?":
            await ctx.send(ctx.message.author.mention + "  |  **Command List:**\n"
                                                        "**.tt**  -  Provides key information about current and upcoming periods, etc.\n \n"
                                                        "**.tt help**  -  Gives information on bot functions\n \n"
                                                        "**.tt config**  -  Allows you to configure various user settings for this bot\n \n"
                                                        "**.tt viewday G D**  -  Displays the timetable of the specified day   **G** = Grade    **D** = Day\n"
                                                        "|     *(If no grade is inputted, your grade will be used. If no day is inputted, the current day will be used)*\n \n"
                                                        "**.tt viewperiod P D G**  -  Displays a specified period of a specified day   **P** = Period number   **D** = Day   **G** = Grade\n"
                                                        "|     *(If no day or period is specified, the current ones will be used. If no grade is inputted, your grade will be used. Use 'x' to force the default value)*\n")
        elif mode == "setgrade":
            if str(ctx.message.author.id) in userdata9:
                await ctx.send(str(
                    ctx.message.author.mention) + "  |  Your grade has already been set to 9. Use **.tt config** to change it.")
            elif str(ctx.message.author.id) in userdata8:
                await ctx.send(str(
                    ctx.message.author.mention) + "  |  Your grade has already been set to 8. Use **.tt config** to change it.")
            elif str(ctx.message.author.id) in userdata7:
                await ctx.send(str(
                    ctx.message.author.mention) + "  |  Your grade has already been set to 7. Use **.tt config** to change it.")
        elif mode == "viewday":
            if inp1 == "9" or (inp1 == "11381138" and str(ctx.message.author.id) in userdata9):
                with open("9MonFT.txt", "r") as file:
                    MonTT = eval(file.readline())
                with open("9TueFT.txt", "r") as file:
                    TueTT = eval(file.readline())
                with open("9WedFT.txt", "r") as file:
                    WedTT = eval(file.readline())
                with open("9ThuFT.txt", "r") as file:
                    ThuTT = eval(file.readline())
                with open("9FriFT.txt", "r") as file:
                    FriTT = eval(file.readline())
                if str.lower(inp2) == "mon" or str.lower(inp2) == "monday":
                    await ctx.send(ctx.message.author.mention + "  |  G9's Monday timetable is:")
                    for period in MonTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "tue" or str.lower(inp2) == "tues" or str.lower(inp2) == "tuesday":
                    await ctx.send(ctx.message.author.mention + "  |  G9's Tuesday timetable is:")
                    for period in TueTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "wed" or str.lower(inp2) == "wednesday":
                    await ctx.send(ctx.message.author.mention + "  |  G9's Wednesday timetable is:")
                    for period in WedTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "thu" or str.lower(inp2) == "thur" or str.lower(inp2) == "thurs" or str.lower(inp2) == "thursday":
                    await ctx.send(ctx.message.author.mention + "  |  G9's Thursday timetable is:")
                    for period in ThuTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "fri" or str.lower(inp2) == "friday":
                    await ctx.send(ctx.message.author.mention + "  |  G9's Friday timetable is:")
                    for period in FriTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "sat" or str.lower(inp2) == "saturday" or str.lower(inp2) == "sun" or str.lower(inp2) == "sunday":
                    await ctx.send(ctx.message.author.mention + "  |  There is no timetable set on the weekend")
                else:
                    await ctx.send(ctx.message.author.mention + "  |  That is not the correct usage of that command.\n**.tt viewday G D**  -  Displays the timetable of the specified day   **G** = Grade    **D** = First letter of the day to view")
            elif inp1 == "8" or (inp1 == "11381138" and str(ctx.message.author.id) in userdata8):
                with open("8MonFT.txt", "r") as file:
                    MonTT = eval(file.readline())
                with open("8TueFT.txt", "r") as file:
                    TueTT = eval(file.readline())
                with open("8WedFT.txt", "r") as file:
                    WedTT = eval(file.readline())
                with open("8ThuFT.txt", "r") as file:
                    ThuTT = eval(file.readline())
                with open("8FriFT.txt", "r") as file:
                    FriTT = eval(file.readline())
                if str.lower(inp2) == "mon" or str.lower(inp2) == "monday":
                    await ctx.send(ctx.message.author.mention + "  |  G8's Monday timetable is:")
                    for period in MonTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "tue" or str.lower(inp2) == "tues" or str.lower(inp2) == "tuesday":
                    await ctx.send(ctx.message.author.mention + "  |  G8's Tuesday timetable is:")
                    for period in TueTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "wed" or str.lower(inp2) == "wednesday":
                    await ctx.send(ctx.message.author.mention + "  |  G8's Wednesday timetable is:")
                    for period in WedTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "thu" or str.lower(inp2) == "thur" or str.lower(inp2) == "thurs" or str.lower(inp2) == "thursday":
                    await ctx.send(ctx.message.author.mention + "  |  G8's Thursday timetable is:")
                    for period in ThuTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "fri" or str.lower(inp2) == "friday":
                    await ctx.send(ctx.message.author.mention + "  |  G8's Friday timetable is:")
                    for period in FriTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "sat" or str.lower(inp2) == "saturday" or str.lower(inp2) == "sun" or str.lower(inp2) == "sunday":
                    await ctx.send(ctx.message.author.mention + "  |  There is no timetable set on the weekend")
                else:
                    await ctx.send("That is not the correct usage of that command.\n**.tt viewday G D**  -  Displays the timetable of the specified day   **G** = Grade    **D** = First letter of the day to view")
            elif inp1 == "7" or (inp1 == "11381138" and str(ctx.message.author.id) in userdata7):
                with open("7MonFT.txt", "r") as file:
                    MonTT = eval(file.readline())
                with open("7TueFT.txt", "r") as file:
                    TueTT = eval(file.readline())
                with open("7WedFT.txt", "r") as file:
                    WedTT = eval(file.readline())
                with open("7ThuFT.txt", "r") as file:
                    ThuTT = eval(file.readline())
                with open("7FriFT.txt", "r") as file:
                    FriTT = eval(file.readline())
                if str.lower(inp2) == "mon" or str.lower(inp2) == "monday":
                    await ctx.send(ctx.message.author.mention + "G7's Monday timetable is:")
                    for period in MonTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "tue" or str.lower(inp2) == "tues" or str.lower(inp2) == "tuesday":
                    await ctx.send(ctx.message.author.mention + "G7's Tuesday timetable is:")
                    for period in TueTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "wed" or str.lower(inp2) == "wednesday":
                    await ctx.send(ctx.message.author.mention + "G7's Wednesday timetable is:")
                    for period in WedTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "thu" or str.lower(inp2) == "thur" or str.lower(inp2) == "thurs" or str.lower(inp2) == "thursday":
                    await ctx.send(ctx.message.author.mention + "G7's Thursday timetable is:")
                    for period in ThuTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "fri" or str.lower(inp2) == "friday":
                    await ctx.send(ctx.message.author.mention + "G7's Friday timetable is:")
                    for period in FriTT:
                        await ctx.send(period)
                elif str.lower(inp2) == "sat" or str.lower(inp2) == "saturday" or str.lower(inp2) == "sun" or str.lower(inp2) == "sunday":
                    await ctx.send(ctx.message.author.mention + "  |  There is no timetable set on the weekend")
                else:
                    await ctx.send("That is not the correct usage of that command.\n**.tt viewday G D**  -  Displays the timetable of the specified day   **G** = Grade    **D** = First letter of the day to view")
        elif mode == "config":
            if inp1 == "11381138":
                await ctx.send("*User configuartion*\n"
                               "**.tt config clubs**  -  Allows you to view, set, and edit school clubs\n"
                               "**.tt config grade X** Allows you to change your grade if you set it incorrectly  X = The grade you want to be set as\n"
                               "**.tt config reset** Resets all of your settings to their default values\n"
                               "**.tt config reset all** Completely resets your settings, and also removes your ID from this bot's database (debug, not recommended)")
            elif inp1 == "grade":
                with open("users9.txt", "r") as file:
                    userdata9 = file.read()
                with open("users8.txt", "r") as file:
                    userdata8 = file.read()
                with open("users7.txt", "r") as file:
                    userdata7 = file.read()
                if inp2 == "9":
                    if str(ctx.message.author.id) in userdata9:
                        await ctx.send(ctx.message.author.mention + "  |  You are already set as Grade 9")
                    elif str(ctx.message.author.id) in userdata8:
                        with open("users8.txt", "r") as file:
                            tempdata = file.readlines()
                        with open("users8.txt", "w") as file:
                            file.write("\n")
                        for value in tempdata:
                            if str(ctx.message.author.id) not in str(value):
                                with open("users8.txt", "a") as file:
                                    file.write(str(value))
                        with open("users9.txt", "a") as file:
                            file.write(str(ctx.message.author.id) + "\n")
                        await ctx.send(ctx.message.author.mention + "  |  You have been set as Grade 9")
                    elif str(ctx.message.author.id) in userdata7:
                        with open("users7.txt", "r") as file:
                            tempdata = file.readlines()
                        with open("users7.txt", "w") as file:
                            file.write("\n")
                        for value in tempdata:
                            if str(ctx.message.author.id) not in str(value):
                                with open("users7.txt", "a") as file:
                                    file.write(str(value))
                        with open("users9.txt", "a") as file:
                            file.write(str(ctx.message.author.id) + "\n")
                        await ctx.send(ctx.message.author.mention + "  |  You have been set as Grade 9")
                elif inp2 == "8":
                    if str(ctx.message.author.id) in userdata8:
                        await ctx.send(ctx.message.author.mention + "  |  You are already set as Grade 8")
                    elif str(ctx.message.author.id) in userdata9:
                        with open("users9.txt", "r") as file:
                            tempdata = file.readlines()
                        with open("users9.txt", "w") as file:
                            file.write("\n")
                        for value in tempdata:
                            if str(ctx.message.author.id) not in str(value):
                                with open("users9.txt", "a") as file:
                                    file.write(str(value))
                        with open("users8.txt", "a") as file:
                            file.write(str(ctx.message.author.id) + "\n")
                        await ctx.send(ctx.message.author.mention + "  |  You have been set as Grade 8")
                    elif str(ctx.message.author.id) in userdata7:
                        with open("users7.txt", "r") as file:
                            tempdata = file.readlines()
                        with open("users7.txt", "w") as file:
                            file.write("\n")
                        for value in tempdata:
                            if str(ctx.message.author.id) not in str(value):
                                with open("users7.txt", "a") as file:
                                    file.write(str(value))
                        with open("users8.txt", "a") as file:
                            file.write(str(ctx.message.author.id) + "\n")
                        await ctx.send(ctx.message.author.mention + "  |  You have been set as Grade 8")
                elif inp2 == "7":
                    if str(ctx.message.author.id) in userdata7:
                        await ctx.send(ctx.message.author.mention + "  |  You are already set as Grade 7")
                    elif str(ctx.message.author.id) in userdata8:
                        with open("users8.txt", "r") as file:
                            tempdata = file.readlines()
                        with open("users8.txt", "w") as file:
                            file.write("\n")
                        for value in tempdata:
                            if str(ctx.message.author.id) not in str(value):
                                with open("users8.txt", "a") as file:
                                    file.write(str(value))
                        with open("users7.txt", "a") as file:
                            file.write(str(ctx.message.author.id) + "\n")
                        await ctx.send(ctx.message.author.mention + "  |  You have been set as Grade 7")
                    elif str(ctx.message.author.id) in userdata9:
                        with open("users9.txt", "r") as file:
                            tempdata = file.readlines()
                        with open("users9.txt", "w") as file:
                            file.write("\n")
                        for value in tempdata:
                            if str(ctx.message.author.id) not in str(value):
                                with open("users9.txt", "a") as file:
                                    file.write(str(value))
                        with open("users7.txt", "a") as file:
                            file.write(str(ctx.message.author.id) + "\n")
                        await ctx.send(ctx.message.author.mention + "  |  You have been set as Grade 7")
    else:
        if mode == "setgrade":
            if inp1 == "7" or inp1 == "8" or inp1 == "9":
                if inp1 == "7":
                    with open("users7.txt", "a") as file:
                        file.write(str(ctx.message.author.id) + "\n")
                elif inp1 == "8":
                    with open("users8.txt", "a") as file:
                        file.write(str(ctx.message.author.id) + "\n")
                elif inp1 == "9":
                    with open("users9.txt", "a") as file:
                        file.write(str(ctx.message.author.id) + "\n")
                await ctx.send(
                    ctx.message.author.mention + "  |  You have been set as Grade " + inp1)
            else:
                await ctx.send(ctx.message.author.mention + "  |  Please set your grade by typing **.tt setgrade X**, where **X** is your grade number.")
        else:
            await ctx.send("Hello " + ctx.message.author.mention + ". You have not yet been registered in my database\nPlease tell me what grade you are in by typing **.tt setgrade X**, where **X** is your grade number\n*(You can always change this later if needed by using **.tt config**)*")


client.run(BOT_TOKEN)
