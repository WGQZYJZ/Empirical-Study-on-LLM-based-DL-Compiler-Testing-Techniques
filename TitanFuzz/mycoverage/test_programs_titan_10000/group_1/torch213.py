import torch
from torch import nn
from torch.autograd import Variable

x = torch.arange(0, 9).view(3, 3)
y = torch.swapaxes(x, 0, 1)