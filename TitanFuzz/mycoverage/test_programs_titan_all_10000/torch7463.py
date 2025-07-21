import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 5)
index = torch.tensor([0, 2, 0, 0, 1])
src = torch.randn(5)
output_tensor = torch.Tensor.scatter_add_(input_tensor, dim=0, index=index, src=src)
input_tensor = torch.randn(3, 5)
index = torch.tensor([0, 2, 0, 0, 1])
src = torch.randn(5)
output_tensor = torch.Tensor.scatter_add_(input_tensor, dim=0, index=index, src=src)