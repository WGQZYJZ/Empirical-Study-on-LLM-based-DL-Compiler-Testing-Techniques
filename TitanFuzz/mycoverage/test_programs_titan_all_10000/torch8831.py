import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
output = torch.diag(input)
output = torch.diag(input, diagonal=1)
output = torch.diag(input, diagonal=(- 1))