import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
triu_input = torch.triu(input)
triu_input = torch.triu(input, diagonal=1)
triu_input = torch.triu(input, diagonal=(- 1))
triu_input = torch.triu(input, diagonal=0)