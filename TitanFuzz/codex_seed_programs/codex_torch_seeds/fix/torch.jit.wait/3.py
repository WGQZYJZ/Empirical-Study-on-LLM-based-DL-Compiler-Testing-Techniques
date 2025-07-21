'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.wait\ntorch.jit.wait(future)\n'
import torch
import time
import torch
x = torch.zeros(1)
future = torch.jit._fork(torch.add, x, 1)
torch.jit.wait(future)
print(future.value())
print(time.time())