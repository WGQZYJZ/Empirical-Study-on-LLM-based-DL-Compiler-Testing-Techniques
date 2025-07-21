import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(3, 4)
b = torch.rand(3, 4)
c = torch.rand(3, 4)
d = torch.row_stack((a, b, c))