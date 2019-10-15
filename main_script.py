import time
import discord
from discord.ext import commands

bot_name = "TimeTableBot"

bot_owner_id = "402344993391640578"

club_CHI = "MYP Chilled Out Zone"
club_IMP = "Imperial Assault campaign club"
club_TTR = "Tinker Thinker Reader"
club_BND = "Advanced Band"
club_LGA = "Let's Get Active"
club_CAL = "Calligraphy"
club_FTY = "Touch Footy"
club_R20 = "Role 20"
club_MUS = "Music Video Club"
club_MKC = "Model Kit Construction"
club_IKE = "Ikebana"
club_MSS = "Modern Survival Skills"
club_BSK = "Basketball"

sp_NULL = "No class"
sp_NUCL = "No club"
sp_HMRM = "Homeroom"
sp_AMRE = "Morning recess"
sp_LNCH = "Lunch"
sp_LNRE = "Lunch recess"
sp_PMRE = "Afternoon recess"
CurrentPeriod = "customerror"
NextPeriod = "customerror"

id_CHI = ("chi", "myp chill out club", "myp chill out", "chill", "chill out", "chill out club", "chill club", "myp chill club")
id_IMP = ("imp", "imperial assault", "star wars imperial assault", "star wars: imperial assault")
id_TTR = ("ttr", "tinker", "thinker", "reader", "homework", "hw", "tinker thinker", "tinker thinker reader")
id_BND = ("bnd", "band", "advanced band", "adv", "adv band")
id_LGA = ("lga", "let's get active", "active", "get active")
id_CAL = ("cal", "calligraphy")
id_FTY = ("fty", "footy", "touch footy")
id_R20 = ("r20", "role 20", "rp", "roleplay")
id_MUS = ("mus", "music video", "music video club")
id_MKC = ("mkc", "mdl", "model", "model kit", "kit construction", "model kit construction", "kit", "model construction", "construction")
id_IKE = ("ike", "ikebana", "ikebana club")
id_MSS = ("mss", "survival", "survival skills", "modern survival", "modern survival skills")
id_BSK = ("bsk", "basketball", "basketball club")

with open("club_BND_MON", "r") as file:
    club_BND_MON = file.read()
with open("club_LGA_MON", "r") as file:
    club_LGA_MON = file.read()
with open("club_TTR_MON", "r") as file:
    club_TTR_MON = file.read()

with open("club_TTR_TUE", "r") as file:
    club_TTR_TUE = file.read()
with open("club_CAL_TUE", "r") as file:
    club_CAL_TUE = file.read()
with open("club_CHI_TUE", "r") as file:
    club_CHI_TUE = file.read()

with open("club_FTY_WED", "r") as file:
    club_FTY_WED = file.read()

with open("club_TTR_THU", "r") as file:
    club_TTR_THU = file.read()
with open("club_IMP_THU", "r") as file:
    club_IMP_THU = file.read()
with open("club_MKC_THU", "r") as file:
    club_MKC_THU = file.read()
with open("club_MUS_THU", "r") as file:
    club_MUS_THU = file.read()
with open("club_R20_THU", "r") as file:
    club_R20_THU = file.read()

with open("club_TTR_FRI", "r") as file:
    club_TTR_FRI = file.read()
with open("club_CHI_FRI", "r") as file:
    club_CHI_FRI = file.read()
with open("club_IKE_FRI", "r") as file:
    club_IKE_FRI = file.read()
with open("club_BSK_FRI", "r") as file:
    club_BSK_FRI = file.read()
with open("club_MSS_FRI", "r") as file:
    club_MSS_FRI = file.read()


def SetNextPeriod(grade, idvar="11381138"):
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
                time.localtime()[3] == 14 and time.localtime()[4] < 30):
            NextPeriod = MonTT[4]

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            NextPeriod = sp_HMRM
        #  3:45 to 4:15
        elif (time.localtime()[3] == 15 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 16 and time.localtime()[4] < 15):
            if ViewClub("Monday", str(idvar)) == "null":
                NextPeriod = TueTT[0]
            else:
                NextPeriod = ViewClub("Monday", str(idvar))
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
                time.localtime()[3] == 14 and time.localtime()[4] < 30):
            NextPeriod = TueTT[4]

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            NextPeriod = sp_HMRM
        #  3:45 to 4:15
        elif (time.localtime()[3] == 15 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 16 and time.localtime()[4] < 15):
            if ViewClub("Tuesday", str(idvar)) == "null":
                NextPeriod = WedTT[0]
            else:
                NextPeriod = ViewClub("Tuesday", str(idvar))
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
            if ViewClub("Wednesday", str(idvar)) == "null":
                NextPeriod = ThuTT[0]
            else:
                NextPeriod = ViewClub("Wednesday", str(idvar))
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
                time.localtime()[3] == 14 and time.localtime()[4] < 30):
            NextPeriod = ThuTT[4]

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            NextPeriod = sp_HMRM
        #  3:45 to 4:15
        elif (time.localtime()[3] == 15 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 16 and time.localtime()[4] < 15):
            if ViewClub("Thursday", str(idvar)) == "null":
                NextPeriod = FriTT[0]
            else:
                NextPeriod = ViewClub("Thursday", str(idvar))
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
                time.localtime()[3] == 14 and time.localtime()[4] < 30):
            NextPeriod = FriTT[4]

        #  2:45 to 3:45
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 15 and time.localtime()[4] < 45):
            NextPeriod = sp_HMRM
        #  3:45 to 4:15
        elif (time.localtime()[3] == 15 and time.localtime()[4] >= 45) or (
                time.localtime()[3] == 16 and time.localtime()[4] < 15):
            if ViewClub("Friday", str(idvar)) == "null":
                NextPeriod = MonTT[0]
            else:
                NextPeriod = ViewClub("Friday", str(idvar))
        else:
            NextPeriod = MonTT[0]
    else:
        NextPeriod = MonTT[0]
    return NextPeriod


def SetCurrentPeriod(grade, idvar="11381138"):
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
                time.localtime()[3] == 14 and time.localtime()[4] < 30):
            CurrentPeriod = MonTT[3]

        #  2:30 to 2:45
        elif time.localtime()[3] == 14 and 30 < time.localtime()[4] > 45:
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
            CurrentPeriod = ViewClub(Day(), str(idvar))

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
                time.localtime()[3] == 14 and time.localtime()[4] < 30):
            CurrentPeriod = TueTT[3]

        #  2:30 to 2:45
        elif time.localtime()[3] == 14 and 30 < time.localtime()[4] > 45:
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
            CurrentPeriod = ViewClub(Day(), str(idvar))

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
                time.localtime()[3] == 14 and time.localtime()[4] < 30):
            CurrentPeriod = WedTT[3]

        #  2:30 to 3:30
        elif (time.localtime()[3] == 14 and time.localtime()[4] >= 30) or (time.localtime()[3] == 15 and time.localtime()[4] < 30):
            CurrentPeriod = ViewClub(Day(), str(idvar))

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
                time.localtime()[3] == 14 and time.localtime()[4] < 30):
            CurrentPeriod = ThuTT[3]

        #  2:30 to 2:45
        elif time.localtime()[3] == 14 and 30 < time.localtime()[4] > 45:
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
            CurrentPeriod = ViewClub(Day(), str(idvar))

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
                time.localtime()[3] == 14 and time.localtime()[4] < 30):
            CurrentPeriod = FriTT[3]

        #  2:30 to 2:45
        elif time.localtime()[3] == 14 and 30 < time.localtime()[4] > 45:
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
            CurrentPeriod = ViewClub(Day(), str(idvar))

        #  Else
        else:
            CurrentPeriod = sp_NULL

    #   Other
    else:
        CurrentPeriod = sp_NULL

    return CurrentPeriod

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

def Remove_Club(id, club_filename):
    with open(club_filename, "r") as file:
        tempdata = file.readlines()
    with open(club_filename, "w") as file:
        file.write("\n")
    for value in tempdata:
        if str(id) not in str(value):
            with open(club_filename, "a") as file:
                file.write(str(value))

client = commands.Bot(command_prefix=".")

with open("users9.txt", "r") as file:
    userdata9 = file.read()
with open("users8.txt", "r") as file:
    userdata8 = file.read()
with open("users7.txt", "r") as file:
    userdata7 = file.read()


