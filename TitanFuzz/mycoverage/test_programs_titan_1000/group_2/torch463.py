import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 7)
other = torch.randn(5, 7)
output_tensor = torch.Tensor.not_equal_(input_tensor, other)