import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
shrinked_data = torch.Tensor.hardshrink(input_data, lambd=0.5)