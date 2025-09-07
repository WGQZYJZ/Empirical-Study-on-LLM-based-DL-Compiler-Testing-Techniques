import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(2, 3)
torch.diagflat(input, offset=0)