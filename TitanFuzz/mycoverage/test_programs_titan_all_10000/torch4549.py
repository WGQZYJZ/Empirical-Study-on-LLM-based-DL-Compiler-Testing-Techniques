import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 3)
other = torch.randn(5, 3)
output_tensor = torch.Tensor.subtract(input_tensor, other)