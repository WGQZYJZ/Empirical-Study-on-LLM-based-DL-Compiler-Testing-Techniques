import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
index = torch.tensor([1, 2, 0])
src = torch.tensor([2, 3, 4])
torch.Tensor.scatter_add_(input_tensor, dim=0, index=index, src=src)