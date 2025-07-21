'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.fork\ntorch.jit.fork(func, *args, **kwargs)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
x = torch.rand(3, 3)
y = torch.rand(3, 3)
z = torch.rand(3, 3)
torch.jit.fork(torch.add, x, y, out=z)
print(z)
torch.jit.fork(torch.add, x, y, out=z)
print(z)
torch.jit.fork(torch.add, x, y, out=z)
print(z)
torch.jit.fork(torch.add, x, y, out=z)
print(z)