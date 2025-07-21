import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 4)
torch.unbind(x, dim=0)
torch.unbind(x, dim=1)