import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
dim = 0
index = torch.tensor([1, 2, 3])
src = torch.tensor([1, 2, 3])
output_tensor = torch.Tensor.scatter_add(input_tensor, dim, index, src)