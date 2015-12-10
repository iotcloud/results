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
            avg_of_numbers = (sum(numbers) + 0.0)/(len(numbers) )

    with open(file_name, "r") as in_f:
        numbers = []
        for line in in_f:
            line = line.strip().split(',')[0] # remove whitespace
            if line: # make sure there is something there
                number_on_line = long(line)
                # if number_on_line < upperbound and number_on_line < avg_of_numbers * 2:
                if number_on_line < avg_of_numbers * 10:
                    numbers.append(number_on_line)

        if len(numbers) > 0:
            sum_of_numbers = sum(numbers)
            avg_of_numbers = (sum(numbers) + 0.0)/(len(numbers))

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
            avg_of_numbers = (sum(numbers)+ 0.0)/len(numbers)
            min_of_numbers = (sum(minx)  + 0.0)/len(minx)
            max_of_numbers = (sum(maxes) + 0.0)/len(maxes)

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
    printmma(data, tasks, 'jstorm_bcast_original30x8x4_DEC_04')
    printmma(data, tasks, 'jstorm_bcast_binary30x8x4_DEC_05')
    printmma(data, tasks, 'jstorm_bcast_pipesplit30x8x4_DEC_05')
    printmma(data, tasks, 'jstorm_bcast_flat30x8x4_DEC_05')

def printmma(data, tasks, fileName):
    print fileName
    minS = ""
    maxS = ""
    avS = ""
    for d in data:
        minS += str(d)
        maxS += str(d)
        avS += str(d)
        for t in tasks:
            mm = minmaxaverage("jstorm/" + fileName + "/" + str(d) + "_" + str(t))
            avS = avS + " " + str(mm[0])
            minS = minS + " " + str(mm[1])
            maxS = maxS + " " + str(mm[2])
        avS += "\n"
        minS += "\n"
        maxS += "\n"
    print "ave"
    print avS
    print "min"
    print minS
    print "max"
    print maxS

def mma2():
    tasks = [10, 20, 30, 40, 50, 60]
    data = [100, 10000, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]

    printmma(data, tasks, 'jstorm_bcast_binary30x8x4_DEC_08')
    printmma(data, tasks, 'jstorm_bcast_pipesplit30x8x4_DEC_08')
    printmma(data, tasks, 'jstorm_bcast_flat30x8x4_DEC_08')

def printAverage(tasks, data, fileName):
    print fileName
    for d in data:
        s = str(d)
        for t in tasks:
            s = s + " " + str(average("jstorm/" + fileName + "/" + str(d)  + "_" + str(t), 1000))
        print s

def large():
    tasks = [10, 20, 30, 40, 50, 60]
    data = [200000, 400000, 600000, 800000, 1000000]
    printAverage(tasks, data, 'jstorm_bcast_intra_large_binary30x8x4_DEC_05')
    printAverage(tasks, data, 'jstorm_bcast_intra_large_flat30x8x4_DEC_05')
    printAverage(tasks, data, 'jstorm_bcast_intra_large_pipesplit30x8x4_DEC_05')
    printAverage(tasks, data, 'jstorm_bcast_large_binary30x8x4_DEC_05')
    printAverage(tasks, data, 'jstorm_bcast_large_flat30x8x4_DEC_05')
    printAverage(tasks, data, 'jstorm_bcast_large_pipesplit30x8x4_DEC_05')
    printAverage(tasks, data, 'jstorm_bcast_large30x8x4_DEC_05')


def normal():
    tasks = [10, 20, 30, 40, 50, 60]
    data = [100, 10000, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]
    printAverage(tasks, data, 'jstorm_bcast_original30x8x4_DEC_04')
    printAverage(tasks, data, 'jstorm_bcast_original30x8x4_DEC_05')
    printAverage(tasks, data, 'jstorm_bcast_pipe30x8x4_DEC_03')
    printAverage(tasks, data, 'jstorm_bcast_intra_pipe30x8x4_DEC_03')
    printAverage(tasks, data, 'jstorm_bcast_intra_pipesplit30x8x4_DEC_03')
    printAverage(tasks, data, 'jstorm_bcast_intra_binary30x8x4_DEC_04')
    printAverage(tasks, data, 'jstorm_bcast_intra_flat30x8x4_DEC_05')
    printAverage(tasks, data, 'jstorm_bcast_binary30x8x4_DEC_05')
    printAverage(tasks, data, 'jstorm_bcast_flat30x8x4_DEC_05')
    printAverage(tasks, data, 'jstorm_bcast_pipesplit30x8x4_DEC_05')

def normal2():
    tasks = [10, 20, 30, 40, 50, 60]
    data = [100, 10000, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]
    printAverage(tasks, data, 'jstorm_bcast_original30x8x4_DEC_08')
    printAverage(tasks, data, 'jstorm_bcast_pipe30x8x4_DEC_08')
    printAverage(tasks, data, 'jstorm_bcast_intra_pipe30x8x4_DEC_08')
    printAverage(tasks, data, 'jstorm_bcast_intra_pipesplit30x8x4_DEC_08')
    printAverage(tasks, data, 'jstorm_bcast_intra_binary30x8x4_DEC_08')
    printAverage(tasks, data, 'jstorm_bcast_intra_flat30x8x4_DEC_08')
    printAverage(tasks, data, 'jstorm_bcast_binary30x8x4_DEC_08')
    printAverage(tasks, data, 'jstorm_bcast_flat30x8x4_DEC_08')
    printAverage(tasks, data, 'jstorm_bcast_pipesplit30x8x4_DEC_08')


def calcHist():
    histogram(10, 'jstorm_bcast_intra_binary30x8x4_DEC_08', 60, 200000)
    histogram(10, 'jstorm_bcast_intra_flat30x8x4_DEC_08', 60, 200000)
    histogram(10, 'jstorm_bcast_intra_pipesplit30x8x4_DEC_08', 60, 200000)

    histogram(10, 'jstorm_bcast_intra_binary30x8x4_DEC_08', 30, 200000)
    histogram(10, 'jstorm_bcast_intra_flat30x8x4_DEC_08', 30, 200000)
    histogram(10, 'jstorm_bcast_intra_pipesplit30x8x4_DEC_08', 30, 200000)

def histogram(binNo, directory, task, data):
    avg_of_numbers = 0
    min_of_numbers = 0
    max_of_numbers = 0
    fileName = "jstorm/" + directory + "/" + str(data)  + "_" + str(task)
    with open(fileName, "r") as in_f:
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
            avg_of_numbers = (sum(numbers) * .000001+ 0.0)/len(numbers)
            min_of_numbers = (sum(minx) * .000001 + 0.0)/len(minx)
            max_of_numbers = (sum(maxes) * .000001 + 0.0)/len(maxes)
    bins = []
    delta = (max_of_numbers - min_of_numbers) / binNo
    for i in range(0, binNo):
        if (i < binNo - 1):
            bin = {"end": (min_of_numbers + delta * i), "count": 0}
        else:
            bin = {"end": 1000000000000, "count": 0}
        bins.append(bin)

    with open(fileName, "r") as in_f:
        for line in in_f:
            line = line.strip().split(',') # remove whitespace
            for i in range(1, len(line)): # make sure there is something there
                if line[i]:
                    number_on_line = long(line[i].strip()) * .000001
                    for k in range(0, binNo):
                        bin = bins[k]
                        if (number_on_line < bin["end"]):
                            bin["count"] += 1
                            break
    print bins

def main():
    pass

if __name__ == "__main__":
    calcHist()
    #normal2()
    # large()
    #mma2()
