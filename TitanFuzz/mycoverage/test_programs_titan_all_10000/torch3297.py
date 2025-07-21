import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, 4)
y = torch.flip(x, dims=[0])
y = torch.flip(x, dims=[1])
y = torch.flip(x, dims=[0, 1])
y = torch.flip(x, dims=[0, 2])