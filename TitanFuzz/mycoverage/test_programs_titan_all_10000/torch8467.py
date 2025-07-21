import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, 4)
y = torch.randn(3, 4, 5)
z = torch.randn(4, 5, 6)
result = torch.einsum('ijk,jkl,klm->ilm', x, y, z)