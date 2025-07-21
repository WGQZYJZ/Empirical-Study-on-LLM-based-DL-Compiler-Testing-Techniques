import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[2, 3], [4, 5]])
other = torch.Tensor([[1, 2], [3, 4]])
result = torch.Tensor.hypot_(input_tensor, other)
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
dim = 1
index = torch.LongTensor([0, 1, 1])