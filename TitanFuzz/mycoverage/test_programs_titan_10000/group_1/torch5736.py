import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(2, 3)
unbind_input = torch.unbind(input, dim=0)