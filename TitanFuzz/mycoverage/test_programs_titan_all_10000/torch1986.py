import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(3, 4)
other = torch.rand(3, 4)
output = torch.less(input, other)