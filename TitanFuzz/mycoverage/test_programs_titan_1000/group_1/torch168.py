import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 100)
y = torch.randn(1, 100)
z = torch.trapz(y, x=x)