import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([10, 20, 30])
z = torch.tensor([100, 200])
out = torch.cartesian_prod(x, y, z)