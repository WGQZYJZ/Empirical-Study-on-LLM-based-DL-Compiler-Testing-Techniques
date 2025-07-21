import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.positive(input_tensor)
input_tensor = torch.randn(3, 3)
exponent = torch.randn(3, 3)
output_tensor = torch.Tensor.pow(input_tensor, exponent)