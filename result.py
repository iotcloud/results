def average(file_name, upperbound):
    with open(file_name, "r") as in_f:
        numbers = []
        for line in in_f:
            line = line.strip() # remove whitespace
            if line: # make sure there is something there
                number_on_line = int(line)
                if number_on_line < upperbound:
                    numbers.append(number_on_line)

        avg_of_numbers = 0
        if len(numbers) > 0:
            sum_of_numbers = sum(numbers)
            avg_of_numbers = sum(numbers)/len(numbers)

    return avg_of_numbers

def main():
    # tasks = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    tasks = [10, 20, 30, 40, 50, 60]
    data = [10000, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000]
    # data = [100, 1000, 10000, 20000, 30000]
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("/home/supun/dev/projects/iotrobots/collectives/jstorm_original_OCT_05/" + str(d)  + "_" + str(t), 1000))
        print s

    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("/home/supun/dev/projects/iotrobots/collectives/jstorm_bcast_SEP_10_binary/" + str(d)  + "_" + str(t), 50))
    #     print s
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("/home/supun/dev/projects/iotrobots/collectives/jstorm_bcast_SEP_10_binary_logs/" + str(d)  + "_" + str(t), 50))
    #     print s
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("/home/supun/dev/projects/iotrobots/collectives/jstorm_bcast_OCT_06/" + str(d)  + "_" + str(t), 1000))
        print s

    # for d in data:
    #     s = str(d) + ": "
    #     for t in tasks:
    #         s = s + " " + str(average("/home/supun/dev/projects/iotrobots/collectives/bcast/" + str(d)  + "_" + str(t), 60))
    #     print s

if __name__ == "__main__":
    main()
