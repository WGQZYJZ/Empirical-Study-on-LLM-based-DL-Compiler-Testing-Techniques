import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(3, 3)
b = torch.rand(3, 3)
c = torch.rand(3, 3)
torch.stack((a, b, c))
torch.stack((a, b, c), dim=1)