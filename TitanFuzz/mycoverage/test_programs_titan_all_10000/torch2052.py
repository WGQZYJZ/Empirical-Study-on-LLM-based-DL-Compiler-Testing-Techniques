import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
index = torch.tensor([0, 1, 2, 0, 1, 2])
src = torch.tensor([1, 1, 1, 1, 1, 1])
output_tensor = torch.Tensor.scatter_add(input_tensor, dim=0, index=index, src=src)