import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 3)
index = torch.tensor([0, 2, 1, 2])
src = torch.tensor([1.0, 2.0, 3.0, 4.0])
output_tensor = torch.Tensor.scatter_add(input_tensor, 0, index, src)