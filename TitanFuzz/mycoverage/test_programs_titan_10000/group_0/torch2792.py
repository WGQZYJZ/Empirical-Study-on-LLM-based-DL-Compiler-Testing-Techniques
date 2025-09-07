import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(3, 4)
y = torch.normal(0, 1, (3, 4))
z = torch.normal(0, 1, (3, 4), out=x)