def measure_string(myStr):
    if myStr == "":
        return 0
    else:
        return measure_string(myStr[:-1]) + 1
print(measure_string("13 characters"))

