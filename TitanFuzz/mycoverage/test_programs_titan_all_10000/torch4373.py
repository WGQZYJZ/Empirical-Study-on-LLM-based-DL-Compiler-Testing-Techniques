import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(3, 4)
index = torch.tensor([1, 2])
src = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
torch.Tensor.scatter_(data, dim=0, index=index, src=src)