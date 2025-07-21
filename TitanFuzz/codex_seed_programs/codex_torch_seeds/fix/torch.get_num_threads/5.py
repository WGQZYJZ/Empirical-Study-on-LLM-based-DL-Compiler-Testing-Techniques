'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_num_threads\ntorch.get_num_threads()\n'
import torch
import time
N = 100000
print('Number of threads: ', torch.get_num_threads())
torch.set_num_threads(1)
print('Number of threads: ', torch.get_num_threads())
A = torch.ones(N, dtype=torch.float32)
B = torch.ones(N, dtype=torch.float32)
start = time.time()
C = torch.add(A, B)
end = time.time()
print('Time taken to add two tensors: ', (end - start))
start = time.time()
D = torch.multiply(A, B)
end = time.time()