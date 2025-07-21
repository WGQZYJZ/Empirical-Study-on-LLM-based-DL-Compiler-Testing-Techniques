import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
other = 0.5
output_tensor = torch.Tensor.greater_equal_(input_tensor, other)