def AddStats(idinp, statinp):
    stat = str.lower(statinp)
    value = 1
    id = str.lower(idinp)
    with open("stats7.txt", "r") as file:
        statfile7 = eval(file.readline())
    with open("stats8.txt", "r") as file:
        statfile8 = eval(file.readline())
    with open("stats9.txt", "r") as file:
        statfile9 = eval(file.readline())
    with open("users9.txt", "r") as file:
        userdata9 = file.read()
    with open("users8.txt", "r") as file:
        userdata8 = file.read()
    with open("users7.txt", "r") as file:
        userdata7 = file.read()
    if id in userdata9:
        if stat == "tt":
            statfile9[0] += value
        elif stat == "valid_day":
            statfile9[1] += value
        elif stat == "mon":
            statfile9[2] += value
        elif stat == "tue":
            statfile9[3] += value
        elif stat == "wed":
            statfile9[4] += value
        elif stat == "thu":
            statfile9[5] += value
        elif stat == "fri":
            statfile9[6] += value
        elif stat == "club":
            statfile9[7] += value
        elif stat == "grade":
            statfile9[8] += value
        elif stat == "invalid_day":
            statfile9[9] += value
        elif stat == "valid_config":
            statfile9[10] += value
        elif stat == "invalid_config":
            statfile9[11] += value
        elif stat == "invalid_tt":
            statfile9[12] += value
        elif stat == "invalid_admin":
            statfile9[13] += value
        elif stat == "help":
            statfile9[14] += value
        elif stat == "valid_admin":
            statfile9[15] += value
        elif stat == "tt_overview":
            statfile9[16] += value
        elif stat == "tt_registration":
            statfile9[17] += value
        elif stat == "sat":
            statfile9[18] += value
        elif stat == "sun":
            statfile9[19] += value
        elif stat == "reset_normal":
            statfile9[20] += value
        elif stat == "reset_full":
            statfile9[21] += value
    elif id in userdata8:
        if stat == "tt":
            statfile8[0] += value
        elif stat == "valid_day":
            statfile8[1] += value
        elif stat == "mon":
            statfile8[2] += value
        elif stat == "tue":
            statfile8[3] += value
        elif stat == "wed":
            statfile8[4] += value
        elif stat == "thu":
            statfile8[5] += value
        elif stat == "fri":
            statfile8[6] += value
        elif stat == "club":
            statfile8[7] += value
        elif stat == "grade":
            statfile8[8] += value
        elif stat == "invalid_day":
            statfile8[9] += value
        elif stat == "valid_config":
            statfile8[10] += value
        elif stat == "invalid_config":
            statfile8[11] += value
        elif stat == "invalid_tt":
            statfile8[12] += value
        elif stat == "invalid_admin":
            statfile8[13] += value
        elif stat == "help":
            statfile8[14] += value
        elif stat == "valid_admin":
            statfile8[15] += value
        elif stat == "tt_overview":
            statfile8[16] += value
        elif stat == "tt_registration":
            statfile8[17] += value
        elif stat == "sat":
            statfile8[18] += value
        elif stat == "sun":
            statfile8[19] += value
        elif stat == "reset_normal":
            statfile8[20] += value
        elif stat == "reset_full":
            statfile8[21] += value
    elif id in userdata7:
        if stat == "tt":
            statfile7[0] += value
        elif stat == "valid_day":
            statfile7[1] += value
        elif stat == "mon":
            statfile7[2] += value
        elif stat == "tue":
            statfile7[3] += value
        elif stat == "wed":
            statfile7[4] += value
        elif stat == "thu":
            statfile7[5] += value
        elif stat == "fri":
            statfile7[6] += value
        elif stat == "club":
            statfile7[7] += value
        elif stat == "grade":
            statfile7[8] += value
        elif stat == "invalid_day":
            statfile7[9] += value
        elif stat == "valid_config":
            statfile7[10] += value
        elif stat == "invalid_config":
            statfile7[11] += value
        elif stat == "invalid_tt":
            statfile7[12] += value
        elif stat == "invalid_admin":
            statfile7[13] += value
        elif stat == "help":
            statfile7[14] += value
        elif stat == "valid_admin":
            statfile7[15] += value
        elif stat == "tt_overview":
            statfile7[16] += value
        elif stat == "tt_registration":
            statfile7[17] += value
        elif stat == "sat":
            statfile7[18] += value
        elif stat == "sun":
            statfile7[19] += value
        elif stat == "reset_normal":
            statfile7[20] += value
        elif stat == "reset_full":
            statfile7[21] += value
    with open("stats9.txt", "w") as file:
        file.write(str(statfile9))
    with open("stats8.txt", "w") as file:
        file.write(str(statfile8))
    with open("stats7.txt", "w") as file:
        file.write(str(statfile7))


def ViewClub(dayinp, idinp):
    day = str.lower(dayinp)
    id = str.lower(idinp)
    with open("club_BND_MON", "r") as file:
        club_BND_MON = file.read()
    with open("club_LGA_MON", "r") as file:
        club_LGA_MON = file.read()
    with open("club_TTR_MON", "r") as file:
        club_TTR_MON = file.read()

    with open("club_TTR_TUE", "r") as file:
        club_TTR_TUE = file.read()
    with open("club_CAL_TUE", "r") as file:
        club_CAL_TUE = file.read()
    with open("club_CHI_TUE", "r") as file:
        club_CHI_TUE = file.read()

    with open("club_FTY_WED", "r") as file:
        club_FTY_WED = file.read()

    with open("club_TTR_THU", "r") as file:
        club_TTR_THU = file.read()
    with open("club_IMP_THU", "r") as file:
        club_IMP_THU = file.read()
    with open("club_MKC_THU", "r") as file:
        club_MKC_THU = file.read()
    with open("club_MUS_THU", "r") as file:
        club_MUS_THU = file.read()
    with open("club_R20_THU", "r") as file:
        club_R20_THU = file.read()

    with open("club_TTR_FRI", "r") as file:
        club_TTR_FRI = file.read()
    with open("club_CHI_FRI", "r") as file:
        club_CHI_FRI = file.read()
    with open("club_IKE_FRI", "r") as file:
        club_IKE_FRI = file.read()
    with open("club_BSK_FRI", "r") as file:
        club_BSK_FRI = file.read()
    with open("club_MSS_FRI", "r") as file:
        club_MSS_FRI = file.read()
    if day == "monday":
        if id in club_BND_MON:
            return club_BND
        elif id in club_LGA_MON:
            return club_LGA
        elif id in club_TTR_MON:
            return club_TTR
        else:
            return "null"
    elif day == "tuesday":
        if id in club_TTR_TUE:
            return club_TTR
        elif id in club_CAL_TUE:
            return club_CAL
        elif id in club_CHI_TUE:
            return club_CHI
        else:
            return "null"
    elif day == "wednesday":
        if id in club_FTY_WED:
            return club_FTY
        else:
            return "null"
    elif day == "thursday":
        if id in club_TTR_THU:
            return club_TTR
        elif id in club_IMP_THU:
            return club_IMP
        elif id in club_MKC_THU:
            return club_MKC
        elif id in club_MUS_THU:
            return club_MUS
        elif id in club_R20_THU:
            return club_R20
        else:
            return "null"
    elif day == "friday":
        if id in club_TTR_FRI:
            return club_TTR
        elif id in club_CHI_FRI:
            return club_CHI
        elif id in club_IKE_FRI:
            return club_IKE
        elif id in club_BSK_FRI:
            return club_BSK
        elif id in club_MSS_FRI:
            return club_MSS
        else:
            return "null"
    else:
        return "null"


stat_tt = "tt"
stat_tt_overview = "tt_overview"
stat_tt_registration = "tt_registration"
stat_valid_day = "valid_day"
stat_invalid_day = "invalid_day"
stat_valid_config = "valid_config"
stat_invalid_config = "invalid_config"
stat_mon = "mon"
stat_tue = "tue"
stat_wed = "wed"
stat_thu = "thu"
stat_fri = "fri"
stat_sat = "sat"
stat_sun = "sun"
stat_club = "club"
stat_grade = "grade"
stat_invalid_tt = "invalid_tt"
stat_invalid_admin = "invalid_admin"
stat_valid_admin = "valid_admin"
stat_help = "help"
stat_reset_normal = "reset_normal"
stat_reset_full = "reset_full"

valid_filenames = ("7MonFT.txt", "7TueFT.txt", "7WedFT.txt", "7ThuFT.txt", "7FriFT.txt", "8MonFT.txt", "8TueFT.txt", "8WedFT.txt", "8ThuFT.txt", "8FriFT.txt", "9MonFT.txt", "9TueFT.txt", "9WedFT.txt", "9ThuFT.txt", "9FriFT.txt", "club_BND_MON", "club_BSK_FRI", "club_CAL_TUE", "club_CHI_FRI"
                   , "club_CHI_TUE", "club_FTY_WED", "club_IKE_FRI", "club_IMP_THU", "club_LGA_MON", "club_MKC_THU", "club_MSS_FRI", "club_MUS_THU", "club_R20_THU", "club_TTR_FRI", "club_TTR_MON", "club_TTR_THU", "club_TTR_TUE"
                   , "stats7.txt", "stats8.txt", "stats9.txt", "users7.txt", "users8.txt", "users9.txt")


@client.event
async def on_ready():
    print(bot_name + " is now running")
    await client.change_presence(activity=discord.Game("Use '.tt ?' for info"))

