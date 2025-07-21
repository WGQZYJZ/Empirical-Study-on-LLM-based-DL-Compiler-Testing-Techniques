import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
indices = torch.tensor([[0, 1, 2], [1, 2, 0], [0, 1, 2]])
dim = 1
result = torch.Tensor.take_along_dim(input_tensor, indices, dim)