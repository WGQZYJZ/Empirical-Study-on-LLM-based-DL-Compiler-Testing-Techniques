import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3, 3)
output_tensor = torch.Tensor.diff(input_tensor, n=1, dim=(- 1), prepend=None, append=None)