import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
y = torch.randn(3, 4)
z = torch.randn(3, 4)
torch.column_stack((x, y, z))