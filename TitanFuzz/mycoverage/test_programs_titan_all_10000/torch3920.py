import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(4, dtype=torch.float)
output = torch.diagflat(input, offset=0)