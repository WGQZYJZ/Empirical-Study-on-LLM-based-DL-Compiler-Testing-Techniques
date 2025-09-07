import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(1, 3)
y = torch.square(x)
y = torch.sqrt(x)
y = torch.rsqrt(x)
y = torch.pow(x, 2)
y = torch.exp(x)