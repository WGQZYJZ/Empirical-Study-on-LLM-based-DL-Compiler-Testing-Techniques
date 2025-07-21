import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
input_tensor = torch.randn(2, 3)
output = torch.Tensor.hardshrink(input_tensor, lambd=0.5)