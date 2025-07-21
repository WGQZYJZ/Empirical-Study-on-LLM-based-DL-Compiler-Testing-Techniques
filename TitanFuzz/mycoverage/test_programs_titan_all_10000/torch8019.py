import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, dtype=torch.float32)
exponent = torch.tensor([2, 3, 4])
output_tensor = torch.Tensor.float_power_(input_tensor, exponent)