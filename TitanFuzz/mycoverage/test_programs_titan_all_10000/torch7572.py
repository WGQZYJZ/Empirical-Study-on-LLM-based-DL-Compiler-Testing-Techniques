import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
y = torch.randn(2, 3)
z = torch.multiply(x, y)
z = torch.mul(x, y)