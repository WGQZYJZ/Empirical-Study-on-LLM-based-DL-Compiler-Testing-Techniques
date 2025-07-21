import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 10)
other = torch.rand(10, 10)
result = torch.Tensor.hypot(input_tensor, other)