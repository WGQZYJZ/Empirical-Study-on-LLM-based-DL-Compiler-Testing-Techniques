import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
output = torch.Tensor.igamma(input_tensor, other)