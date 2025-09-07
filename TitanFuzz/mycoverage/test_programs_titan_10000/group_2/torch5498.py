import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 3)
other = torch.randn(3, 4)
out = torch.Tensor.vdot(input_tensor, other)