'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
import time
a = torch.rand(10000, 10000)
b = torch.rand(10000, 10000)
torch.set_num_threads(8)
start = time.time()
c = torch.matmul(a, b)
end = time.time()
print('Time taken for matrix multiplication: {}'.format((end - start)))