import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3, 5)
y = torch.swapaxes(x, 0, 1)