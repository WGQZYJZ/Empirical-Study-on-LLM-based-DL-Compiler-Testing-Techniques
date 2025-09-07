import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.less(x, y)
x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.less_equal(x, y)
x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.greater(x, y)