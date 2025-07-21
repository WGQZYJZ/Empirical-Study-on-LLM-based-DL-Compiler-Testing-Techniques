import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(4, 3)
b = torch.randn(4, 1)
c = torch.column_stack((a, b))