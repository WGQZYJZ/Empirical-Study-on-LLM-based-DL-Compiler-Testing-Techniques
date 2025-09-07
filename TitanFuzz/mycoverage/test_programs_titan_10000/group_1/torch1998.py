import torch
from torch import nn
from torch.autograd import Variable

x = torch.arange(0, 10, 0.1)
y = torch.sin(x)
result = torch.trapz(y, dx=0.1)