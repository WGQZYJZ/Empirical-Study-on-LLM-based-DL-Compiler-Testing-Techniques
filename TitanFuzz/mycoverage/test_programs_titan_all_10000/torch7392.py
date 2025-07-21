import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 2, 3, 4, 5)
y = torch.fft.rfftn(x, 3)
z = torch.fft.irfftn(y, 3)