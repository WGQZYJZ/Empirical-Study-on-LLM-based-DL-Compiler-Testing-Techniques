'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
import time
torch.set_num_interop_threads(4)
a = torch.rand(1000000, 1)
b = torch.rand(1000000, 1)
start = time.time()
c = torch.add(a, b)
print('time elapsed: {}'.format((time.time() - start)))