import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3, 3)
expanded_tensor = torch.Tensor.expand_as(input_tensor, other)