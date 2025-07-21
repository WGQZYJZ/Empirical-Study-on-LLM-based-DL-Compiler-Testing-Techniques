import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(6).view(2, 3)
y = torch.swapdims(x, 0, 1)