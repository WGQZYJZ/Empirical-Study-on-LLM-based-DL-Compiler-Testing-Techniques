import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
exponent = 1.5
output_tensor = torch.Tensor.float_power(input_tensor, exponent)