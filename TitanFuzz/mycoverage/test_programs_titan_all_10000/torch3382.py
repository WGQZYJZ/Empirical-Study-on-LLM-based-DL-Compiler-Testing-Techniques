import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 5)
other = torch.randn(5, 5)
output = torch.Tensor.igammac_(input_tensor, other)