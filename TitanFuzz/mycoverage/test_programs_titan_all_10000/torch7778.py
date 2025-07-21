import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(3, 4)
b = torch.randn(3, 4)
c = torch.randn(3, 4)
torch.Tensor.index_add(a, 0, torch.tensor([0, 2]), b)
torch.Tensor.index_add(a, 1, torch.tensor([0, 2]), c)
a = torch.randn(3, 4)