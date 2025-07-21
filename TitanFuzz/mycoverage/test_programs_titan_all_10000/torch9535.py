import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
divisor = 3.0
output_tensor = torch.Tensor.remainder(input_tensor, divisor)