import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(100)
histogram = torch.Tensor.histogram(input, bins=10)