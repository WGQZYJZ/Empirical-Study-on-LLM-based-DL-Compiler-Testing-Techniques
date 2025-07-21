'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
import time
x = torch.randn(1000000, dtype=torch.float32)
y = torch.randn(1000000, dtype=torch.float32)
torch.set_num_threads(8)
t1 = time.time()
z = torch.add(x, y)
t2 = time.time()
print((t2 - t1))