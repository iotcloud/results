def average(file_name, upperbound):
    avg_of_numbers = 0
    with open(file_name, "r") as in_f:
        numbers = []
        for line in in_f:
            line = line.strip().split(',')[0] # remove whitespace
            if line: # make sure there is something there
                number_on_line = long(line)
                # if number_on_line < upperbound:
                numbers.append(number_on_line)


        if len(numbers) > 0:
            sum_of_numbers = sum(numbers)
            avg_of_numbers = (sum(numbers) + 0.0)/len(numbers)

    with open(file_name, "r") as in_f:
        numbers = []
        for line in in_f:
            line = line.strip().split(',')[0] # remove whitespace
            if line: # make sure there is something there
                number_on_line = long(line)
                # if number_on_line < upperbound and number_on_line < avg_of_numbers * 2:
                if number_on_line < avg_of_numbers * 2:
                    numbers.append(number_on_line)

        if len(numbers) > 0:
            sum_of_numbers = sum(numbers)
            avg_of_numbers = (sum(numbers) + 0.0)/(len(numbers) * 1000* 1000)

    return avg_of_numbers

def minmaxaverage(file_name):
    avg_of_numbers = 0
    min_of_numbers = 0
    max_of_numbers = 0
    with open(file_name, "r") as in_f:
        numbers = []
        maxes = []
        minx = []
        for line in in_f:
            minL = 1000000000
            maxL = -10000000000
            line = line.strip().split(',') # remove whitespace
            lineSum = 0
            for i in range(1, len(line)): # make sure there is something there
                if line[i]:
                    number_on_line = long(line[i].strip())
                    if number_on_line < minL and number_on_line != 0:
                        minL = number_on_line
                    if number_on_line > maxL:
                        maxL = number_on_line

                    lineSum += number_on_line
                # if number_on_line < upperbound:
            numbers.append(lineSum * 1.0 / (len(line) - 1))
            maxes.append(maxL)
            minx.append(minL)

        if len(numbers) > 0:
            sum_of_numbers = sum(numbers)
            avg_of_numbers = (sum(numbers) * .001 + 0.0)/len(numbers)
            min_of_numbers = (sum(minx) * .001 + 0.0)/len(minx)
            max_of_numbers = (sum(maxes) * .001 + 0.0)/len(maxes)

    return avg_of_numbers, min_of_numbers, max_of_numbers

def slam():
    part = [64, 128]
    tasks = [8, 16, 32, 64]
    print 'Original'
    for p in part:
        s = str(p)
        for t in tasks:
            best = "jstorm/tempest_original/const/" + str(p) + "_" + str(t) + "_2_best"
            #print best
            s = s + " " + str(average(best, 1000))
        print s
    print 'Original_OCT_25'
    for p in part:
        s = str(p)
        for t in tasks:
            best = "jstorm/tempest_original_OCT_25/const/" + str(p) + "_" + str(t) + "_2_best"
            #print best
            s = s + " " + str(average(best, 1000))
        print s
    print 'Flat2'
    for p in part:
        s = str(p)
        for t in tasks:
            best = "jstorm/tempest_flat2/const/" + str(p) + "_" + str(t) + "_2_best"
            #print best
            s = s + " " + str(average(best, 1000))
        print s
    print 'binary_OCT_23'
    for p in part:
        s = str(p)
        for t in tasks:
            best = "jstorm/tempest_binary_OCT_23/const/" + str(p) + "_" + str(t) + "_2_best"
            #print best
            s = s + " " + str(average(best, 1000))
        print s
    print 'binary_OCT_24b'
    for p in part:
        s = str(p)
        for t in tasks:
            best = "jstorm/tempest_binary_OCT_24/const/" + str(p) + "_" + str(t) + "_2_best"
            #print best
            s = s + " " + str(average(best, 1000))
        print s

