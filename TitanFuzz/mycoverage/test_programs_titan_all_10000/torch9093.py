import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
split_tensor = torch.Tensor.split(input_tensor, 2, dim=0)
split_tensor = torch.Tensor.split(input_tensor, 2, dim=1)
split_tensor = torch.Tensor.split(input_tensor, [2, 2], dim=0)
split_tensor = torch.Tensor.split(input_tensor, [2, 2], dim=1)