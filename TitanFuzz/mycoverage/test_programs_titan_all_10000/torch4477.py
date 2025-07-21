import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 5)
y = torch.rand(3, 5)
z = torch.rand(3, 5)
result = torch.column_stack((x, y, z))