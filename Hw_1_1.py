import queue
import time
from datetime import datetime, timedelta 
import random

request_queue = queue.Queue()

processed_requests = 0

def generate_request():
    request_id = processed_requests + 1
    creation_time = datetime.now()
    request_queue.put((request_id, creation_time))
    print(f"Заявка {request_id} створена ({creation_time.strftime('%Y-%m-%d %H:%M:%S')}).")

def process_request():
    global processed_requests
    if not request_queue.empty():
        request_id, creation_time = request_queue.get()
        execution_time = creation_time + timedelta(minutes=random.uniform(0, 2))
        print(f"Заявка {request_id} обробляється ({execution_time.strftime('%Y-%m-%d %H:%M:%S')}).")
        processed_requests += 1
        completion_time = datetime.now()
        print(f"Заявка {request_id} виконана ({completion_time.strftime('%Y-%m-%d %H:%M:%S')}).")
    else:
        print("Черга порожня. Заявок на обробку немає.")

while processed_requests < 5:
    generate_request()
    process_request()
    time.sleep(1)

print("Всі заявки прийняті та виконані.")