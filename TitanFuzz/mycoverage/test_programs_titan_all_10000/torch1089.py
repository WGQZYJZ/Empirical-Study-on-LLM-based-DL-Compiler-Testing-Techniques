import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 10)
exponent = torch.randn(10, 10)
torch.Tensor.float_power_(input_tensor, exponent)