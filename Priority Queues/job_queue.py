# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        self.job_heap = []
        for worker in range(0, self.num_workers):
            self.job_heap.append([worker, 0])

        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)

        for i in range(len(self.jobs)):
        # for job_time in self.jobs:
            min_node = self.get_min()
            min_worker_index = min_node[0]
            previous_work_time = min_node[1]

            self.assigned_workers[i] = min_worker_index
            self.start_times[i] = previous_work_time

            new_work_time = previous_work_time + self.jobs[i]

            self.change_priority(0, new_work_time)


        # TODO: replace this code with a faster algorithm.
        # next_free_time = [0] * self.num_workers
        # for i in range(len(self.jobs)):
        #     next_worker = 0
        #     for j in range(self.num_workers):
        #         if next_free_time[j] < next_free_time[next_worker]:
        #             next_worker = j
        #     self.assigned_workers[i] = next_worker
        #     self.start_times[i] = next_free_time[next_worker]
        #     next_free_time[next_worker] += self.jobs[i]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

    def parent(self, i):
        return (i-1)//2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def sift_up(self, i):
        while i > 0 and ( (self.job_heap[self.parent(i)][1] > self.job_heap[i][1]) or (self.job_heap[self.parent(i)][0] > self.job_heap[i][0]) ):
            self.job_heap[i], self.job_heap[self.parent(i)] = self.job_heap[self.parent(i)], self.job_heap[i]
            i = self.parent(i)

    def sift_down(self, i):
        min_index = i

        left_index = self.left_child(i)
        if left_index < len(self.job_heap):
            if self.job_heap[min_index][1] > self.job_heap[left_index][1]:
                min_index = left_index
            elif self.job_heap[min_index][1] == self.job_heap[left_index][1] and self.job_heap[min_index][0] > self.job_heap[left_index][0]:
                min_index = left_index

        right_index = self.right_child(i)
        if right_index < len(self.job_heap):
            if self.job_heap[min_index][1] > self.job_heap[right_index][1]:
                min_index = right_index
            elif self.job_heap[min_index][1] == self.job_heap[right_index][1] and self.job_heap[min_index][0] > self.job_heap[right_index][0]:
                min_index = right_index

        if i != min_index:
            self.job_heap[i], self.job_heap[min_index] = self.job_heap[min_index], self.job_heap[i]
            self.sift_down(min_index)

    def get_min(self):
        result = self.job_heap[0]
        return result

    def change_priority(self, i, p):
        old_priority = self.job_heap[i][1]
        self.job_heap[i][1] = p
        if p > old_priority:
            self.sift_down(i)
        else:
            self.sift_up(i)


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

