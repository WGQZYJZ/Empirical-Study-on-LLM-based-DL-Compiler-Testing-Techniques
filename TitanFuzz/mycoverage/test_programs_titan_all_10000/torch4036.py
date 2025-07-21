import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(5, 3)
y = torch.Tensor.multiply_(x, 10)