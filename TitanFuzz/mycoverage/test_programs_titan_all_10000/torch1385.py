import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 2)
y = torch.randn(3, 2)
z = torch.Tensor.greater_equal_(x, y)