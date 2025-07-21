import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(100)
y = torch.randn(100)
z = torch.remainder(x, y)