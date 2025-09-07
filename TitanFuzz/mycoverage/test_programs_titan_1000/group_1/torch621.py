import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3)
y = torch.rand(2, 3)
z = torch.cat((x, y), dim=0)
z = torch.cat((x, y), dim=1)