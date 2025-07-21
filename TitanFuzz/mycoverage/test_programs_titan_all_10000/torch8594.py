import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(10, 3, 4)
y = torch.randn(10, 4, 5)
z = torch.bmm(x, y)