import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
exponent = torch.tensor(2.0)
output_tensor = torch.Tensor.float_power_(input_tensor, exponent)