def main():
    time = input("What time is it? ")
    if convert(time) >= 7 and convert(time) <= 8:
        print("breakfast time")
    elif convert(time) >= 12 and convert(time) <= 13:
        print("lunch time")
    if convert(time) >= 18 and convert(time) <= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    hour = 60
    minutes_to_hours = minutes / hour
    total_hours = hours + minutes_to_hours
    return float(total_hours)



if __name__ == "__main__":
    main()
