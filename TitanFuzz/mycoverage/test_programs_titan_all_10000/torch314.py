import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(100)
hist = torch.Tensor.histogram(input, bins=10)