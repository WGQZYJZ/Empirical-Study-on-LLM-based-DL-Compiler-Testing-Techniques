import torch
from torch import nn
from torch.autograd import Variable
x = torch.linspace(start=0, end=10, steps=5)
y = torch.linspace(start=(- 10), end=10, steps=5)
z = torch.linspace(start=0, end=1, steps=5)
a = torch.linspace(start=0, end=1, steps=5, dtype=torch.int32)
b = torch.linspace(start=0, end=1, steps=5, dtype=torch.int32, layout=torch.strided)
c = torch.linspace(start=0, end=1, steps=5, dtype=torch.int32, layout=torch.strided, device='cpu')