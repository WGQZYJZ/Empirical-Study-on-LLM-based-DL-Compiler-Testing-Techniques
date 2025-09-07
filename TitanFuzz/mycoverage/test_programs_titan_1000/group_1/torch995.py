import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(2, 2)
b = torch.rand(2, 2)
c = torch.hstack((a, b))