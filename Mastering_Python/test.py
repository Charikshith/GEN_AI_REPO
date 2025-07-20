from multiprocessing import Process, Queue

def insert_value(queue: Queue, i: int) -> None:
    queue.put(i)
    print(f"Inserted {i} into the queue.")

def main() -> None:
    q = Queue()
    processes = [Process(target=insert_value, args=(q, i)) for i in range(5)]
    
    # Start all processes
    for process in processes:
        process.start()
    
    # Wait for all processes to complete
    for process in processes:
        process.join()
    
    # Retrieve results from the queue
    results = [q.get() for _ in processes]
    print("Results:", results)

if __name__ == "__main__":
    main()