@client.command(pass_context=True)
async def debug(ctx, mode="11381138", var1="11381138", var2="11381138", *, note=" "):
    with open("debugpermissions.txt", "r") as file:
        debug_ids = file.read()
    if str(ctx.message.author.id) in debug_ids:
        AddStats(str(ctx.message.author.id), stat_valid_admin)
        if str.lower(mode) == "userids":
            with open("users9.txt", "r") as file:
                userdata9 = file.read()
            with open("users8.txt", "r") as file:
                userdata8 = file.read()
            with open("users7.txt", "r") as file:
                userdata7 = file.read()

            if str.lower(var1) == "9":
                if str.lower(var2) == "dm":
                    await ctx.send(ctx.message.author.mention + "  |  A DM has been sent to you")
                    await ctx.author.send("Grade 9 user id list:\n" + userdata9)
                elif str.lower(var2) == "here":
                    await ctx.send(ctx.message.author.mention + "  |  Grade 9 user id list:\n" + userdata9)
                else:
                    await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command. Use **.debug help** for info")
            elif str.lower(var1) == "8":
                if str.lower(var2) == "dm":
                    await ctx.send(ctx.message.author.mention + "  |  A DM has been sent to you")
                    await ctx.author.send("Grade 8 user id list:\n" + userdata8)
                elif str.lower(var2) == "here":
                    await ctx.send(ctx.message.author.mention + "  |  Grade 8 user id list:\n" + userdata8)
                else:
                    await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command. Use **.debug help** for info")
            elif str.lower(var1) == "7":
                if str.lower(var2) == "dm":
                    await ctx.send(ctx.message.author.mention + "  |  A DM has been sent to you")
                    await ctx.author.send("Grade 8 user id list:\n" + userdata8)
                elif str.lower(var2) == "here":
                    await ctx.send(ctx.message.author.mention + "  |  Grade 8 user id list:\n" + userdata8)
                else:
                    await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command. Use **.debug help** for info")
            elif str.lower(var1) == "all":
                if str.lower(var2) == "dm":
                    await ctx.author.send("All user id lists\n \n" + "Grade 9 user id list:\n" + userdata9 + "\nGrade 8 user id list:\n" + userdata8 + "\nGrade 7 user id list:\n" + userdata7)
                    await ctx.send(ctx.message.author.mention + "  |  A DM has been sent to you")
                elif str.lower(var2) == "here":
                    await ctx.send(ctx.message.author.mention + "  |  All user id lists\n \n" + "Grade 9 user id list:\n" + userdata9 + "\nGrade 8 user id list:\n" + userdata8 + "\nGrade 7 user id list:\n" + userdata7)
                else:
                    await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command. Use **.debug help** for info")
            else:
                await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command. Use **.debug help** for info")
        elif str.lower(mode) == "stats":
            with open("stats9.txt", "r") as file:
                statfile9 = eval(file.readline())
            with open("stats8.txt", "r") as file:
                statfile8 = eval(file.readline())
            with open("stats7.txt", "r") as file:
                statfile7 = eval(file.readline())
            if str.lower(var1) == "9":
                if str.lower(var2) == "here":
                    await ctx.send(ctx.message.author.mention + "  |  **Grade 9 statistics:**\n \nAll **.tt** commands - " + str(statfile9[0]) +
                                   "\n \n**.tt** (registration) - " + str(statfile9[17]) + "\n**.tt** (overview) - " + str(statfile9[16]) + "\n**.tt help** - " + str(statfile9[14]) + "\n \n**.tt day** (valid) - " + str(statfile9[1]) + "\n**.tt day** (Monday) - " + str(statfile9[2]) + "\n**.tt day** (Tuesday) - " + str(statfile9[3]) + "\n**.tt day** (Wednesday) - " + str(statfile9[4]) + "\n**.tt day** (Thursday) - " + str(statfile9[5]) + "\n**.tt day** (Friday) - " +
                                   str(statfile9[6]) + "\n**.tt day** (invalid) - " + str(statfile9[9]) +
                                   "\n \n**.tt config** (valid) - " + str(statfile9[10]) + "\n**.tt config grade** - " + str(statfile9[8]) + "\n**.tt config club** - " + str(statfile9[7]) + "\n**.tt config reset** - " + str(statfile9[20]) + "\n**.tt config reset all** - " + str(statfile9[21]) + "\n**.tt config** (invalid) - " + str(statfile9[11]) +
                                   "\n \n**.debug** (valid) - " + str(statfile9[15]) + "\n**.debug** (invalid) - " + str(statfile9[13]))
                elif str.lower(var2) == "dm":
                    await ctx.author.send("**Grade 9 statistics:**\n \nAll **.tt** commands - " + str(statfile9[0]) +
                                          "\n \n**.tt** (registration) - " + str(statfile9[17]) + "\n**.tt** (overview) - " + str(statfile9[16]) + "\n**.tt help** - " + str(statfile9[14]) + "\n \n**.tt day** (valid) - " + str(statfile9[1]) + "\n**.tt day** (Monday) - " + str(statfile9[2]) + "\n**.tt day** (Tuesday) - " + str(statfile9[3]) + "\n**.tt day** (Wednesday) - " + str(statfile9[4]) + "\n**.tt day** (Thursday) - " + str(statfile9[5]) + "\n**.tt day** (Friday) - " +
                                          str(statfile9[6]) + "\n**.tt day** (invalid) - " + str(statfile9[9]) +
                                          "\n \n**.tt config** (valid) - " + str(statfile9[10]) + "\n**.tt config grade** - " + str(statfile9[8]) + "\n**.tt config club** - " + str(statfile9[7]) + "\n**.tt config reset** - " + str(statfile9[20]) + "\n**.tt config reset all** - " + str(statfile9[21]) + "\n**.tt config** (invalid) - " + str(statfile9[11]) +
                                          "\n \n**.debug** (valid) - " + str(statfile9[15]) + "\n**.debug** (invalid) - " + str(statfile9[13]))
                    await ctx.send(ctx.message.author.mention + "  |  A DM has been sent to you")
                else:
                    await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command. Use **.debug help** for info")
            elif str.lower(var1) == "8":
                if str.lower(var2) == "here":
                    await ctx.send(ctx.message.author.mention + "  |  **Grade 8 statistics:**\n \nAll **.tt** commands - " + str(statfile8[0]) +
                                   "\n \n**.tt** (registration) - " + str(statfile8[17]) + "\n**.tt** (overview) - " + str(statfile8[16]) + "\n**.tt help** - " + str(statfile8[14]) + "\n \n**.tt day** (valid) - " + str(statfile8[1]) + "\n**.tt day** (Monday) - " + str(statfile8[2]) + "\n**.tt day** (Tuesday) - " + str(statfile8[3]) + "\n**.tt day** (Wednesday) - " + str(statfile8[4]) + "\n**.tt day** (Thursday) - " + str(statfile8[5]) + "\n**.tt day** (Friday) - " +
                                   str(statfile8[6]) + "\n**.tt day** (invalid) - " + str(statfile8[9]) +
                                   "\n \n**.tt config** (valid) - " + str(statfile8[10]) + "\n**.tt config grade** - " + str(statfile8[8]) + "\n**.tt config club** - " + str(statfile8[7]) + "\n**.tt config reset** - " + str(statfile8[20]) + "\n**.tt config reset all** - " + str(statfile8[21]) + "\n**.tt config** (invalid) - " + str(statfile8[11]) +
                                   "\n \n**.debug** (valid) - " + str(statfile8[15]) + "\n**.debug** (invalid) - " + str(statfile8[13]))
                elif str.lower(var2) == "dm":
                    await ctx.author.send("**Grade 8 statistics:**\n \nAll **.tt** commands - " + str(statfile8[0]) +
                                          "\n \n**.tt** (registration) - " + str(statfile8[17]) + "\n**.tt** (overview) - " + str(statfile8[16]) + "\n**.tt help** - " + str(statfile8[14]) + "\n \n**.tt day** (valid) - " + str(statfile8[1]) + "\n**.tt day** (Monday) - " + str(statfile8[2]) + "\n**.tt day** (Tuesday) - " + str(statfile8[3]) + "\n**.tt day** (Wednesday) - " + str(statfile8[4]) + "\n**.tt day** (Thursday) - " + str(statfile8[5]) + "\n**.tt day** (Friday) - " +
                                          str(statfile8[6]) + "\n**.tt day** (invalid) - " + str(statfile8[9]) +
                                          "\n \n**.tt config** (valid) - " + str(statfile8[10]) + "\n**.tt config grade** - " + str(statfile8[8]) + "\n**.tt config club** - " + str(statfile8[7]) + "\n**.tt config reset** - " + str(statfile8[20]) + "\n**.tt config reset all** - " + str(statfile8[21]) + "\n**.tt config** (invalid) - " + str(statfile8[11]) +
                                          "\n \n**.debug** (valid) - " + str(statfile8[15]) + "\n**.debug** (invalid) - " + str(statfile8[13]))
                    await ctx.send(ctx.message.author.mention + "  |  A DM has been sent to you")
                else:
                    await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command. Use **.debug help** for info")
            elif str.lower(var1) == "7":
                if str.lower(var2) == "here":
                    await ctx.send(ctx.message.author.mention + "  |  **Grade 7 statistics:**\n \nAll **.tt** commands - " + str(statfile7[0]) +
                                   "\n \n**.tt** (registration) - " + str(statfile7[17]) + "\n**.tt** (overview) - " + str(statfile7[16]) + "\n**.tt help** - " + str(statfile7[14]) + "\n \n**.tt day** (valid) - " + str(statfile7[1]) + "\n**.tt day** (Monday) - " + str(statfile7[2]) + "\n**.tt day** (Tuesday) - " + str(statfile7[3]) + "\n**.tt day** (Wednesday) - " + str(statfile7[4]) + "\n**.tt day** (Thursday) - " + str(statfile7[5]) + "\n**.tt day** (Friday) - " +
                                   str(statfile7[6]) + "\n**.tt day** (invalid) - " + str(statfile7[9]) +
                                   "\n \n**.tt config** (valid) - " + str(statfile7[10]) + "\n**.tt config grade** - " + str(statfile7[8]) + "\n**.tt config club** - " + str(statfile7[7]) + "\n**.tt config reset** - " + str(statfile7[20]) + "\n**.tt config reset all** - " + str(statfile7[21]) + "\n**.tt config** (invalid) - " + str(statfile7[11]) +
                                   "\n \n**.debug** (valid) - " + str(statfile7[15]) + "\n**.debug** (invalid) - " + str(statfile7[13]))
                elif str.lower(var2) == "dm":
                    await ctx.author.send("**Grade 7 statistics:**\n \nAll **.tt** commands - " + str(statfile7[0]) +
                                          "\n \n**.tt** (registration) - " + str(statfile7[17]) + "\n**.tt** (overview) - " + str(statfile7[16]) + "\n**.tt help** - " + str(statfile7[14]) + "\n \n**.tt day** (valid) - " + str(statfile7[1]) + "\n**.tt day** (Monday) - " + str(statfile7[2]) + "\n**.tt day** (Tuesday) - " + str(statfile7[3]) + "\n**.tt day** (Wednesday) - " + str(statfile7[4]) + "\n**.tt day** (Thursday) - " + str(statfile7[5]) + "\n**.tt day** (Friday) - " +
                                          str(statfile7[6]) + "\n**.tt day** (invalid) - " + str(statfile7[9]) +
                                          "\n \n**.tt config** (valid) - " + str(statfile7[10]) + "\n**.tt config grade** - " + str(statfile7[8]) + "\n**.tt config club** - " + str(statfile7[7]) + "\n**.tt config reset** - " + str(statfile7[20]) + "\n**.tt config reset all - " + str(statfile7[21]) + "\n**.tt config** (invalid) - " + str(statfile7[11]) +
                                          "\n \n**.debug** (valid) - " + str(statfile7[15]) + "\n**.debug** (invalid) - " + str(statfile7[13]))
                    await ctx.send(ctx.message.author.mention + "  |  A DM has been sent to you")
                else:
                    await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command. Use **.debug help** for info")
            elif str.lower(var1) == "all":
                if str.lower(var2) == "here":
                    await ctx.send(ctx.message.author.mention + "  |  All user statistics - \n \n \n***Grade 9:***\n \nAll **.tt** commands - " + str(statfile9[0]) +
                                   "\n \n**.tt** (registration) - " + str(statfile9[17]) + "\n**.tt** (overview) - " + str(statfile9[16]) + "\n**.tt help** - " + str(statfile9[14]) + "\n \n**.tt day** (valid) - " + str(statfile9[1]) + "\n**.tt day** (Monday) - " + str(statfile9[2]) + "\n**.tt day** (Tuesday) - " + str(statfile9[3]) + "\n**.tt day** (Wednesday) - " + str(statfile9[4]) + "\n**.tt day** (Thursday) - " + str(statfile9[5]) + "\n**.tt day** (Friday) - " +
                                   str(statfile9[6]) + "\n**.tt day** (invalid) - " + str(statfile9[9]) +
                                   "\n \n**.tt config** (valid) - " + str(statfile9[10]) + "\n**.tt config grade** - " + str(statfile9[8]) + "\n**.tt config club** - " + str(statfile9[7]) + "\n**.tt config reset** - " + str(statfile9[20]) + "\n**.tt config reset all** - " + str(statfile9[21]) + "\n**.tt config** (invalid) - " + str(statfile9[11]) +
                                   "\n \n**.debug** (valid) - " + str(statfile9[15]) + "\n**.debug** (invalid) - " + str(statfile9[13]) + "\n \n \n***Grade 8:***\n \nAll **.tt** commands - " + str(statfile8[0]) +
                                   "\n \n**.tt** (registration) - " + str(statfile8[17]) + "\n**.tt** (overview) - " + str(statfile8[16]) + "\n**.tt help** - " + str(statfile8[14]) + "\n \n**.tt day** (valid) - " + str(statfile8[1]) + "\n**.tt day** (Monday) - " + str(statfile8[2]) + "\n**.tt day** (Tuesday) - " + str(statfile8[3]) + "\n**.tt day** (Wednesday) - " + str(statfile8[4]) + "\n**.tt day** (Thursday) - " + str(statfile8[5]) + "\n**.tt day** (Friday) - " +
                                   str(statfile8[6]) + "\n**.tt day** (invalid) - " + str(statfile8[9]) +
                                   "\n \n**.tt config** (valid) - " + str(statfile8[10]) + "\n**.tt config grade** - " + str(statfile8[8]) + "\n**.tt config club** - " + str(statfile8[7]) + "\n**.tt config reset** - " + str(statfile8[20]) + "\n**.tt config reset all** - " + str(statfile8[21]) + "\n**.tt config** (invalid) - " + str(statfile8[11]) +
                                   "\n \n**.debug** (valid) - " + str(statfile8[15]) + "\n**.debug** (invalid) - " + str(statfile8[13]) + "\n \n \n***Grade 7:***\n \nAll **.tt** commands - " + str(statfile7[0]) +
                                   "\n \n**.tt** (registration) - " + str(statfile7[17]) + "\n**.tt** (overview) - " + str(statfile7[16]) + "\n**.tt help** - " + str(statfile7[14]) + "\n \n**.tt day** (valid) - " + str(statfile7[1]) + "\n**.tt day** (Monday) - " + str(statfile7[2]) + "\n**.tt day** (Tuesday) - " + str(statfile7[3]) + "\n**.tt day** (Wednesday) - " + str(statfile7[4]) + "\n**.tt day** (Thursday) - " + str(statfile7[5]) + "\n**.tt day** (Friday) - " +
                                   str(statfile7[6]) + "\n**.tt day** (invalid) - " + str(statfile7[9]) +
                                   "\n \n**.tt config** (valid) - " + str(statfile7[10]) + "\n**.tt config grade** - " + str(statfile7[8]) + "\n**.tt config club** - " + str(statfile7[7]) + "\n**.tt config reset** - " + str(statfile7[20]) + "\n**.tt config reset all** - " + str(statfile7[21]) + "\n**.tt config** (invalid) - " + str(statfile7[11]) +
                                   "\n \n**.debug** (valid) - " + str(statfile7[15]) + "\n**.debug** (invalid) - " + str(statfile7[13]))
                elif str.lower(var2) == "dm":
                    await ctx.author.send("All user statistics - \n \n \n***Grade 9:***\n \nAll **.tt** commands - " + str(statfile9[0]) +
                                          "\n \n**.tt** (registration) - " + str(statfile9[17]) + "\n**.tt** (overview) - " + str(statfile9[16]) + "\n**.tt help** - " + str(statfile9[14]) + "\n \n**.tt day** (valid) - " + str(statfile9[1]) + "\n**.tt day** (Monday) - " + str(statfile9[2]) + "\n**.tt day** (Tuesday) - " + str(statfile9[3]) + "\n**.tt day** (Wednesday) - " + str(statfile9[4]) + "\n**.tt day** (Thursday) - " + str(statfile9[5]) + "\n**.tt day** (Friday) - " +
                                          str(statfile9[6]) + "\n**.tt day** (invalid) - " + str(statfile9[9]) +
                                          "\n \n**.tt config** (valid) - " + str(statfile9[10]) + "\n**.tt config grade** - " + str(statfile9[8]) + "\n**.tt config club** - " + str(statfile9[7]) + "\n**.tt config reset** - " + str(statfile9[20]) + "\n**.tt config reset all** - " + str(statfile9[21]) + "\n**.tt config** (invalid) - " + str(statfile9[11]) +
                                          "\n \n**.debug** (valid) - " + str(statfile9[15]) + "\n**.debug** (invalid) - " + str(statfile9[13]) + "\n \n \n***Grade 8:***\n \nAll **.tt** commands - " + str(statfile8[0]) +
                                          "\n \n**.tt** (registration) - " + str(statfile8[17]) + "\n**.tt** (overview) - " + str(statfile8[16]) + "\n**.tt help** - " + str(statfile8[14]) + "\n \n**.tt day** (valid) - " + str(statfile8[1]) + "\n**.tt day** (Monday) - " + str(statfile8[2]) + "\n**.tt day** (Tuesday) - " + str(statfile8[3]) + "\n**.tt day** (Wednesday) - " + str(statfile8[4]) + "\n**.tt day** (Thursday) - " + str(statfile8[5]) + "\n**.tt day** (Friday) - " +
                                          str(statfile8[6]) + "\n**.tt day** (invalid) - " + str(statfile8[9]) +
                                          "\n \n**.tt config** (valid) - " + str(statfile8[10]) + "\n**.tt config grade** - " + str(statfile8[8]) + "\n**.tt config club** - " + str(statfile8[7]) + "\n**.tt config reset** - " + str(statfile8[20]) + "\n**.tt config reset all** - " + str(statfile8[21]) + "\n**.tt config** (invalid) - " + str(statfile8[11]) +
                                          "\n \n**.debug** (valid) - " + str(statfile8[15]) + "\n**.debug** (invalid) - " + str(statfile8[13]) + "\n \n \n***Grade 7:***\n \nAll **.tt** commands - " + str(statfile7[0]) +
                                          "\n \n**.tt** (registration) - " + str(statfile7[17]) + "\n**.tt** (overview) - " + str(statfile7[16]) + "\n**.tt help** - " + str(statfile7[14]) + "\n \n**.tt day** (valid) - " + str(statfile7[1]) + "\n**.tt day** (Monday) - " + str(statfile7[2]) + "\n**.tt day** (Tuesday) - " + str(statfile7[3]) + "\n**.tt day** (Wednesday) - " + str(statfile7[4]) + "\n**.tt day** (Thursday) - " + str(statfile7[5]) + "\n**.tt day** (Friday) - " +
                                          str(statfile7[6]) + "\n**.tt day** (invalid) - " + str(statfile7[9]) +
                                          "\n \n**.tt config** (valid) - " + str(statfile7[10]) + "\n**.tt config grade** - " + str(statfile7[8]) + "\n**.tt config club** - " + str(statfile7[7]) + "\n**.tt config reset** - " + str(statfile7[20]) + "\n**.tt config reset all** - " + str(statfile7[21]) + "\n**.tt config** (invalid) - " + str(statfile7[11]) +
                                          "\n \n**.debug** (valid) - " + str(statfile7[15]) + "\n**.debug** (invalid) - " + str(statfile7[13]))
                    await ctx.send(ctx.message.author.mention + "  |  A DM has been sent to you")
                else:
                    await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command. Use **.debug help** for info")
            else:
                await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command. Use **.debug help** for info")
        elif str.lower(mode) == "lock":
            if str(ctx.message.author.id) == bot_owner_id:
                with open("lock_parameters.txt", "r") as file:
                    global_variables = eval(file.readline())
                global_variables[0] = 1
                global_variables[1] = " " + str(var1) + " " + str(var2) + " " + str(note)
                with open("lock_parameters.txt", "w") as file:
                    file.write(str(global_variables))
                await ctx.send(ctx.message.author.mention + "  |  " + bot_name + " has been locked")
            else:
                await ctx.send(ctx.message.author.mention + "  |  Only the bot owner has permission to use that command")
        elif str.lower(mode) == "unlock":
            with open("lock_parameters.txt", "r") as file:
                global_variables = eval(file.readline())
            global_variables[0] = 0
            with open("lock_parameters.txt", "w") as file:
                file.write(str(global_variables))
            await ctx.send(ctx.message.author.mention + "  |  " + bot_name + " has been unlocked")
        elif str.lower(mode) == "permissions":
            if str.lower(var1) == "add":
                with open("debugpermissions.txt", "a") as file:
                    file.write(str(var2))
            elif str.lower(var1) == "remove":
                with open("debugpermissions.txt", "r") as file:
                    tempdata = file.readlines()
                with open("debugpermissions.txt", "w") as file:
                    file.write("\n")
                for value in tempdata:
                    if str(var2) not in str(value):
                        with open("debugpermissions.txt", "a") as file:
                            file.write(str(value))
                with open("users8.txt", "a") as file:
                    file.write(str(ctx.message.author.id) + "\n")
        elif str.lower(mode) == "?" or str.lower(mode) == "help":
            AddStats(str(ctx.message.author.id), stat_help)
            if str.lower(var1) == "dm":
                await ctx.send(ctx.message.author.mention + "  |  A DM has been sent to you")
                await ctx.author.send("**Debug command list**\n \n"
                                      "**.debug help dm/here**  -  Gives information on admin functions\n \n"
                                      "**.debug userids X dm/here**  -  Lists ids contained in the specified database ***X** = 9, 8, 7, or ALL*\n \n"
                                      "**.debug stats X dm/here**  -  Displays bot statistics ***X** = 9, 8, 7, or ALL*\n")

            elif str.lower(var1) == "here":
                await ctx.send(ctx.message.author.mention + "  |  **Debug command list**\n \n"
                                      "**.debug help dm/here**  -  Gives information on admin functions\n \n"
                                      "**.debug userids X dm/here**  -  Lists ids contained in specified database ***X** = 9, 8, 7, or ALL*\n \n"
                                      "**.debug stats X dm/here**  -  Displays bot statistics ***X** = 9, 8, 7, or ALL*\n")

            else:
                await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command. Use **.debug help** for info")
    else:
        AddStats(str(ctx.message.author.id), stat_invalid_admin)
        await ctx.send(ctx.message.author.mention + "  |  You do not have permission to use debug commands")


