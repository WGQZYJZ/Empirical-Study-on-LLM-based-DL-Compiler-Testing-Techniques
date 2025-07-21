import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3)
y = torch.rand(4, 3)
z = torch.rand(2, 4)
result = torch.block_diag(x, y, z)