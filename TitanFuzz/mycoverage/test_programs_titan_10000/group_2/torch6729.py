import torch
from torch import nn
from torch.autograd import Variable

x = torch.arange(0, 4)
y = torch.tile(x, (2,))
y = torch.tile(x, (2, 1))
y = torch.tile(x, (2, 2))