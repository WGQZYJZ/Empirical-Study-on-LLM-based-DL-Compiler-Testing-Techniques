import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
result = torch.Tensor.atan2(input_tensor, other)
result = torch.atan2(input_tensor, other)
result = input_tensor.atan2(other)