import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
split_tensor = torch.Tensor.hsplit(input_tensor, 2)
split_tensor = torch.Tensor.hsplit(input_tensor, [1, 3])