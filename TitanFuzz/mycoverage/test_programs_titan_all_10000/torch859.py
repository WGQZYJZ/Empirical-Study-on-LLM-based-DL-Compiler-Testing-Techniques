import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 3)
other = torch.randn(5, 3)
result = torch.Tensor.le(input_tensor, other)