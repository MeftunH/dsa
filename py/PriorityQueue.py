import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        heapq.heappush(self.queue, item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return heapq.heappop(self.queue)

    # Display the queue
    def display(self):
        return self.queue