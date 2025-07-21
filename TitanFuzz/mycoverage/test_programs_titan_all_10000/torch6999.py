import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
divisor = 2
output_tensor = torch.Tensor.remainder(input_tensor, divisor)