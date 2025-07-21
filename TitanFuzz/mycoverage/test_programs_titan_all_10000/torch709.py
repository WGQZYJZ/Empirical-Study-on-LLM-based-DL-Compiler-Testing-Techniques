import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
split_size = 2
split_tensor = torch.Tensor.hsplit(input_tensor, split_size)