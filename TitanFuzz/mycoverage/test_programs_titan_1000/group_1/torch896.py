import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 5)
other = torch.randn(3, 5)
result = torch.Tensor.subtract_(input_tensor, other)