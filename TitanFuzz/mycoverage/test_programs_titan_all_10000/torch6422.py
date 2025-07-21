import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 6)
split_size = 2
split_tensor = torch.Tensor.split(input_tensor, split_size, dim=0)
split_tensor = torch.Tensor.split(input_tensor, split_size, dim=1)