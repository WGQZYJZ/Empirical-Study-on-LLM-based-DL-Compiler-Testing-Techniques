import torch
from torch import nn
from torch.autograd import Variable

x = torch.arange(18).view(3, 2, 3)
y = torch.arange(27).view(3, 3, 3)