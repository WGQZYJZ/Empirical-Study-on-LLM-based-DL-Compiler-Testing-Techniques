import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
other = torch.Tensor([[1, 1, 1], [1, 1, 1]])
result = torch.Tensor.subtract_(input_tensor, other)