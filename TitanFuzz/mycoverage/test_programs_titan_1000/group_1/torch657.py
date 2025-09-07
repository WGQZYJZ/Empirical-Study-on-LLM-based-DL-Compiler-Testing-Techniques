import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(2, 3)
b = torch.randn(2, 3)
c = torch.randn(2, 3)
torch.dstack((a, b, c))