import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(10, 3)
torch.msort(input)
input = torch.rand(10, 3)
torch.median(input)