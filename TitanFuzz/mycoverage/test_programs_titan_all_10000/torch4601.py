import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
output_tensor = torch.Tensor.subtract_(input_tensor, other)
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.sum(input_tensor)