'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
import time
N = 1000000
x = torch.rand(N)
y = torch.rand(N)
torch.set_num_threads(1)
start = time.time()
z = torch.dot(x, y)
end = time.time()
print('Time elapsed: {}'.format((end - start)))