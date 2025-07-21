'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.wait\ntorch.jit.wait(future)\n'
import torch
import time
import torch
x = torch.ones(2, 2)
y = torch.ones(2, 2)
future = torch.jit._fork(torch.add, x, y)
torch.jit.wait(future)
print(future.value())
x = torch.ones(2, 2)
y = torch.ones(2, 2)
future = torch.jit._fork(torch.add, x, y)
torch.jit.wait(future)
print(future.value())