import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(5, 5, 5)
result = torch.dsplit(a, 5)