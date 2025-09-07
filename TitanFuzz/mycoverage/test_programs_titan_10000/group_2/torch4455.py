import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.randn(3, requires_grad=True)
a = torch.Tensor.cross(x, y, dim=0)
b = torch.Tensor.cross(x, y, dim=1)