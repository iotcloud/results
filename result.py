def average(file_name, upperbound):
    with open(file_name, "r") as in_f:
        numbers = []
        for line in in_f:
            line = line.strip().split(',')[0] # remove whitespace
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
    tasks = [10, 20, 30, 40, 50, 60]
    data = [10000, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]
    print 'Original'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_original_OCT_07/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'async binary'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_async_binary8x4_OCT_13/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'async flat'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_async_flat8x4_OCT_13/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'async pipe'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_async_pipe8x4_OCT_13/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'binary'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_binary8x4_OCT_13/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'flat'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_flat8x4_OCT_13/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'pipe'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_pipe8x4_OCT_13/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'binary_)CT_19'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_binary8x4_OCT_19/" + str(d)  + "_" + str(t), 1000))
        print s
if __name__ == "__main__":
    main()
