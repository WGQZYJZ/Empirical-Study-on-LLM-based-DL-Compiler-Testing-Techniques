import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
other = torch.randn(2, 3)
less = torch.less(input, other)