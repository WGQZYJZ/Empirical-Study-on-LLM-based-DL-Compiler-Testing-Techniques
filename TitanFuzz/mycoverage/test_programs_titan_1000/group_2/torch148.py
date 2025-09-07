import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 3)
other = torch.randn(4, 3)
result = torch.Tensor.cross(input_tensor, other, dim=(- 1))
input_tensor = torch.randn(4, 3)
other = torch.randn(4, 3)
result = torch.cross(input_tensor, other, dim=(- 1))