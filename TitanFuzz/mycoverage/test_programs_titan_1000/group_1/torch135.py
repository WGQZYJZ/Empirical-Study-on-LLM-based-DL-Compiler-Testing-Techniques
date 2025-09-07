import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 4)
index = torch.tensor([[0, 1, 2, 0], [3, 0, 0, 2]])
src = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
output_tensor = torch.Tensor.scatter_add_(input_tensor, dim=0, index=index, src=src)