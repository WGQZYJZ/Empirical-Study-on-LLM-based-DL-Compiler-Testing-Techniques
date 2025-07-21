import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(3, 4)
b = torch.randn(3, 4)
c = torch.randn(4, 4)
torch.row_stack((a, b))
torch.row_stack((a, b, c))