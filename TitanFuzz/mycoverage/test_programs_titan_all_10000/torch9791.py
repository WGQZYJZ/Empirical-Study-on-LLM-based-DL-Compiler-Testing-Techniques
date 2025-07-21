import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
index = torch.tensor([[0, 1], [1, 0]])
src = torch.randn(2, 2)
output_tensor = torch.Tensor.scatter_add_(input_tensor, dim=0, index=index, src=src)