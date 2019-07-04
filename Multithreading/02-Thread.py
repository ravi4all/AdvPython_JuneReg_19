import threading

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

t1 = threading.Thread(target=job_1)
t2 = threading.Thread(target=job_2)

t1.start()
t2.start()
