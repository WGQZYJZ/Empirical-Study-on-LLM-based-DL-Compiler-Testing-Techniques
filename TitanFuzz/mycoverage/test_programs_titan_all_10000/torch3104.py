import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
exponent = 2.0
output_tensor = torch.Tensor.float_power_(input_tensor, exponent)
input_tensor = torch.randn(3, 3)
exponent = 2.0
output_tensor = input_tensor.float_power_(exponent)