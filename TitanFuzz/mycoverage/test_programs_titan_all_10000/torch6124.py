import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 4)
y = torch.arange(1, 3)
z = torch.arange(1, 5)
torch.cartesian_prod(x, y, z)