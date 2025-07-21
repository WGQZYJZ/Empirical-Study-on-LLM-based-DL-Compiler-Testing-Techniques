import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.Tensor.subtract_(x, y)
z = torch.Tensor.subtract_(x, y, alpha=2)
z = torch.Tensor.subtract_(x, y, alpha=3)