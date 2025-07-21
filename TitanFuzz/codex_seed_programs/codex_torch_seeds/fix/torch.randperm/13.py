'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randperm\ntorch.randperm(n, *, generator=None, out=None, dtype=torch.int64, layout=torch.strided, device=None, requires_grad=False, pin_memory=False)\n'
import torch
from torch.autograd import Variable
import torch
x = torch.rand(5, 3)
print(x)
y = torch.randperm(5)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros\ntorch.zeros(size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
from torch.autograd import Variable
import torch
x = torch.rand(5, 3)
print(x)
y = torch.zeros(5, 3)
print(y)