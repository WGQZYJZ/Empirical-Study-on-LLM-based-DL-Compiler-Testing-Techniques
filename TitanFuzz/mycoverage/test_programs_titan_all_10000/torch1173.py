import torch
from torch import nn
from torch.autograd import Variable
x = torch.Tensor([[1, 1], [2, 2], [3, 3]])
y = torch.atleast_3d(x)