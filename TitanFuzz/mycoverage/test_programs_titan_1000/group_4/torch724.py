import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
torch.Tensor.copysign(input_tensor, other)
input_tensor = torch.randn(2, 3)
torch.Tensor.cos(input_tensor)