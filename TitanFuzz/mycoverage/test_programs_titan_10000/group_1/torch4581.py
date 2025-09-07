import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(3, 4)
y = torch.rand(3, 4)
z = torch.rand(3, 4)
torch.dstack((x, y, z))
torch.dstack((x, y, z)).shape