import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 10, dtype=torch.float32).reshape(3, 3)
y = torch.narrow(x, dim=0, start=0, length=2)
y = torch.narrow(x, dim=0, start=1, length=2)
y = torch.narrow(x, dim=1, start=0, length=2)
y = torch.narrow(x, dim=1, start=1, length=2)