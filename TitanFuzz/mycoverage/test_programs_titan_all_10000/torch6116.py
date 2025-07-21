import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
other = 0.5
result = torch.Tensor.less_equal_(input_tensor, other)