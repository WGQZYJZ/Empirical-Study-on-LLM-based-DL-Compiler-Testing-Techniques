import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 2)
other = torch.rand(3, 2)
result = torch.Tensor.less_equal(input_tensor, other)
result = torch.Tensor.le(input_tensor, other)
result = torch.le(input_tensor, other)