import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4)
other = torch.randn(2, 3, 4)
result = torch.Tensor.lt_(input_tensor, other)