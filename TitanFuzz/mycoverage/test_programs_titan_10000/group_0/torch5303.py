import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(1, 1, requires_grad=True)
out = torch.fix(input)