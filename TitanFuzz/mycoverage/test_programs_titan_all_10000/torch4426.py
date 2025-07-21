import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 2, 3, requires_grad=True)
y = torch.abs(x)
x = torch.randn(1, 2, 3, requires_grad=True)
y = torch.acos(x)
x = torch.randn(1, 2, 3, requires_grad=True)
y = torch.add(x, x)