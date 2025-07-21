import torch
from torch import nn
from torch.autograd import Variable
x = torch.Tensor([[1, 2, 3], [1, 2, 3]])
torch.sum(x, dim=1)
x = torch.Tensor([[1, 2, 3], [1, 2, 3]])
torch.sum(x, dim=1, keepdim=True)