@client.command(pass_context=True)
async def tt(ctx, modeinp="11381138", inp1="11381138", inp2="11381138", inp3="11381138"):
    with open("lock_parameters.txt", "r") as file:
        global_variables = eval(file.readline())
    if global_variables[0] == 1:
        await ctx.send(ctx.message.author.mention + "  |  " + bot_name + " is currently locked" + str(global_variables[1]))
    elif global_variables[0] == 0:
        AddStats(str(ctx.message.author.id), stat_tt)
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
                AddStats(str(ctx.message.author.id), stat_tt_overview)
                if str(ctx.message.author.id) in userdata9:
                    if SetCurrentPeriod("9") == sp_NULL or SetCurrentPeriod("9") == sp_NUCL:
                        if ViewClub(Day(), str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  (G9)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nThere is nothing scheduled for your current period\nYour next sceduled period is " + SetNextPeriod("9", str(ctx.message.author.id)) + "\n \nYou don't have a club today")
                        else:
                            await ctx.send(ctx.message.author.mention + "  (G9)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nThere is nothing scheduled for your current period\nYour next sceduled period is " + SetNextPeriod("9", str(ctx.message.author.id)) + "\n \nYour club today is " + ViewClub(Day(), str(ctx.message.author.id)))
                    else:
                        if ViewClub(Day(), str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  (G9)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nYour current period is " + SetCurrentPeriod("9", str(ctx.message.author.id)) + "\nYour next sceduled period is " + SetNextPeriod("9", str(ctx.message.author.id)) + "\n \nYou don't have a club today")
                        else:
                            await ctx.send(ctx.message.author.mention + "  (G9)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nYour current period is " + SetCurrentPeriod("9", str(ctx.message.author.id)) + "\nYour next sceduled period is " + SetNextPeriod("9", str(ctx.message.author.id)) + "\n \nYour club today is " + ViewClub(Day(), str(ctx.message.author.id)))
                elif str(ctx.message.author.id) in userdata8:
                    if SetCurrentPeriod("8") == sp_NULL or SetCurrentPeriod("8") == sp_NUCL:
                        if ViewClub(Day(), str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  (G8)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nThere is nothing scheduled for your current period\nYour next sceduled period is " + SetNextPeriod("8", str(ctx.message.author.id)) + "\n \nYou don't have a club today")
                        else:
                            await ctx.send(ctx.message.author.mention + "  (G8)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nThere is nothing scheduled for your current period\nYour next sceduled period is " + SetNextPeriod("8", str(ctx.message.author.id)) + "\n \nYour club today is " + ViewClub(Day(), str(ctx.message.author.id)))
                    else:
                        if ViewClub(Day(), str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  (G8)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nYour current period is " + SetCurrentPeriod("8", str(ctx.message.author.id)) + "\nYour next sceduled period is " + SetNextPeriod("8", str(ctx.message.author.id)) + "\n \nYou don't have a club today")
                        else:
                            await ctx.send(ctx.message.author.mention + "  (G8)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nYour current period is " + SetCurrentPeriod("8", str(ctx.message.author.id)) + "\nYour next sceduled period is " + SetNextPeriod("8", str(ctx.message.author.id)) + "\n \nYour club today is " + ViewClub(Day(), str(ctx.message.author.id)))
                elif str(ctx.message.author.id) in userdata7:
                    if SetCurrentPeriod("7") == sp_NULL or SetCurrentPeriod("7") == sp_NUCL:
                        if ViewClub(Day(), str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  (G7)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nThere is nothing scheduled for your current period\nYour next sceduled period is " + SetNextPeriod("7", str(ctx.message.author.id)) + "\n \nYou don't have a club today")
                        else:
                            await ctx.send(ctx.message.author.mention + "  (G7)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nThere is nothing scheduled for your current period\nYour next sceduled period is " + SetNextPeriod("7", str(ctx.message.author.id)) + "\n \nYour club today is " + ViewClub(Day(), str(ctx.message.author.id)))
                    else:
                        if ViewClub(Day(), str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  (G7)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nYour current period is " + SetCurrentPeriod("7", str(ctx.message.author.id)) + "\nYour next sceduled period is " + SetNextPeriod("7", str(ctx.message.author.id)) + "\n \nYou don't have a club today")
                        else:
                            await ctx.send(ctx.message.author.mention + "  (G7)  |  Today is " + str(Day()) + " the " + str(Date()) + " of " + str(Month()) + " " + str(time.localtime()[0]) + ". The time is " + str(Time()) + "\n \nYour current period is " + SetCurrentPeriod("7", str(ctx.message.author.id)) + "\nYour next sceduled period is " + SetNextPeriod("7", str(ctx.message.author.id)) + "\n \nYour club today is " + ViewClub(Day(), str(ctx.message.author.id)))

            elif mode == "help" or mode == "?":
                await ctx.send(ctx.message.author.mention + "  |  **Command List:**\n \n"
                                                            "**.tt**  -  Provides key information about current and upcoming periods, etc.\n \n"
                                                            "**.tt help**  -  Gives information on bot functions\n \n"
                                                            "**.tt day *grade day***  -  Displays the timetable of the specified day\n"
                                                            "If no grade is inputted, your grade will be used. If no day is inputted, the current day will be used. Use 'x' to force the default value\n \n"
                                                            "**.tt club set *day club***  -  Allows you to set a school club on the specified day\n \n"
                                                            "**.tt club remove *day***  -  Removes you from your club on the specified day\n \n"  
                                                            "**.tt setgrade *grade***  -  Allows you to change the grade you are in if you set it incorrectly\n \n"
                                                            "**.tt report *message*** - Allows you to report an issue, bug, or suggestion about the bot directly to the owner")

            elif mode == "day":
                AddStats(str(ctx.message.author.id), stat_valid_day)
                if inp1 == "9" or (inp1 == "11381138" and str(ctx.message.author.id) in userdata9) or (str.lower(inp1) == "x" and str(ctx.message.author.id) in userdata9):
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
                        AddStats(str(ctx.message.author.id), stat_mon)
                        if ViewClub("monday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G9 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G9 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYour club on this day is " + ViewClub("monday", str(ctx.message.author.id)))
                    
                    elif str.lower(inp2) == "tue" or str.lower(inp2) == "tues" or str.lower(inp2) == "tuesday":
                        AddStats(str(ctx.message.author.id), stat_tue)
                        if ViewClub("tuesday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G9 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G9 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYour club on this day is " + ViewClub("tuesday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "wed" or str.lower(inp2) == "wednesday":
                        AddStats(str(ctx.message.author.id), stat_wed)
                        if ViewClub("wednesday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G9 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G9 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYour club on this day is " + ViewClub("Wednesday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "thu" or str.lower(inp2) == "thur" or str.lower(inp2) == "thurs" or str.lower(inp2) == "thursday":
                        AddStats(str(ctx.message.author.id), stat_thu)
                        if ViewClub("thursday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G9 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G9 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYour club on this day is " + ViewClub("thursday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "fri" or str.lower(inp2) == "friday":
                        AddStats(str(ctx.message.author.id), stat_fri)
                        if ViewClub("friday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G9 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G9 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYour club on this day is " + ViewClub("friday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "sat" or str.lower(inp2) == "saturday" or str.lower(inp2) == "sun" or str.lower(inp2) == "sunday":
                        if str.lower(inp2) == "sat" or str.lower(inp2) == "saturday":
                            AddStats(str(ctx.message.author.id), stat_sat)
                        else:
                            AddStats(str(ctx.message.author.id), stat_sun)
                        await ctx.send(ctx.message.author.mention + "  |  There is no school timetable on the weekend")
                    elif str.lower(inp2) == "x" or inp2 == "11381138":
                        if str.lower(Day()) == "monday":
                            AddStats(str(ctx.message.author.id), stat_mon)
                            if ViewClub("monday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G9 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G9 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYour club on this day is " + ViewClub("monday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "tuesday":
                            AddStats(str(ctx.message.author.id), stat_tue)
                            if ViewClub("tuesday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G9 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G9 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYour club on this day is " + ViewClub("tuesday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "wednesday":
                            AddStats(str(ctx.message.author.id), stat_wed)
                            if ViewClub("monday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G9 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G9 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYour club on this day is " + ViewClub("wednesday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "thursday":
                            AddStats(str(ctx.message.author.id), stat_thu)
                            if ViewClub("thursday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G9 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G9 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYour club on this day is " + ViewClub("thursday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "friday":
                            AddStats(str(ctx.message.author.id), stat_fri)
                            if ViewClub("friday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G9 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G9 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYour club on this day is " + ViewClub("friday", str(ctx.message.author.id)))
                    else:
                        AddStats(str(ctx.message.author.id), stat_invalid_day)
                        await ctx.send(ctx.message.author.mention + "  |  That is not the correct usage of this command. Use **.tt help** for help")
                elif inp1 == "8" or (inp1 == "11381138" and str(ctx.message.author.id) in userdata8) or (str.lower(inp1) == "x" and str(ctx.message.author.id) in userdata8):
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
                        AddStats(str(ctx.message.author.id), stat_mon)
                        if ViewClub("monday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G8 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G8 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYour club on this day is " + ViewClub("monday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "tue" or str.lower(inp2) == "tues" or str.lower(inp2) == "tuesday":
                        AddStats(str(ctx.message.author.id), stat_tue)
                        if ViewClub("tuesday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G8 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G8 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYour club on this day is " + ViewClub("tuesday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "wed" or str.lower(inp2) == "wednesday":
                        AddStats(str(ctx.message.author.id), stat_wed)
                        if ViewClub("wednesday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G8 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G8 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYour club on this day is " + ViewClub("wednesday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "thu" or str.lower(inp2) == "thur" or str.lower(inp2) == "thurs" or str.lower(inp2) == "thursday":
                        AddStats(str(ctx.message.author.id), stat_thu)
                        if ViewClub("thursday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G8 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G8 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYour club on this day is " + ViewClub("thursday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "fri" or str.lower(inp2) == "friday":
                        AddStats(str(ctx.message.author.id), stat_fri)
                        if ViewClub("monday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G8 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G8 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYour club on this day is " + ViewClub("friday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "sat" or str.lower(inp2) == "saturday" or str.lower(inp2) == "sun" or str.lower(inp2) == "sunday":
                        if str.lower(inp2) == "sat" or str.lower(inp2) == "saturday":
                            AddStats(str(ctx.message.author.id), stat_sat)
                        else:
                            AddStats(str(ctx.message.author.id), stat_sun)
                        await ctx.send(ctx.message.author.mention + "  |  There is no school timetable on the weekend")
                    elif str.lower(inp2) == "x" or inp2 == "11381138":
                        if str.lower(Day()) == "monday":
                            AddStats(str(ctx.message.author.id), stat_mon)
                            if ViewClub("monday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G8 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G8 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYour club on this day is " + ViewClub("monday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "tuesday":
                            AddStats(str(ctx.message.author.id), stat_tue)
                            if ViewClub("tuesday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G8 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G8 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYour club on this day is " + ViewClub("tuesday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "wednesday":
                            AddStats(str(ctx.message.author.id), stat_wed)
                            if ViewClub("wednesday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G8 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G8 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYour club on this day is " + ViewClub("wednesday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "thursday":
                            AddStats(str(ctx.message.author.id), stat_thu)
                            if ViewClub("thursday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G8 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G8 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYour club on this day is " + ViewClub("thursday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "friday":
                            AddStats(str(ctx.message.author.id), stat_fri)
                            if ViewClub("friday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G8 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G8 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYour club on this day is " + ViewClub("friday", str(ctx.message.author.id)))
                    else:
                        AddStats(str(ctx.message.author.id), stat_invalid_day)
                        await ctx.send(ctx.message.author.mention + "  |  That is not the correct usage of this command. Use **.tt help** for help")
                elif inp1 == "7" or (inp1 == "11381138" and str(ctx.message.author.id) in userdata7) or (str.lower(inp1) == "x" and str(ctx.message.author.id) in userdata7):
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
                        AddStats(str(ctx.message.author.id), stat_mon)
                        if ViewClub("monday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G7 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G7 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYour club on this day is " + ViewClub("monday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "tue" or str.lower(inp2) == "tues" or str.lower(inp2) == "tuesday":
                        AddStats(str(ctx.message.author.id), stat_tue)
                        if ViewClub("tuesday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G7 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G7 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYour club on this day is " + ViewClub("tuesday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "wed" or str.lower(inp2) == "wednesday":
                        AddStats(str(ctx.message.author.id), stat_wed)
                        if ViewClub("wednesday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G7 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G7 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYour club on this day is " + ViewClub("wednesday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "thu" or str.lower(inp2) == "thur" or str.lower(inp2) == "thurs" or str.lower(inp2) == "thursday":
                        AddStats(str(ctx.message.author.id), stat_thu)
                        if ViewClub("thursday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G7 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G7 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYour club on this day is " + ViewClub("thursday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "fri" or str.lower(inp2) == "friday":
                        AddStats(str(ctx.message.author.id), stat_fri)
                        if ViewClub("friday", str(ctx.message.author.id)) == "null":
                            await ctx.send(ctx.message.author.mention + "  |  The G7 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYou do not have a club on this day")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  The G7 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYour club on this day is " + ViewClub("friday", str(ctx.message.author.id)))
                    elif str.lower(inp2) == "sat" or str.lower(inp2) == "saturday" or str.lower(inp2) == "sun" or str.lower(inp2) == "sunday":
                        if str.lower(inp2) == "sat" or str.lower(inp2) == "saturday":
                            AddStats(str(ctx.message.author.id), stat_sat)
                        else:
                            AddStats(str(ctx.message.author.id), stat_sun)
                        await ctx.send(ctx.message.author.mention + "  |  There is no school timetable on the weekend")
                    elif str.lower(inp2) == "x" or inp2 == "11381138":
                        if str.lower(Day()) == "monday":
                            AddStats(str(ctx.message.author.id), stat_mon)
                            if ViewClub("monday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G7 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G7 Monday timetable is:\n \n" + str(MonTT[0]) + "\n" + str(MonTT[1]) + "\n" + str(MonTT[2]) + "\n" + str(MonTT[3]) + "\n" + str(MonTT[4]) + "\n \nYour club on this day is " + ViewClub("monday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "tuesday":
                            AddStats(str(ctx.message.author.id), stat_tue)
                            if ViewClub("tuesday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G7 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G7 Tuesday timetable is:\n \n" + str(TueTT[0]) + "\n" + str(TueTT[1]) + "\n" + str(TueTT[2]) + "\n" + str(TueTT[3]) + "\n" + str(TueTT[4]) + "\n \nYour club on this day is " + ViewClub("tuesday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "wednesday":
                            AddStats(str(ctx.message.author.id), stat_wed)
                            if ViewClub("wednesday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G7 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G7 Wednesday timetable is:\n \n" + str(WedTT[0]) + "\n" + str(WedTT[1]) + "\n" + str(WedTT[2]) + "\n" + str(WedTT[3]) + "\n \nYour club on this day is " + ViewClub("wednesday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "thursday":
                            AddStats(str(ctx.message.author.id), stat_thu)
                            if ViewClub("thursday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G7 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G7 Thursday timetable is:\n \n" + str(ThuTT[0]) + "\n" + str(ThuTT[1]) + "\n" + str(ThuTT[2]) + "\n" + str(ThuTT[3]) + "\n" + str(ThuTT[4]) + "\n \nYour club on this day is " + ViewClub("thursday", str(ctx.message.author.id)))
                        elif str.lower(Day()) == "friday":
                            AddStats(str(ctx.message.author.id), stat_fri)
                            if ViewClub("friday", str(ctx.message.author.id)) == "null":
                                await ctx.send(ctx.message.author.mention + "  |  The G7 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYou do not have a club on this day")
                            else:
                                await ctx.send(ctx.message.author.mention + "  |  The G7 Friday timetable is:\n \n" + str(FriTT[0]) + "\n" + str(FriTT[1]) + "\n" + str(FriTT[2]) + "\n" + str(FriTT[3]) + "\n" + str(FriTT[4]) + "\n \nYour club on this day is " + ViewClub("friday", str(ctx.message.author.id)))
                    else:
                        AddStats(str(ctx.message.author.id), stat_invalid_day)
                        await ctx.send(ctx.message.author.mention + "  |  That is not the correct usage of this command. Use **.tt help** for help")
            elif mode == "setgrade":
                    AddStats(str(ctx.message.author.id), stat_grade)
                    with open("users9.txt", "r") as file:
                        userdata9 = file.read()
                    with open("users8.txt", "r") as file:
                        userdata8 = file.read()
                    with open("users7.txt", "r") as file:
                        userdata7 = file.read()
                    if str(inp1) == "9":
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
                    elif str(inp1) == "8":
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
                    elif str(inp1) == "7":
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
            elif mode == "club":
                AddStats(str(ctx.message.author.id), stat_club)
                with open("club_BND_MON", "r") as file:
                    club_BND_MON = file.read()
                with open("club_LGA_MON", "r") as file:
                    club_LGA_MON = file.read()
                with open("club_TTR_MON", "r") as file:
                    club_TTR_MON = file.read()

                with open("club_TTR_TUE", "r") as file:
                    club_TTR_TUE = file.read()
                with open("club_CAL_TUE", "r") as file:
                    club_CAL_TUE = file.read()
                with open("club_CHI_TUE", "r") as file:
                    club_CHI_TUE = file.read()

                with open("club_FTY_WED", "r") as file:
                    club_FTY_WED = file.read()

                with open("club_TTR_THU", "r") as file:
                    club_TTR_THU = file.read()
                with open("club_IMP_THU", "r") as file:
                    club_IMP_THU = file.read()
                with open("club_MKC_THU", "r") as file:
                    club_MKC_THU = file.read()
                with open("club_MUS_THU", "r") as file:
                    club_MUS_THU = file.read()
                with open("club_R20_THU", "r") as file:
                    club_R20_THU = file.read()

                with open("club_TTR_FRI", "r") as file:
                    club_TTR_FRI = file.read()
                with open("club_CHI_FRI", "r") as file:
                    club_CHI_FRI = file.read()
                with open("club_IKE_FRI", "r") as file:
                    club_IKE_FRI = file.read()
                with open("club_BSK_FRI", "r") as file:
                    club_BSK_FRI = file.read()
                with open("club_MSS_FRI", "r") as file:
                    club_MSS_FRI = file.read()
                if str.lower(inp1) == "set":
                    if str.lower(inp2) == "mon" or str.lower(inp2) == "monday":
                        if str(ctx.message.author.id) in club_BND_MON or str(ctx.message.author.id) in club_LGA_MON or str(ctx.message.author.id) in club_TTR_MON:
                            await ctx.send(str(ctx.message.author.mention) + "  |  " + "You are already in a club on Monday. Remove that club first if you want to add this one")
                        elif str.lower(inp3) in id_BND:
                            with open("club_BND_MON", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                                await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Monday has been set to " + club_BND)

                        elif str.lower(inp3) in id_LGA:
                            with open("club_LGA_MON", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Monday has been set to " + club_LGA)
                        elif str.lower(inp3) in id_TTR:
                            with open("club_TTR_MON", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Monday has been set to " + club_TTR)
                        else:
                            await ctx.send(str(ctx.message.author.mention) + "  |  " + "That is not a valid club name")
                    elif str.lower(inp2) == "tue" or str.lower(inp2) == "tuesday":
                        if str(ctx.message.author.id) in club_TTR_TUE or str(ctx.message.author.id) in club_CAL_TUE or str(ctx.message.author.id) in club_CHI_TUE:
                            await ctx.send(str(ctx.message.author.mention) + "  |  " + "You are already in a club on Tuesday. Remove that club first if you want to add this one")
                        elif str.lower(inp3) in id_TTR:
                            with open("club_TTR_TUE", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Tuesday has been set to " + club_TTR)
                        elif str.lower(inp3) in id_CAL:
                            with open("club_CAL_TUE", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Tuesday has been set to " + club_CAL)
                        elif str.lower(inp3) in id_CHI:
                            with open("club_CHI_TUE", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Tuesday has been set to " + club_CHI)
                        else:
                            await ctx.send(str(ctx.message.author.mention) + "  |  " + "That is not a valid club name")
                    elif str.lower(inp2) == "wed" or str.lower(inp2) == "wednesday":
                        if str(ctx.message.author.id) in club_FTY_WED:
                            await ctx.send(str(ctx.message.author.mention) + "  |  " + "You are already in a club on Wednesday. Remove that club first if you want to add this one")
                        elif str.lower(inp3) in id_FTY:
                            with open("club_FTY_WED", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Wednesday has been set to " + club_FTY)
                        else:
                            await ctx.send(str(ctx.message.author.mention) + "  |  " + "That is not a valid club name")
                    elif str.lower(inp2) == "thu" or str.lower(inp2) == "thursday" or str.lower(inp2) == "thur" or str.lower(inp2) == "thurs":
                        if str(ctx.message.author.id) in club_TTR_THU or str(ctx.message.author.id) in club_IMP_THU or str(ctx.message.author.id) in club_MKC_THU or str(ctx.message.author.id) in club_MUS_THU or str(ctx.message.author.id) in club_R20_THU:
                            await ctx.send(str(ctx.message.author.mention) + "  |  " + "You are already in a club on Thursday. Remove that club first if you want to add this one")
                        elif str.lower(inp3) in id_TTR:
                            with open("club_TTR_THU", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Thursday has been set to " + club_TTR)
                        elif str.lower(inp3) in id_IMP:
                            with open("club_IMP_THU", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Thursday has been set to " + club_IMP)
                        elif str.lower(inp3) in id_MKC:
                            with open("club_MKC_THU", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Thursday has been set to " + club_MKC)
                        elif str.lower(inp3) in id_MUS:
                            with open("club_MUS_THU", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Thursday has been set to " + club_MUS)
                        elif str.lower(inp3) in id_R20:
                            with open("club_R20_THU", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Thursday has been set to " + club_R20)
                        else:
                            await ctx.send(str(ctx.message.author.mention) + "  |  " + "That is not a valid club name")
                    elif str.lower(inp2) == "fri" or str.lower(inp2) == "friday":
                        if str(ctx.message.author.id) in club_TTR_FRI or str(ctx.message.author.id) in club_CHI_FRI or str(ctx.message.author.id) in club_IKE_FRI or str(ctx.message.author.id) in club_BSK_FRI or str(ctx.message.author.id) in club_MSS_FRI:
                            await ctx.send(str(ctx.message.author.mention) + "  |  " + "You are already in a club on Friday. Remove that club first if you want to add this one")
                        elif str.lower(inp3) in id_TTR:
                            with open("club_TTR_FRI", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Friday has been set to " + club_TTR)
                        elif str.lower(inp3) in id_CHI:
                            with open("club_CHI_FRI", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Friday has been set to " + club_CHI)
                        elif str.lower(inp3) in id_IKE:
                            with open("club_IKE_FRI", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Friday has been set to " + club_IKE)
                        elif str.lower(inp3) in id_BSK:
                            with open("club_BSK_FRI", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Friday has been set to " + club_BSK)
                        elif str.lower(inp3) in id_MSS:
                            with open("club_MSS_FRI", "a") as file:
                                file.write(str(str(ctx.message.author.id)) + "\n")
                            await ctx.send(str(ctx.message.author.mention) + "  |  Your club on Friday has been set to " + club_MSS)
                        else:
                            await ctx.send(str(ctx.message.author.mention) + "  |  " + "That is not a valid club name")
                    else:
                        await ctx.send(str(ctx.message.author.mention) + "  |  That is not a valid day name")
                elif str.lower(inp1) == "remove":
                    with open("club_BND_MON", "r") as file:
                        club_BND_MON = file.read()
                    with open("club_LGA_MON", "r") as file:
                        club_LGA_MON = file.read()
                    with open("club_TTR_MON", "r") as file:
                        club_TTR_MON = file.read()

                    with open("club_TTR_TUE", "r") as file:
                        club_TTR_TUE = file.read()
                    with open("club_CAL_TUE", "r") as file:
                        club_CAL_TUE = file.read()
                    with open("club_CHI_TUE", "r") as file:
                        club_CHI_TUE = file.read()

                    with open("club_FTY_WED", "r") as file:
                        club_FTY_WED = file.read()

                    with open("club_TTR_THU", "r") as file:
                        club_TTR_THU = file.read()
                    with open("club_IMP_THU", "r") as file:
                        club_IMP_THU = file.read()
                    with open("club_MKC_THU", "r") as file:
                        club_MKC_THU = file.read()
                    with open("club_MUS_THU", "r") as file:
                        club_MUS_THU = file.read()
                    with open("club_R20_THU", "r") as file:
                        club_R20_THU = file.read()

                    with open("club_TTR_FRI", "r") as file:
                        club_TTR_FRI = file.read()
                    with open("club_CHI_FRI", "r") as file:
                        club_CHI_FRI = file.read()
                    with open("club_IKE_FRI", "r") as file:
                        club_IKE_FRI = file.read()
                    with open("club_BSK_FRI", "r") as file:
                        club_BSK_FRI = file.read()
                    with open("club_MSS_FRI", "r") as file:
                        club_MSS_FRI = file.read()
                    if str.lower(inp2) == "mon" or str.lower(inp2) == "monday":
                        if str(ctx.message.author.id) in club_BND_MON:
                            Remove_Club(str(ctx.message.author.id), "club_BND_MON")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_BND + " on Monday")
                        elif str(ctx.message.author.id) in club_LGA_MON:
                            Remove_Club(str(ctx.message.author.id), "club_LGA_MON")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_LGA + " on Monday")
                        elif str(ctx.message.author.id) in club_TTR_MON:
                            Remove_Club(str(ctx.message.author.id), "club_TTR_MON")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_TTR + " on Monday")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  You are not in a club on Monday")
                    elif str.lower(inp2) == "tue" or str.lower(inp2) == "tuesday":
                        if str(ctx.message.author.id) in club_CAL_TUE:
                            Remove_Club(str(ctx.message.author.id), "club_CAL_TUE")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_CAL + " on Tuesday")
                        elif str(ctx.message.author.id) in club_CHI_TUE:
                            Remove_Club(str(ctx.message.author.id), "club_CHI_TUE")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_CHI + " on Tuesday")
                        elif str(ctx.message.author.id) in club_TTR_TUE:
                            Remove_Club(str(ctx.message.author.id), "club_TTR_TUE")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_TTR + " on Tuesday")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  You are not in a club on Tuesday")
                    elif str.lower(inp2) == "wed" or str.lower(inp2) == "wednesday":
                        if str(ctx.message.author.id) in club_FTY_WED:
                            Remove_Club(str(ctx.message.author.id), "club_FTY_WED")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_FTY + " on Wednesday")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  You are not in a club on Wednesday")
                    elif str.lower(inp2) == "thu" or str.lower(inp2) == "thur" or str.lower(inp2) == "thurs" or str.lower(inp2) == "thursday":
                        if str(ctx.message.author.id) in club_IMP_THU:
                            Remove_Club(str(ctx.message.author.id), "club_IMP_THU")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_IMP + " on Thursday")
                        elif str(ctx.message.author.id) in club_MKC_THU:
                            Remove_Club(str(ctx.message.author.id), "club_MKC_THU")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_MKC + " on Thursday")
                        elif str(ctx.message.author.id) in club_MUS_THU:
                            Remove_Club(str(ctx.message.author.id), "club_MUS_THU")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_MUS + " on Thursday")
                        elif str(ctx.message.author.id) in club_R20_THU:
                            Remove_Club(str(ctx.message.author.id), "club_R20_THU")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_R20 + " on Thursday")
                        elif str(ctx.message.author.id) in club_TTR_THU:
                            Remove_Club(str(ctx.message.author.id), "club_TTR_THU")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_TTR + " on Thursday")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  You are not in a club on Thursday")
                    elif str.lower(inp2) == "fri" or str.lower(inp2) == "friday":
                        if str(ctx.message.author.id) in club_CHI_FRI:
                            Remove_Club(str(ctx.message.author.id), "club_CHI_FRI")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_CHI + " on Friday")
                        elif str(ctx.message.author.id) in club_BSK_FRI:
                            Remove_Club(str(ctx.message.author.id), "club_BSK_FRI")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_BSK + " on Friday")
                        elif str(ctx.message.author.id) in club_IKE_FRI:
                            Remove_Club(str(ctx.message.author.id), "club_IKE_FRI")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_IKE + " on Friday")
                        elif str(ctx.message.author.id) in club_MSS_FRI:
                            Remove_Club(str(ctx.message.author.id), "club_MSS_FRI")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_MSS + " on Friday")
                        elif str(ctx.message.author.id) in club_TTR_FRI:
                            Remove_Club(str(ctx.message.author.id), "club_TTR_FRI")
                            await ctx.send(ctx.message.author.mention + "  |  You have been removed from " + club_TTR + " on Friday")
                        else:
                            await ctx.send(ctx.message.author.mention + "  |  You are not in a club on Friday")
                    else:
                        await ctx.send(ctx.message.author.mention + "  |  That is not a valid day name. For information on this command, use **.tt help**")
            elif mode == "report":
                if str(inp1) == "11381138":
                    await ctx.send(ctx.message.author.mention + "  |  To send a report, please add a message explaining your report or suggestion after the command, like this:  **.tt report *please add cats***")
                else:
                    await ctx.send(ctx.message.author.mention + "  |  Your report has been sent! Thank you for the feedback")
                    with open("reports.txt", "a") as file:
                        file.write(str(inp1) + "\n")
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
                    await ctx.send(ctx.message.author.mention + "  |  You have been set as Grade " + inp1)
                    AddStats(str(ctx.message.author.id), stat_tt_registration)
                else:
                    await ctx.send(ctx.message.author.mention + "  |  Please set your grade by typing **.tt setgrade X**, where **X** is your grade number.")
            else:
                await ctx.send("Hello " + ctx.message.author.mention + ". You have not yet been registered in my database\nPlease tell me what grade you are in by typing **.tt setgrade X**, where **X** is your grade number\n*(You can always change this later if needed)*")

@client.command(pass_context=True)
async def reports(ctx, inp1="11381138"):
    if str(ctx.message.author.id) == bot_owner_id:
        if str.lower(inp1) == "show":
            with open("reports.txt", "r") as file:
                reports = file.read()
            await ctx.author.send(str(reports))
        elif str.lower(inp1) == "delete":
            with open("reports.txt", "w") as file:
                file.write("\n")


client.run("NjI3MDk5ODk3MjIwNDMxODcy.XY3v5Q.Q19bNJrTqvFa1eDTPEmfJjvd4HE")
