'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
import time
torch.set_num_interop_threads(1)
a = torch.rand(1000, 1000)
b = torch.rand(1000, 1000)
start_time = time.time()
for i in range(100):
    c = torch.matmul(a, b)
print('Time taken to multiply 2 matrices with 1 thread: ', (time.time() - start_time))
torch.set_num_interop_threads(2)
a = torch.rand(1000, 1000)
b = torch.rand(1000, 1000)
start_time = time.time()
for i in range(100):
    c = torch.matmul(a, b)
print('Time taken to multiply 2 matrices with 2 threads: ', (time.time() - start_time))