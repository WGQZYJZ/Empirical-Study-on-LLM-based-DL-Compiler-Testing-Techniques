import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 5)
other = torch.randn(4, 5)
result = torch.Tensor.not_equal(input_tensor, other)