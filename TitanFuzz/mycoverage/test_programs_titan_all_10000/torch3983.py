import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 3, 3)
output_tensor = torch.Tensor.hardshrink(input_tensor, lambd=0.5)