import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(0, 10, 0.1)
x = torch.arange(0, 10)
x = torch.arange(10)
x = torch.arange(start=0, end=10, step=2)
x = torch.arange(start=0, end=10, step=2, dtype=torch.float)
x = torch.arange(start=0, end=10, step=2, dtype=torch.float, layout=torch.strided)