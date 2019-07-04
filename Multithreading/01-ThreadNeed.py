def job_1():
    print("Job_1 Started")
    for i in range(100000):
        for j in range(10000):
            k = i + j
    print("Completed {} iterations".format(k))
    print("Job_1 Completed")

def job_2():
    print("Job_2 Started")
    for i in range(1000):
        for j in range(100):
            k = i + j
    print("Completed {} iterations".format(k))
    print("Job_2 Completed")

job_1()
job_2()