def mma():
    tasks = [10, 20, 30, 40, 50, 60]
    data = [100, 10000, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]

    print 'jstorm_bcast_original30x8x4_DEC_04'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(minmaxaverage("jstorm/jstorm_bcast_original30x8x4_DEC_04/" + str(d)  + "_" + str(t)))
        print s
    print 'jstorm_bcast_binary30x8x4_DEC_05'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(minmaxaverage("jstorm/jstorm_bcast_binary30x8x4_DEC_05/" + str(d)  + "_" + str(t)))
        print s
    print 'jstorm_bcast_pipesplit30x8x4_DEC_05'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(minmaxaverage("jstorm/jstorm_bcast_pipesplit30x8x4_DEC_05/" + str(d)  + "_" + str(t)))
        print s
    print 'jstorm_bcast_flat30x8x4_DEC_05'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(minmaxaverage("jstorm/jstorm_bcast_flat30x8x4_DEC_05/" + str(d)  + "_" + str(t)))
        print s

def large():
    tasks = [10, 20, 30, 40, 50, 60]
    data = [200000, 400000, 600000, 800000, 1000000]
    print 'jstorm_bcast_intra_large_binary30x8x4_DEC_05'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_intra_large_binary30x8x4_DEC_05/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'jstorm_bcast_intra_large_flat30x8x4_DEC_05'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_intra_large_flat30x8x4_DEC_05/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'jstorm_bcast_intra_large_pipesplit30x8x4_DEC_05'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_intra_large_pipesplit30x8x4_DEC_05/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'jstorm_bcast_large30x8x4_DEC_05'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_large30x8x4_DEC_05/" + str(d)  + "_" + str(t), 1000))
        print s

def main():
    large()

    tasks = [10, 20, 30, 40, 50, 60]
    data = [100, 10000, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]
    # print 'Original'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_original_OCT_07/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'async binary'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_async_binary8x4_OCT_13/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'async flat'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_async_flat8x4_OCT_13/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'async pipe'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_async_pipe8x4_OCT_13/" + str(d)  + "_" + str(t), 1000))
    #     print s
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
    # print 'pipe'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_pipe8x4_OCT_13/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'binary_)CT_19'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_binary8x4_OCT_19/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'binary_mapped_30x8x4_NOV_01'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_mapped_binary_30x8x4_NOV_01/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'jstorm_bcast_async_binary4x8_NOV_28'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_async_binary4x8_NOV_28/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'binary_mapped_30x8x4_NOV_28'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_intra_async_binary8x4_NOV_28/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'binary_mapped_30x4x8_NOV_28'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_intra_async_binary4x8_NOV_28/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'binary_mapped_30x4x8_NOV_29'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_intra_async_binary4x8_NOV_29/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'binary_mapped_30x4x8_DEC_01'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_intra_async_binary4x8_DEC_01/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'binary_mapped_30x1x8_NOV_30'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_intra_async_binary1x8_NOV_30/" + str(d)  + "_" + str(t), 1000))
    #     print s
    # print 'binary_async_30x1x8_NOV_30'
    # for d in data:
    #     s = str(d)
    #     for t in tasks:
    #         s = s + " " + str(average("jstorm/jstorm_bcast_async_binary1x8_NOV_30/" + str(d)  + "_" + str(t), 1000))
    #     print s
    print 'jstorm_bcast_original30x8x4_DEC_04'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_original30x8x4_DEC_04/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'jstorm_bcast_pipe30x8x4_DEC_03'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_pipe30x8x4_DEC_03/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'jstorm_bcast_intra_pipe30x8x4_DEC_03'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_intra_pipe30x8x4_DEC_03/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'jstorm_bcast_intra_pipesplit30x8x4_DEC_03'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_intra_pipesplit30x8x4_DEC_03/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'jstorm_bcast_intra_binary30x8x4_DEC_04'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_intra_binary30x8x4_DEC_04/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'jstorm_bcast_intra_flat30x8x4_DEC_05'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_intra_flat30x8x4_DEC_05/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'jstorm_bcast_binary30x8x4_DEC_05'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_binary30x8x4_DEC_05/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'jstorm_bcast_flat30x8x4_DEC_05'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_intra_flat30x8x4_DEC_04/" + str(d)  + "_" + str(t), 1000))
        print s
    print 'jstorm_bcast_pipesplit30x8x4_DEC_05'
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/jstorm_bcast_pipesplit30x8x4_DEC_05/" + str(d)  + "_" + str(t), 1000))
        print s
if __name__ == "__main__":
    # main()
    mma()
