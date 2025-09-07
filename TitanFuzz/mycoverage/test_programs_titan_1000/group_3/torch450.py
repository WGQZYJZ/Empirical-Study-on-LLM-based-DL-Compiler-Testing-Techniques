import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 2)
other = torch.randn(2, 2)
torch.Tensor.arctanh_(input_tensor, other)