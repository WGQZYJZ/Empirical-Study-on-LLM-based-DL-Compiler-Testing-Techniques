import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4, 5)
exponent = torch.randn(1)
result = torch.Tensor.float_power(input_tensor, exponent)