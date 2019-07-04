import threading
def job():
    thread_name = threading.current_thread().getName()
    print("Thread {} entered".format(thread_name))

    for i in range(10000):
        for j in range(1000):
            k = i + j
    thread_name = threading.current_thread().getName()
    print("Thread {} exits".format(thread_name))

for i in range(5):
    t = threading.Thread(target=job)
    t.start()